import io
import textwrap
import traceback
from contextlib import redirect_stdout

from discord.ext import commands


class Utility(commands.Cog):
    """Simple Utilities"""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = ""

    def cleanup_code(self, content: str) -> str:
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])

    @commands.hybrid_command()
    async def ping(self, ctx):
        """Replies with Pong to indicate that the bot is alive"""
        await ctx.reply(f"Pong! {round(1000*self.bot.latency, 2)}ms")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, module):
        try:
            await self.bot.reload_extension(module)
        except commands.ExtensionNotLoaded:
            await self.bot.load_extension(module)
        await ctx.reply("Reloaded")

    @commands.command(hidden=True, name="eval")
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            "bot": self.bot,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "_": self._last_result,
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as error:
            return await ctx.send(f"```py\n{error.__class__.__name__}: {error}\n```")

        func = env["func"]
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception:
            value = stdout.getvalue()
            await ctx.send(f"```py\n{value}{traceback.format_exc()}\n```")
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction("\u2705")
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f"```py\n{value}\n```")
            else:
                self._last_result = ret
                await ctx.send(f"```py\n{value}{ret}\n```")


async def setup(bot):
    await bot.add_cog(Utility(bot))
