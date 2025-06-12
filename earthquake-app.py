import requests
from datetime import datetime

USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson"

def fetch_earthquake_data():
    try:
        response = requests.get(USGS_URL)
        response.raise_for_status()
        data = response.json()
        return data["features"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def display_earthquakes(earthquakes):
    if not earthquakes:
        print("No significant earthquakes in the last hour.")
        return

    print(f"{len(earthquakes)} significant earthquake(s) detected:\n")
    for eq in earthquakes:
        props = eq["properties"]
        place = props.get("place", "Unknown location")
        magnitude = props.get("mag", "N/A")
        time = datetime.utcfromtimestamp(props["time"] / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')
        url = props.get("url", "")
        print(f"Magnitude {magnitude} at {place} on {time}")
        print(f"More info: {url}\n")

if __name__ == "__main__":
    print("🔍 Checking for recent significant earthquakes...")
    earthquakes = fetch_earthquake_data()
    display_earthquakes(earthquakes)
