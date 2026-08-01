import discord
from discord.ext import commands

from views.castle_views import CastleMainView


class Castle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="castle",
        description="Browse castle skins"
    )
    async def castle(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🗿 Castle Skins",
            description="Choose an option below.",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(
            embed=embed,
            view=CastleMainView(),
            ephemeral=False
        )


async def setup(bot):
    await bot.add_cog(Castle(bot))