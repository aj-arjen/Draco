import discord
from discord.ext import commands

SUGGESTIONS_CHANNEL_ID = 1526714924464865481


class SuggestionModal(discord.ui.Modal, title="💡 New Suggestion"):
    suggestion = discord.ui.TextInput(
        label="Your suggestion",
        style=discord.TextStyle.paragraph,
        placeholder="Share your idea for Draco or the server...",
        required=True,
        max_length=1000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(SUGGESTIONS_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Suggestions channel not found.",
                ephemeral=True,
            )
            return

        embed = discord.Embed(
            title="💡 New Suggestion",
            description=self.suggestion.value,
            color=0xC49A3A,
        )

        embed.add_field(
            name="Suggested by",
            value=interaction.user.mention,
            inline=False,
        )

        message = await channel.send(embed=embed)
        await message.add_reaction("👍🏻")
        await message.add_reaction("👎🏻")

        await interaction.response.send_message(
            "✅ Thank you! Your suggestion has been submitted.",
            ephemeral=True,
        )


class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="suggestion",
        description="Submit a suggestion for Draco or the server.",
    )
    async def suggestion(self, interaction: discord.Interaction):
        await interaction.response.send_modal(SuggestionModal())


async def setup(bot):
    await bot.add_cog(Suggestions(bot))
