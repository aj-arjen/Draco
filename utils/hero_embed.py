import discord


FACTION_COLORS = {
    "League": 0x3498DB,
    "Horde": 0xE74C3C,
    "Nature": 0x2ECC71,
}


POSITION_NAMES = {
    "front": "Frontline",
    "middle": "Midline",
    "back": "Backline",
}


def build_hero_embed(hero: dict):
    """
    Build a Discord embed and thumbnail for a hero.

    Returns:
        tuple(discord.Embed, discord.File)
    """

    color = FACTION_COLORS.get(
        hero["faction"],
        0xC49A3A
    )

    position = POSITION_NAMES.get(
        hero["position"].lower(),
        hero["position"]
    )

    image_path = (
        f"hero_database/factions/"
        f"{hero['faction'].lower()}/heroes/images/"
        f"{hero['id']}.png"
    )

    file = discord.File(
        image_path,
        filename=f"{hero['id']}.png"
    )

    filled = "⭐" * hero["investment"]["stars"]
    empty = "✩" * (5 - hero["investment"]["stars"])
    stars = filled + empty

    embed = discord.Embed(
        title=hero["name"],
        description=(
            f"**{hero['faction']} • {hero['rarity']}**\n"
            f"**{hero['class']} • {position}**\n\n"
            f"**Description**\n"
            f"{hero['description']}"
        ),
        color=color
    )

    embed.set_thumbnail(
        url=f"attachment://{hero['id']}.png"
    )

    embed.add_field(
        name="Recommended Gear",
        value=(
            f"**{hero['gear']['recommended'].replace('_', ' ').title()}**\n\n"
            f"{' → '.join(item.title() for item in hero['gear']['priority'])}"
        ),
        inline=False
    )

    embed.add_field(
        name="Investment",
        value=f"{stars} • {hero['investment']['rating']}",
        inline=False
    )

    return embed, file