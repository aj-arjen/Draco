import discord
from discord.ext import commands

APPRECIATION_CHANNEL_ID = 1527383558061035641

class AppreciationModal(discord.ui.Modal, title="❤️ Appreciation"):

    message = discord.ui.TextInput(
        label="Your appreciation",
        style=discord.TextStyle.paragraph,
        placeholder="Write your appreciation here...",
        required=True,
        max_length=1000,
    )

    async def on_submit(self, interaction: discord.Interaction):

        channel = interaction.guild.get_channel(APPRECIATION_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Appreciation channel not found.",
                ephemeral=True,
            )
            return

        embed = discord.Embed(
            title="❤️ New Appreciation",
            color=0xC49A3A,
        )

        embed.add_field(
            name="💬 Message",
            value=self.message.value,
            inline=False,
        )

        embed.add_field(
            name="👤 From",
            value=interaction.user.mention,
            inline=False,
        )

        embed.timestamp = discord.utils.utcnow()

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "❤️ Thank you for your kind words!",
            ephemeral=True,
        )
class Appreciation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="appreciation",
        description="Show your appreciation for all the work that was put into creating this server."
    )
    async def appreciation(
        self,
        interaction: discord.Interaction
    ):
        await interaction.response.send_modal(
            AppreciationModal()
        )


async def setup(bot):
    await bot.add_cog(Appreciation(bot))