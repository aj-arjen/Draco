import discord


class CommandCenterSelect(discord.ui.Select):

    def __init__(self):

        options = [
          
            discord.SelectOption(
                label="Translation",
                emoji="💬",
                description="Translate messages"
),

            discord.SelectOption(
                label="Gift Codes",
                emoji="🎁",
                description="View all gift code commands"
            ),

            discord.SelectOption(
                label="Applications",
                emoji="📝",
                description="Application system"
            ),

            discord.SelectOption(
                label="Red Alerts",
                emoji="🚨",
                description="Red Alert commands"
            ),

            discord.SelectOption(
                label="Suggestions",
                emoji="💡",
                description="Coming soon"
            ),

            discord.SelectOption(
                label="Hero Database",
                emoji="📚",
                description="Coming soon"
            )

        ]

        super().__init__(
            placeholder="Choose a category...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        choice = self.values[0]

        embed = discord.Embed(
            color=0xC49A3A
        )

        file = None

        if choice == "Gift Codes":

            embed.title = "🎁 Gift Codes"

            embed.description = (
                "Available commands:\n\n"
                "`/giftcode CODE`\n"
                "Example: `/giftcode DRAGON2026`"
            )

            file = discord.File(
                "assets/reactions/draco_gift.png",
                filename="draco_gift.png"
            )

            embed.set_image(
                url="attachment://draco_gift.png"
            )
            
        elif choice == "Translation":

            embed.title = "💬 Translation"

            embed.description = (
        "💬 **Translate Messages**\n"
        "Use `/translate` on any message to instantly read it in your own language.\n\n"

        "🌎 Connect with players from all over the world.\n\n"

        "💡 More translation features are hopefully coming in the future."
    )

            file = discord.File(
        "assets/reactions/draco_help.png",
                filename="draco_help.png"
    )

            embed.set_image(
        url="attachment://draco_help.png"
    )

        elif choice == "Applications":

            embed.title = "📝 Applications"

            embed.description = (
                "Available commands:\n\n"
                "`/setup`\n"
                "Creates the application panel."
            )

            file = discord.File(
                "assets/reactions/draco_welcome.png",
                filename="draco_welcome.png"
            )

            embed.set_image(
                url="attachment://draco_welcome.png"
            )

        elif choice == "Red Alerts":

            embed.title = "🚨 Red Alerts"

            embed.description = (
                "Available commands:\n\n"
                "`/alert`\n"
                "Send a Red Alert."
            )

            file = discord.File(
                "assets/reactions/draco_angry.png",
                filename="draco_angry.png"
            )

            embed.set_image(
                url="attachment://draco_angry.png"
            )

        else:

            embed.title = "🚧 Under Construction"

            embed.description = (
                "This module is still under development.\n\n"
                "Check back soon!"
            )

            file = discord.File(
                "assets/reactions/draco_underconstruction.png",
                filename="draco_underconstruction.png"
            )

            embed.set_image(
                url="attachment://draco_underconstruction.png"
            )

        await interaction.response.edit_message(
            embed=embed,
            attachments=[file],
            view=self.view
        )


class CommandCenterView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)

        self.add_item(
            CommandCenterSelect()
        )