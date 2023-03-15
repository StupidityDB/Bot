#!/usr/bin/env python3

"""
This is a bot for StupidityDB and ReviewDB
"""

from discord.ext import commands
import discord
import config


class Bot(commands.Bot):
    """
    Bot class containing the cog loader and error handler
    """

    def __init__(self, intents: discord.Intents, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or(">"), intents=intents, **kwargs
        )

    async def setup_hook(self):
        for cog in config.cogs:
            try:
                await self.load_extension(cog)
            except Exception as exc:
                print(
                    f"Could not load extension {cog} due to {exc.__class__.__name__}: {exc}"
                )

    async def on_ready(self):
        print(f"Logged on as {self.user} (ID: {self.user.id})")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.reply(
                embed=discord.Embed(
                    title="Error",
                    description="🤯 You are not allowed to run this command.",
                )
            )


intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.watching, name="you being stupit")
bot = Bot(intents=intents, activity=activity)


bot.run(config.token)
