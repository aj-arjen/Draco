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

    # -----------------------------
    # Recommended Gear
    # -----------------------------

    recommended = hero["gear"]["recommended"]

    recommended_stage = " • ".join(recommended["stage"])

    gear_text = (
        f"**{recommended['set'].replace('_', ' ').title()}**\n\n"
        f"**Stage**\n"
        f"{recommended_stage}\n\n"
        f"**Why?**\n"
        f"{recommended['why']}\n\n"
    )

    # -----------------------------
    # Alternative Gear
    # -----------------------------

    alternative = hero["gear"]["alternative"]

    if alternative is None:

        gear_text += (
            "**Alternative**\n"
            "None\n\n"
        )

    else:

        alternative_stage = " • ".join(alternative["stage"])

        gear_text += (
            "**Alternative**\n"
            f"**{alternative['set'].replace('_', ' ').title()}**\n\n"
            f"**Stage**\n"
            f"{alternative_stage}\n\n"
            f"**Why?**\n"
            f"{alternative['why']}\n\n"
        )

    gear_text += (
        "**Priority**\n"
        + " → ".join(item.title() for item in hero["gear"]["priority"])
    )

    embed.add_field(
        name="Gear",
        value=gear_text,
        inline=False
    )

    investment = hero["investment"]

    investment_text = (
        f"{stars} • {investment['rating']}"
    )

    if "why" in investment:
        investment_text += (
            f"\n\n**Why?**\n"
            f"{investment['why']}"
        )

    embed.add_field(
        name="Investment",
        value=investment_text,
        inline=False
    )

    return embed, file