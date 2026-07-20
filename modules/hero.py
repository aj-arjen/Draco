import discord
from discord import app_commands
from discord.ext import commands

from utils.hero_loader import load_hero
from utils.hero_embed import build_hero_embed


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
        hero_data = load_hero(hero)

        if hero_data is None:
            await interaction.response.send_message(
                f"❌ Hero **{hero}** was not found.",
                ephemeral=True
            )
            return

        embed, file = build_hero_embed(hero_data)

        await interaction.response.send_message(
            embed=embed,
            file=file
        )


async def setup(bot):
    await bot.add_cog(Hero(bot))