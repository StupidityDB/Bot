import discord
from discord.ext import commands
from lib.stupiditydb import StupidityDB


class Stupidity(commands.Cog):
    """Operations involving stupiditydb"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.stupiditydb: StupidityDB = StupidityDB()

    @commands.hybrid_command(name="stupit")
    async def get_stupidity(self, ctx, *, user: discord.User):
        """Get stupidity of a specific user"""
        stupidity = await self.stupiditydb.get_user_stupidity(user.id)
        await ctx.send(f"Stupidity: {stupidity}%")

    @commands.hybrid_command(name="stupitvote")
    async def vote_stupidity(self, ctx, user: discord.User):
        """Vote for someone's stupidity"""
        ok = await self.stupiditydb.vote_user(user.id, ctx.author.id)
        if ok:
            await ctx.send("Voted!")


async def setup(bot):
    await bot.add_cog(Stupidity(bot))
