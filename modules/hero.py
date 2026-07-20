import discord
from discord import app_commands
from discord.ext import commands

from views.hero_views import FactionView


class Hero(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="hero",
        description="Browse heroes by faction and rarity."
    )
    async def hero(
        self,
        interaction: discord.Interaction
    ):
        await interaction.response.send_message(
            content="Choose a faction:",
            view=FactionView(),
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Hero(bot))