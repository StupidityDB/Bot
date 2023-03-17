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
        await ctx.send(
            f"Stupidity: {stupidity}%"
            if stupidity not in ["None", None]
            else "This user has no stupidity votes."
        )

    @commands.hybrid_command(name="stupitvote")
    async def vote_stupidity(
        self, ctx, user: discord.User, stupidity_level: commands.Range[int, 0, 100]
    ):
        """Vote for someone's stupidity"""
        ok = await self.stupiditydb.vote_user(user.id, ctx.author.id, stupidity_level)
        if ok:
            await ctx.send("Voted!")


async def setup(bot):
    await bot.add_cog(Stupidity(bot))
