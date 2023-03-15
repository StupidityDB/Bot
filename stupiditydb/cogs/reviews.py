from typing import List

from lib.reviewdb import ReviewDB, Review

from discord.ext import commands
import discord


class Reviews(commands.Cog):
    """Operations involving reviews"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.reviewdb: ReviewDB = ReviewDB()

    @commands.hybrid_command(name="get")
    async def get_reviews(self, ctx, *, user: discord.User):
        """Get reviews of a specific user"""
        review_list: List[Review] = await self.reviewdb.get_user_reviews(user.id)
        if not review_list:
            return await ctx.send("No reviews found")
        embeds: List[discord.Embed] = []
        for review in review_list[:10]:
            embed = discord.Embed(title="Review", description=review.comment)
            embed.add_field(name="Author", value=review.user_id)
            embed.add_field(name="Date Posted", value=f"<t:{review.timestamp}>")
            embeds.append(embed)
        await ctx.send(f"{len(embeds)} reviews", embeds=embeds)

async def setup(bot):
    await bot.add_cog(Reviews(bot))
