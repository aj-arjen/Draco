import json
from pathlib import Path

# Pad naar de castle database
CASTLES_PATH = Path("hero_database/castles")


def load_all_castles():
    """
    Load all castle JSON files.
    Returns a list of castle dictionaries.
    """

    castles = []

    if not CASTLES_PATH.exists():
        return castles

    for file in sorted(CASTLES_PATH.glob("*.json")):

        try:
            with open(file, "r", encoding="utf-8") as f:
                castles.append(json.load(f))

        except Exception as e:
            print(f"Error loading {file.name}: {e}")

    return castles


def load_castle(castle_id):
    """
    Load a single castle by its ID.
    Returns a castle dictionary or None.
    """

    file = CASTLES_PATH / f"{castle_id}.json"

    if not file.exists():
        return None

    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        print(f"Error loading {file.name}: {e}")
        return None