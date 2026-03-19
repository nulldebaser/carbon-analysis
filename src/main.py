# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# config
DATA_PATH = "../data/carbonmonitor-global_datas_2025-04-21.csv"

# seed and data assignment
seed = 811

countries = [
    "Brazil",
    "China",
    "EU27 & UK",
    "France",
    "Germany",
    "India",
    "Italy",
    "Japan",
    "ROW",
    "Russia",
    "Spain",
    "United Kingdom",
    "United States",
    "WORLD",
]

sectors = [
    "Domestic Aviation",
    "Ground Transport",
    "Industry",
    "International Aviation",
    "Power",
    "Residential",
]

years = [2019, 2020, 2021, 2022, 2023, 2024]

idx_country = seed % len(countries)
idx_sector = (seed // len(countries)) % len(sectors)
idx_year = (seed // (len(countries) * len(sectors))) % len(years)

country_asig = countries[idx_country]
sector_asig = sectors[idx_sector]
year_asig = years[idx_year]

print("Seed:", seed)
print("País asignado:", country_asig)
print("Sector asignado:", sector_asig)
print("Año asignado:", year_asig)


# reading and cleaning data
def load_and_clean():
    df = pd.read_csv(DATA_PATH)

    if "Unnamed: 4" in df.columns:
        df = df.drop(columns=["Unnamed: 4"])

    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    print("\nHEAD:")
    print(df.head())

    print("\nINFO:")
    print(df.info())

    print("\nDESCRIBE (value):")
    print(df["value"].describe())

    return df
