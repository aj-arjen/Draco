import discord
from pathlib import Path

IMAGE_PATH = Path("hero_database/castles/images")


def create_castle_embed(castle):
    """Create a Discord embed for a castle."""

    embed = discord.Embed(
        title=castle["name"],
        color=discord.Color.gold()
    )

    embed.add_field(
        name="🏰 Faction",
        value=castle["faction"],
        inline=True
    )

    embed.add_field(
        name="⭐ Rarity",
        value=castle["rarity"],
        inline=True
    )

    embed.add_field(
        name="🛡️ Type",
        value=castle["type"],
        inline=True
    )

    embed.add_field(
        name="⭐ Rating",
        value="⭐" * castle["rating"],
        inline=False
    )

    embed.add_field(
        name="💡 Why?",
        value=castle["why"],
        inline=False
    )

    embed.add_field(
        name="📖 Description",
        value=castle["description"],
        inline=False
    )

    image_file = IMAGE_PATH / f"{castle['id']}.png"

    file = None

    if image_file.exists():
        file = discord.File(image_file, filename=image_file.name)
        embed.set_thumbnail(url=f"attachment://{image_file.name}")

    return embed, file