import discord
from discord.ext import commands

from views.relic_views import RelicMainView


class Relic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="relic",
        description="Browse relics, recommendations and rankings."
    )
    async def relic(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🗿 Relics",
            description="Choose an option below.",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(
            embed=embed,
            view=RelicMainView(),
            ephemeral=False
        )


async def setup(bot):
    await bot.add_cog(Relic(bot))