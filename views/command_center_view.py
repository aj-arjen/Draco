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
                label="Red Alerts",
                emoji="🚨",
                description="Red Alert commands"
            ),
            discord.SelectOption(
                label="Hero Database",
                emoji="📚",
                description="Browse heroes, gear, etc.."
            ),

            discord.SelectOption(
                label="Suggestions",
                emoji="💡",
                description="Share your ideas for Draco or this server"
            ),
            
            discord.SelectOption(
                label="Appreciation",
                emoji="❤️",
                description="Show your appreciation if you like all the work I've put into this"
            ),

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

        elif choice == "Hero Database":

            embed.title = "📚 Hero Database"

            embed.description = (
        "The Hero Database is currently under construction.\n\n"
        "In the future, this will be the place where you'll find "
        "everything you need to know about Heroes, Factions, Gear, "
        "Best Lineups and much more... 🐉"
            )

            file = discord.File(
        "assets/reactions/draco_underconstruction.png",
            filename="draco_underconstruction.png"
            )

            embed.set_image(
            url="attachment://draco_underconstruction.png"
            )
       elif choice == "Suggestions":

            embed.title = "💡 Suggestions"

            embed.description = (
        "Share your ideas to help improve Draco and the Dragons Den community.\n\n"
        "**Command:** `/suggestion`"
            )

            file = discord.File(
        "assets/reactions/draco_idea.png",
            filename="draco_idea.png"
            )

            embed.set_image(
                url="attachment://draco_idea.png"
            )


        elif choice == "Appreciation":

            embed.title = "❤️ Appreciation"

            embed.description = (
        "Show your appreciation if you like all the work I've put into this server.\n\n"
        "**Command:** `/appreciation`"
            )

            file = discord.File(
        "assets/reactions/draco_love.png",
            filename="draco_love.png"
            )

            embed.set_image(
                url="attachment://draco_love.png"
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