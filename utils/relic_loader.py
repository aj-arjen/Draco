import json
from pathlib import Path

# Pad naar de relic database
RELICS_PATH = Path("hero_database/relics")


def load_all_relics():
    """
    Load all relic JSON files.
    Returns a list of relic dictionaries.
    """

    relics = []

    if not RELICS_PATH.exists():
        return relics

    for file in sorted(RELICS_PATH.glob("*.json")):

        try:
            with open(file, "r", encoding="utf-8") as f:
                relics.append(json.load(f))

        except Exception as e:
            print(f"Error loading {file.name}: {e}")

    return relics


def load_relic(relic_id):
    """
    Load a single relic by its ID.
    Returns a relic dictionary or None.
    """

    file = RELICS_PATH / f"{relic_id}.json"

    if not file.exists():
        return None

    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        print(f"Error loading {file.name}: {e}")
        return None