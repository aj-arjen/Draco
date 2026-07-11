import discord

from bot import Draco
from settings import TOKEN

bot = Draco()


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )


@bot.tree.command(
    name="setup",
    description="Post the Dragons Den application panel."
)
@discord.app_commands.default_permissions(administrator=True)
async def setup(interaction: discord.Interaction):

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
bot.run(TOKEN)