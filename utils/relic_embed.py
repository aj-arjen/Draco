import discord
from pathlib import Path

IMAGE_PATH = Path("hero_database/relics/images")


def create_relic_embed(relic):
    """Create a Discord embed for a relic."""

    embed = discord.Embed(
        title=relic["name"],
        color=discord.Color.gold()
    )

    embed.add_field(
        name="🏰 Faction",
        value=relic["faction"],
        inline=True
    )

    embed.add_field(
        name="⭐ Rarity",
        value=relic["rarity"],
        inline=True
    )

    embed.add_field(
        name="🛡️ Type",
        value=relic["type"],
        inline=True
    )

    embed.add_field(
        name="⭐ Rating",
        value="⭐" * relic["rating"],
        inline=False
    )

    embed.add_field(
        name="💡 Why?",
        value=relic["why"],
        inline=False
    )

    embed.add_field(
        name="📖 Description",
        value=relic["description"],
        inline=False
    )

    image_file = IMAGE_PATH / f"{relic['id']}.png"

    file = None

    if image_file.exists():
        file = discord.File(image_file, filename=image_file.name)
        embed.set_thumbnail(url=f"attachment://{image_file.name}")

    return embed, file