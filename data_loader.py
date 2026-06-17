import pandas as pd
import requests
import os

OWID_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
LOCAL_FILE = "owid-covid-data.csv"

def load_data():
    """Load and preprocess COVID-19 data."""
    
    # Download if not already present
    if not os.path.exists(LOCAL_FILE):
        print("Downloading COVID-19 data...")
        try:
            response = requests.get(OWID_URL, timeout=60)
            with open(LOCAL_FILE, "wb") as f:
                f.write(response.content)
            print("Download complete!")
        except Exception as e:
            print(f"Download failed: {e}")
            raise

    df = pd.read_csv(LOCAL_FILE)
    df["date"] = pd.to_datetime(df["date"])

    numeric_cols = [
        "new_cases", "new_deaths", "total_cases",
        "total_deaths", "people_vaccinated", "new_vaccinations"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    df = df.sort_values(["location", "date"])
    df["new_cases_smoothed"] = (
        df.groupby("location")["new_cases"]
        .transform(lambda x: x.rolling(7, min_periods=1).mean())
    )
    df["new_deaths_smoothed"] = (
        df.groupby("location")["new_deaths"]
        .transform(lambda x: x.rolling(7, min_periods=1).mean())
    )

    return df


def get_country_list(df):
    """Return sorted list of countries."""
    exclude = ["World", "High income", "Low income", "Europe", "Asia",
               "Africa", "North America", "South America", "Oceania"]
    countries = df[~df["location"].isin(exclude)]["location"].unique().tolist()
    return sorted(countries)