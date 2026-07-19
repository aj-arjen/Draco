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

        embed = discord.Embed(
            title=hero["name"],
            description=(
                f'{hero["faction"]} • '
                f'{hero["rarity"]} • '
                f'{hero["class"]} • '
                f'{hero["position"]}\n\n'
                f'📝 **Description**\n'
                f'{hero["description"]}'
            )
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