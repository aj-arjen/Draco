from discord import app_commands
from discord.ext import commands


class Hero(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="hero",
        description="View information about a hero."
    )
    async def hero(self, interaction):
        await interaction.response.send_message(
            "Hero command is working!"
        )


async def setup(bot):
    await bot.add_cog(Hero(bot))