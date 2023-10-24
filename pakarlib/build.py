import json

from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def build_cities():
    print("Building cities...")
    LANGS = ["he", "ar", "en", "ru"]
    LANG_FIELDS = ["label", "mixname", "rashut"]

    d = defaultdict(dict)

    for lang in LANGS:
        with open(DATA_DIR / "cities"/ f"{lang}.json", "r") as f:
            cities = json.load(f)
            for city in cities:
                for field in LANG_FIELDS:
                    city[f"{field}_{lang}"] = city.pop(field)
                d[city["value"]].update(city)
    
    with open(DATA_DIR / "build"/ "cities.json", "w") as f:
        f.write(json.dumps(list(d.values())))

def build_districts():
    print("Building districts...")
    LANGS = ["he", "ar", "en", "ru"]
    LANG_FIELDS = ["label", "areaname"]

    d = defaultdict(dict)

    for lang in LANGS:
        with open(DATA_DIR / "districts"/ f"{lang}.json", "r") as f:
            districts = json.load(f)
            for district in districts:
                for field in LANG_FIELDS:
                    district[f"{field}_{lang}"] = district.pop(field)
                d[district["value"]].update(district)
    
    with open(DATA_DIR / "build"/ "districts.json", "w") as f:
        f.write(json.dumps(list(d.values())))

if __name__ == "__main__":
    build_cities()
    build_districts()
