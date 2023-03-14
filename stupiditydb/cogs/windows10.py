from discord.ext import commands
import discord

class Windows10(commands.Cog):
    """The description for Windows10 goes here."""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def windows10(self, ctx):
        """Get Windows 10 for FREE! Directly from the Microsoft website. No Virus, Real, Microsoft Official, Windows 10, Official Download 2023"""
        await ctx.send("https://microsoft.com/software-download/windows10ISO\nNote:\n> If you are using Microsoft Windows, spoof your user agent to a different operating system for the best results.")

async def setup(bot):
    await bot.add_cog(Windows10(bot))
