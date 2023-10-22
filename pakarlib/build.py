import requests

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def get_cities():
    LANGS = ["he", "ar", "en", "ru"]
    BASE_URL = "https://www.oref.org.il/Shared/Ajax/GetCitiesMix.aspx"
    for lang in LANGS:
        print(f"Fetching {lang}...")
        res = requests.get(BASE_URL, params={"lang": lang})
        if "Access Denied" in res.text:
            print("Access denied, must run from Israeli IP")
            break
        with open(DATA_DIR / "cities"/ f"{lang}.json", "wb") as f:
            f.write(res.content)

if __name__ == "__main__":
    get_cities()
