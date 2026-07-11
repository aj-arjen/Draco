import discord
from discord.ext import commands


class Setup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="setup",
        description="Post the Dragons Den application panel."
    )
    @discord.app_commands.default_permissions(administrator=True)
    async def setup(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🐉 Dragons Den Server",
            description=(
                "**Welcome, Warrior!**\n\n"
                "*We're excited to have you join this Top Heroes community, built for Server 10867.*"
            ),
            color=0xC49A3A
        )

        embed.add_field(
            name="📋 Submit Your Application",
            value=(
                "Before you can access the server, please complete your application.\n\n"
                "🌍 Select your language\n"
                "🏰 Choose your guild\n"
                "⚔️ Select your rank\n"
                "🎮 Enter your in-game name"
            ),
            inline=False
        )

        embed.add_field(
            name="🔒 Review Process",
            value=(
                "Once your application has been submitted, a Guild Leader will review it.\n\n"
                "After approval, you'll automatically receive access to the appropriate channels."
            ),
            inline=False
        )

        embed.add_field(
            name="⚠️ Important",
            value="Providing incorrect information may result in your application being declined.",
            inline=False
        )

        embed.set_footer(
            text="⚔️ Good luck, Warrior! — Draco 🐉"
        )

        await interaction.channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Application panel created.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Setup(bot))