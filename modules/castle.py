import discord
from discord import app_commands
from discord.ext import commands

from views.castle_views import CastleSelectView


class Castle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="castle",
        description="Browse all castle skins."
    )
    async def castle(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="Castle Database",
            description="Choose a castle skin from the dropdown below.",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(
            embed=embed,
            view=CastleSelectView()
        )


async def setup(bot):
    await bot.add_cog(Castle(bot))