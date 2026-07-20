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
    @app_commands.describe(hero="The hero to view.")
    async def hero(
        self,
        interaction: discord.Interaction,
        hero: str
    ):

        base_path = Path("hero_database/factions")

        hero_file = None

        rarities = [
            "common",
            "rare",
            "epic",
            "legendary",
            "mythic"
        ]

        # Search every faction and rarity
        for faction in base_path.iterdir():

            heroes_folder = faction / "heroes"

            if not heroes_folder.exists():
                continue

            for rarity in rarities:

                candidate = (
                    heroes_folder /
                    rarity /
                    f"{hero.lower()}.json"
                )

                if candidate.exists():
                    hero_file = candidate
                    break

            if hero_file:
                break

        if hero_file is None:
            await interaction.response.send_message(
                f"❌ Hero **{hero}** was not found.",
                ephemeral=True
            )
            return

        with open(hero_file, "r", encoding="utf-8") as f:
            hero = json.load(f)

        # --------------------------------------------------
        # Embed color based on faction
        # --------------------------------------------------

        faction_colors = {
            "League": 0x3498DB,
            "Horde": 0xE74C3C,
            "Nature": 0x2ECC71
        }

        color = faction_colors.get(hero["faction"], 0xC49A3A)

        # --------------------------------------------------
        # Position formatting
        # --------------------------------------------------

        position = hero["position"]

        if position.lower() == "front":
            position = "Frontline"
        elif position.lower() == "middle":
            position = "Midline"
        elif position.lower() == "back":
            position = "Backline"

        # --------------------------------------------------
        # Hero thumbnail
        # --------------------------------------------------

        image_path = (
            f"hero_database/factions/"
            f"{hero['faction'].lower()}/heroes/images/"
            f"{hero['id']}.png"
        )

        file = discord.File(
            image_path,
            filename=f"{hero['id']}.png"
        )

        # --------------------------------------------------
        # Investment
        # --------------------------------------------------

        filled = "⭐" * hero["investment"]["stars"]
        empty = "✩" * (5 - hero["investment"]["stars"])
        stars = filled + empty

        # --------------------------------------------------
        # Embed
        # --------------------------------------------------

        embed = discord.Embed(
            title=hero["name"],
            description=(
                f"**{hero['faction']} • {hero['rarity']}**\n"
                f"**{hero['class']} • {position}**\n\n"
                f"**Description**\n"
                f"{hero['description']}"
            ),
            color=color
        )

        embed.set_thumbnail(
            url=f"attachment://{hero['id']}.png"
        )

        embed.add_field(
            name="Recommended Gear",
            value=(
                f"**{hero['gear']['recommended'].replace('_', ' ').title()}**\n\n"
                f"{' → '.join(item.title() for item in hero['gear']['priority'])}"
            ),
            inline=False
        )

        embed.add_field(
            name="Investment",
            value=(
                f"{stars} • {hero['investment']['rating']}"
            ),
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            file=file
        )


async def setup(bot):
    await bot.add_cog(Hero(bot))