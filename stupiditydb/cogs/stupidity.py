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


async def setup(bot):
    await bot.add_cog(Stupidity(bot))
