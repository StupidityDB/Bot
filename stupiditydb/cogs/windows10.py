from typing import Literal

from discord.ext import commands
import discord
from discord import app_commands


class Windows10(commands.Cog):
    """Windows 10 Downloader"""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @app_commands.describe(version="Windows Version")
    async def windows(self, ctx, version: Literal["11", "10", "8.1"]):
        """Get Windows 10 for FREE! Directly from the Microsoft website."""
        version_dict = {"10": 10, "8.1": 8, "11": 11}
        version = version_dict[version]
        await ctx.send(
            f"https://microsoft.com/software-download/windows{version}\nNote:\n> If you are using Microsoft Windows, spoof your user agent to a different operating system for the best results."
        )


async def setup(bot):
    await bot.add_cog(Windows10(bot))
