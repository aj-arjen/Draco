import discord
from discord.ext import commands

print("BOT.PY LOADED")


class Draco(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def on_ready(self):
        print("-" * 40)
        print(f"🐉 Logged in as {self.user}")
        print("-" * 40)

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Dragons Den Server"
            )
        )
