import discord
from discord.ext import commands
from views.command_center_view import CommandCenterView

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
        modules = [
            "setup",
            "modules.draco",
            "modules.hero",
            "modules.command_center",
            "modules.giftcode",
            "modules.victory",
            "modules.relic",
            "modules.redalert",
            "modules.suggestions",
            "modules.appreciation",
            "modules.say",
        ]

        for module in modules:
            try:
                print(f"Loading {module}...")
                await self.load_extension(module)
                print(f"Loaded {module}")
            except Exception as e:
                print(f"FAILED: {module}")
                print(repr(e))

        synced = await self.tree.sync()
        print(f"Synced {len(synced)} slash commands.")

    async def on_ready(self):
        print("-" * 40)
        print(f"🐉 Logged in as {self.user}")
        print(f"Guilds: {len(self.guilds)}")
        print("-" * 40)
        
        self.add_view(CommandCenterView())

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Dragons Den Server"
            )
        )