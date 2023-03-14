#!/usr/bin/env python3

from discord.ext import commands
import discord
import config


class Bot(commands.Bot):
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
#        self.metrics_msg = await bot.get_channel(1084587617015824456).fetch_message(1085267945829191770)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.reply(
                embed=discord.Embed(
                    title="Error",
                    description=f"🤯 You are not allowed to run this command.",
                )
            )


intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.watching, name="you being stupit")
bot = Bot(intents=intents, activity=activity)


bot.run(config.token)
