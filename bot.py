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

    async def setup_hook(self):
        print("Loading setup")
        await self.load_extension("setup")

        print("Loading draco")
        await self.load_extension("modules.draco")

        print("Loading command_center")
        await self.load_extension("modules.command_center")

        print("Loading timezone")
        await self.load_extension("modules.timezone")

        print("Loading scheduler")
        await self.load_extension("modules.scheduler")

        print("Loading victory")
        await self.load_extension("modules.victory")

        print("Loading events")
        await self.load_extension("modules.events")

        print("Syncing tree")
        await self.tree.sync()

        print("setup_hook finished")
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