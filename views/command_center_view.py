import discord
import traceback

class CommandCenterSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Translation", emoji="💬", description="Translate messages"),
            discord.SelectOption(label="Gift Codes", emoji="🎁", description="View all Gift Codes commands"),
            discord.SelectOption(label="Red Alerts", emoji="🚨", description="Red Alert commands"),
            discord.SelectOption(label="Hero Database", emoji="📚", description="Browse heroes, gear, etc."),
            discord.SelectOption(label="Suggestions", emoji="💡", description="Share your ideas"),
            discord.SelectOption(label="Appreciation", emoji="❤️", description="Show your appreciation"),
        ]
        super().__init__(
            placeholder="Choose a category...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            choice = self.values[0]
            embed = discord.Embed(color=0xC49A3A)

            if choice == "Gift Codes":
                embed.title = "🎁 Gift Codes"
                embed.description = (
                    "Help this community by adding the latest giftcodes.\n\n"
                    "**Command:** \n"
                    '/giftcode "add giftcode here"'
                )
                image = "draco_gift.png"

            elif choice == "Translation":
                embed.title = "💬 Translation"
                embed.description = (
                    "💬 **Translate Messages**\n"
                    "Use `/translate` on any message to instantly read it in your own language.\n\n"
                    "🌎 Connect with players from all over the world.\n\n"
                    "💡 More translation features are hopefully coming in the future."
                )
                image = "draco_help.png"

            elif choice == "Red Alerts":
                embed.title = "🚨 Red Alerts"
                embed.description = (
                    "**Command:** \n\n"
                    "`/alert`\n"
                    "Send a Red Alert."
                )
                image = "draco_surprised.png"

            elif choice == "Hero Database":
                embed.title = "📚 Hero Database"
                embed.description = (
                    "The Hero Database is currently under construction.\n\n"
                    "In the future, this will be the place where you'll find everything you need to know "
                    "about Heroes, Factions, Gear, Best Lineups and much more... 🐉"
                )
                image = "draco_underconstruction.png"

            elif choice == "Suggestions":
                embed.title = "💡 Suggestions"
                embed.description = (
                    "Share your ideas to help improve Draco and the Dragons Den community.\n\n"
                    "**Command:** `/suggestion 'type suggestion here'`"
                )
                image = "draco_idea.png"

            elif choice == "Appreciation":
                embed.title = "❤️ Appreciation"
                embed.description = (
                    "Show your appreciation if you like all the work I've put into this server.\n\n"
                    "**Command:** `/appreciation`"
                )
                image = "draco_love.png"

            else:
                embed.title = "🚧 Under Construction"
                embed.description = "This module is still under development."
                image = "draco_underconstruction.png"

            file = discord.File(f"assets/reactions/{image}", filename=image)
            embed.set_image(url=f"attachment://{image}")

            await interaction.response.edit_message(
                embed=embed,
                attachments=[file],
                view=self.view
            )

        except Exception:
            traceback.print_exc()
            raise

class CommandCenterView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CommandCenterSelect())
