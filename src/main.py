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


# data analysis
def analysis_part(df):
    subset = df[
        (df["country"] == country_asig)
        & (df["year"] == year_asig)
        & (df["sector"] == sector_asig)
    ]

    values = subset["value"].values

    mean = np.mean(values)
    std = np.std(values)

    print("\nPromedio:", mean)
    print("Desviación estándar:", std)

    max_idx = np.argmax(values)
    min_idx = np.argmin(values)

    max_row = subset.iloc[max_idx]
    min_row = subset.iloc[min_idx]

    print("\nMáximo:")
    print(max_row["date"], max_row["value"])

    print("\nMínimo:")
    print(min_row["date"], min_row["value"])

    low_days = subset[subset["value"] < (mean - std)]

    print("\nCantidad de días bajos:", len(low_days))
    print("Primeras 5 fechas:")
    print(low_days["date"].head())

    return subset, mean, std, max_row, min_row


# main
def main():
    df = load_and_clean()
    subset, mean, std, max_row, min_row = analysis_part(df)


if __name__ == "__main__":
    main()
