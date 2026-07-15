import discord
from discord.ext import commands


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

    async def setup_hook(self):
        await self.load_extension("setup")
        await self.load_extension("modules.draco")
        await self.load_extension("modules.command_center")
        await self.load_extension("modules.timezone")
        await self.load_extension("modules.victory")
        await self.load_extension("modules.events")
        await self.tree.sync()
    async def on_ready(self):

        print("-" * 50)
        print(f"🐉 Logged in as {self.user}")
        print("-" * 50)

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Dragons Den Server"
            )
        )