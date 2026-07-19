import discord
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

    import discord

    embed = discord.Embed(
        title=hero["name"],
        description=hero["description"],
    )

    embed.add_field(
        name="🏷️ Hero Info",
        value=(
            f'**Faction:** {hero["faction"]}\n'
            f'**Rarity:** {hero["rarity"]}\n'
            f'**Class:** {hero["class"]}\n'
            f'**Position:** {hero["position"]}'
        ),
        inline=False
    )

    embed.add_field(
        name="⚒️ Recommended Gear",
        value=(
            f'**{hero["gear"]["recommended"].replace("_", " ").title()}**\n'
            f'Priority: {" → ".join(hero["gear"]["priority"]).title()}'
        ),
        inline=False
    )

    await interaction.response.send_message(
    embed=embed
    )


async def setup(bot):
    await bot.add_cog(Hero(bot))