import discord

class ApplicationModal(discord.ui.Modal, title="Dragons Den Application"):

    language = discord.ui.TextInput(
        label="Language",
        placeholder="English / Dutch / German...",
        required=True,
        max_length=20
    )

    guild = discord.ui.TextInput(
        label="Guild",
        placeholder="Which guild do you want to join?",
        required=True,
        max_length=30
    )

    rank = discord.ui.TextInput(
        label="Rank",
        placeholder="Member / Veteran / Officer...",
        required=True,
        max_length=20
    )

    ingame_name = discord.ui.TextInput(
        label="In-game Name",
        placeholder="Enter your in-game name...",
        required=True,
        max_length=30
    )

    async def on_submit(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="📋 New Application",
            color=0xC49A3A
        )

        embed.add_field(name="🌍 Language", value=self.language.value, inline=False)
        embed.add_field(name="🏰 Guild", value=self.guild.value, inline=False)
        embed.add_field(name="⚔️ Rank", value=self.rank.value, inline=False)
        embed.add_field(name="🎮 In-game Name", value=self.ingame_name.value, inline=False)

        embed.set_footer(
            text=f"Discord User: {interaction.user}"
        )

        await interaction.channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Your application has been submitted!",
            ephemeral=True
        )
class ApplyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Apply",
        emoji="📝",
        style=discord.ButtonStyle.green,
        custom_id="apply_button"
    )
    async def apply(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_modal(ApplicationModal())