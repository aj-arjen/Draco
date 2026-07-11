import discord


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
        await interaction.response.send_message(
            "🚧 Application form coming soon!",
            ephemeral=True
        )