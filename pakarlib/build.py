import json
import os

from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def build_cities():
    print("Building cities...")
    LANGS = ["he", "ar", "en", "ru"]
    LANG_FIELDS = ["label", "mixname", "rashut"]

    d = defaultdict(dict)
    lds = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))  # defaultdicts all the way down!

    for lang in LANGS:
        with open(DATA_DIR / "cities"/ f"{lang}.json", "r") as f:
            cities = json.load(f)
            for city in cities:
                val = city["value"]
                for field in LANG_FIELDS:
                    lds[val][field][lang] = city.pop(field)
                d[val].update(city)
    
    # backfill all lang fields
    for k, v in lds.items():
        d[k].update(v)
        d[k].pop("label_he")  # remove the default label_he

    with open(DATA_DIR / "build"/ "cities.json", "w") as f:
        f.write(json.dumps(list(d.values())))

def build_districts():
    print("Building districts...")
    LANGS = ["he", "ar", "en", "ru"]
    LANG_FIELDS = ["label", "areaname"]

    d = defaultdict(dict)
    lds = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))  # defaultdicts all the way down!

    for lang in LANGS:
        with open(DATA_DIR / "districts"/ f"{lang}.json", "r") as f:
            districts = json.load(f)
            for district in districts:
                val = district["value"]
                for field in LANG_FIELDS:
                    lds[val][field][lang] = district.pop(field)
                d[val].update(district)
    
    # backfill all lang fields
    for k, v in lds.items():
        d[k].update(v)
        d[k].pop("label_he")  # remove the default label_he
    
    with open(DATA_DIR / "build"/ "districts.json", "w") as f:
        f.write(json.dumps(list(d.values())))

def build_geojson():
    with open(DATA_DIR / "segments" / "he.json", "r") as f:
        segments_he = json.load(f)["segments"]

    with open(DATA_DIR / "segments" / "en.json", "r") as f:
        segments_en = json.load(f)["segments"]

    res = {"type": "FeatureCollection", "features": []}

    for fn in os.listdir(DATA_DIR / "polygons"):
        with open(DATA_DIR / "polygons" / fn, "r") as f:
            j = json.load(f)
            try:
                sid = j["segmentId"]
                pgs = [[[b,a] for a,b in j["polygonPointList"][0]]]
                od = {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "properties": {
                            "id": sid,
                            "hebName": segments_he.get(sid, {}).get("name", ""),
                            "engName": segments_en.get(sid, {}).get("name", ""),
                            "seconds": int(segments_he.get(sid, {}).get("szSeconds", 0))
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": pgs
                        }
                    }]
                }
                # can save od here if we like

                ft = od["features"][0]
                ft["properties"]["type"] = "unified"
                res["features"].append(ft)
            except Exception:
                pass
    
    with open(DATA_DIR / "build" / "all.geojson", "w") as out:
        json.dump(res, out)

if __name__ == "__main__":
    build_cities()
    build_districts()
    build_geojson()
