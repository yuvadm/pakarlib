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

def get_segments():
    BASE_URL = "https://dist.meser-hadash.org.il/smart-dist/services/anonymous/polygon/id/android"
    sess = requests.Session()
    
    for i in range(5000000, 5005000):
        res = sess.get(BASE_URL, params={"id": str(i), "instance": "1544803905", "locale": "iw_IL"})
        if "CDATA" in res.text:
            print(res.text)
            print(f"{i} - got CDATA error, skipping")
        else:
            with open(DATA_DIR / "segments" / f"{i}.json", "wb") as f:
                cont = res.content
                print(f"{i} - writing {len(cont)} bytes")
                f.write(cont)

if __name__ == "__main__":
    get_cities()
    get_segments()