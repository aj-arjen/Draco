import discord


class CommandCenterSelect(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="General",
                emoji="🏠",
                description="General Draco commands"
            ),
            discord.SelectOption(
                label="Gift Codes",
                emoji="🎁",
                description="Gift code commands"
            ),
            discord.SelectOption(
                label="Alerts",
                emoji="🚨",
                description="Alert commands"
            ),
            discord.SelectOption(
                label="Applications",
                emoji="📝",
                description="Application system"
            ),
            discord.SelectOption(
                label="Coming Soon",
                emoji="🚧",
                description="Future features"
            ),
        ]

        super().__init__(
            placeholder="Choose a category...",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"You selected **{self.values[0]}**.",
            ephemeral=True
        )


class CommandCenterView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CommandCenterSelect())