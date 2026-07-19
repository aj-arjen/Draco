from discord import app_commands
from discord.ext import commands

import json
from pathlib import Path


class Hero(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="hero",
        description="View information about a hero."
    )
    async def hero(self, interaction):
    hero_file = Path(
        "hero_database/factions/league/heroes/legendary/adjudicator.json"
    )

        with open(hero_file, "r", encoding="utf-8") as f:
            hero = json.load(f)

        await interaction.response.send_message(
            hero["name"]
        )


async def setup(bot):
    await bot.add_cog(Hero(bot))