import json
from pathlib import Path


BASE_PATH = Path("hero_database/factions")

RARITIES = [
    "common",
    "rare",
    "epic",
    "legendary",
    "mythic"
]


def find_hero_file(hero_name: str) -> Path | None:
    """
    Find a hero JSON file by hero id.
    Example:
        adjudicator
        paragon
    """

    hero_name = hero_name.lower()

    for faction in BASE_PATH.iterdir():

        heroes_folder = faction / "heroes"

        if not heroes_folder.exists():
            continue

        for rarity in RARITIES:

            candidate = (
                heroes_folder /
                rarity /
                f"{hero_name}.json"
            )

            if candidate.exists():
                return candidate

    return None


def load_hero(hero_name: str) -> dict | None:
    """
    Load a hero JSON file.
    """

    hero_file = find_hero_file(hero_name)

    if hero_file is None:
        return None

    with open(hero_file, "r", encoding="utf-8") as f:
        return json.load(f)


def get_factions() -> list[str]:
    """
    Return all available factions.
    """

    factions = []

    for faction in BASE_PATH.iterdir():

        if faction.is_dir():
            factions.append(faction.name.title())

    factions.sort()

    return factions


def get_rarities(faction: str) -> list[str]:
    """
    Return all rarities for a faction.
    """

    heroes_folder = (
        BASE_PATH /
        faction.lower() /
        "heroes"
    )

    if not heroes_folder.exists():
        return []

    rarities = []

    for rarity in RARITIES:

        if (heroes_folder / rarity).exists():
            rarities.append(rarity.title())

    return rarities


def get_heroes(faction: str, rarity: str) -> list[str]:
    """
    Return all hero ids in a faction/rarity.
    """

    hero_folder = (
        BASE_PATH /
        faction.lower() /
        "heroes" /
        rarity.lower()
    )

    if not hero_folder.exists():
        return []

    heroes = []

    for file in hero_folder.glob("*.json"):
        heroes.append(file.stem)

    heroes.sort()

    return heroes