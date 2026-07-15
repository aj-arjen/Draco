import discord
from discord.ext import commands
from discord import app_commands

from config.config import GUILD_COUNCIL_ROLE_ID

GENERAL_CHANNEL_ID = 1525525149640556704


class Victory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="victory",
        description="Celebrate a Dragons Den victory."
    )
    async def victory(self, interaction: discord.Interaction):

        if not any(role.id == GUILD_COUNCIL_ROLE_ID for role in interaction.user.roles):
            await interaction.response.send_message(
                "❌ Only Guild Council members can use this command.",
                ephemeral=True
            )
            return
          await interaction.response.defer(ephemeral=True)

        channel = self.bot.get_channel(GENERAL_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ General channel not found.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🏆 We Are VICTORIOUS!",
            description=(
                "Together, we proved that teamwork, dedication, "
                "and determination always prevail.\n\n"
                "Thank you to everyone who gave it their all. "
                "This victory belongs to all of us.\n\n"
                "**🔥 On to the next!**"
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="— Draco 🐉"
        )

        file = discord.File(
            "assets/reactions/draco_victory.mp4",
            filename="draco_victory.mp4"
)

        await channel.send(
            embed=embed,
            file=file
)

        await interaction.followup.send(
    "🏆 Victory announcement posted successfully!",
            ephemeral=True
)


async def setup(bot):
    await bot.add_cog(Victory(bot))