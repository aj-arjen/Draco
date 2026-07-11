import discord

class ApplicationModal(discord.ui.Modal, title="Application"):

    ingame_name = discord.ui.TextInput(
        label="In-game Name",
        placeholder="Enter your in-game name...",
        required=True,
        max_length=30
    )

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"✅ Thank you, **{self.ingame_name}**!\n\n"
            "Your application has been received.\n\n"
            "More questions will follow shortly.",
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