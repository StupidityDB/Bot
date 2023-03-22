from typing import List

import discord
from discord.ext import commands
from lib.reviewdb import Review, ReviewDB
from reactionmenu import ViewButton, ViewMenu


class Reviews(commands.Cog):
    """Operations involving reviews"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.reviewdb: ReviewDB = ReviewDB()

    @commands.hybrid_group(name="reviews")
    async def reviews_group(self, ctx):
        """
        Group of commands for reviews"""
        await ctx.send_help(self.reviews_group)

    @reviews_group.command(name="get")
    async def get_reviews(self, ctx, *, user: discord.User):
        """Get reviews of a specific user"""
        review_list: List[Review] = await self.reviewdb.get_user_reviews(user.id)
        if not review_list:
            return await ctx.send("No reviews found")
        menu = ViewMenu(ctx.interaction or ctx, menu_type=ViewMenu.TypeEmbed)
        for review in review_list[:10]:
            embed = discord.Embed(
                title="Review", description=review.comment, timestamp=review.datetime()
            )
            embed.set_author(name=review.user["name"], icon_url=review.user["avatar"])
            menu.add_page(embed)
        menu.add_button(ViewButton.back())
        menu.add_button(ViewButton.next())
        await menu.start()

    @reviews_group.command(name="add")
    async def create_review(self, ctx, user: discord.User, *, comment: str):
        """Create a review"""
        await self.reviewdb.create_user_review(ctx.author, user, comment)
        await ctx.send("Review created")


async def setup(bot):
    await bot.add_cog(Reviews(bot))
