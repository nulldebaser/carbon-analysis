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


# matrix 12 x 6
def build_matrix(df):
    A = np.zeros((12, 6))

    for m in range(1, 13):
        for j in range(len(sectors)):
            sector = sectors[j]

            filtered = df[
                (df["country"] == country_asig)
                & (df["year"] == year_asig)
                & (df["month"] == m)
                & (df["sector"] == sector)
            ]

            if len(filtered) > 0:
                A[m - 1, j] = np.mean(filtered["value"].values)
            else:
                A[m - 1, j] = 0

    print("\nMatriz A (12x6):")
    print(A)

    col_means = np.mean(A, axis=0)
    row_sums = np.sum(A, axis=1)

    max_sector_idx = np.argmax(col_means)
    max_month_idx = np.argmax(row_sums)

    print("\nSector con mayor promedio:", sectors[max_sector_idx])
    print("Mes con mayor total:", max_month_idx + 1)

    top3_idx = np.argsort(col_means)[-3:][::-1]

    print("\nTop 3 sectores:")
    for i in top3_idx:
        print(sectors[i], col_means[i])

    return A, col_means, row_sums


# graphs
def plot_all(subset, max_row, min_row, col_means, row_sums):
    plt.figure()
    plt.plot(subset["date"], subset["value"])
    plt.scatter(max_row["date"], max_row["value"])
    plt.scatter(min_row["date"], min_row["value"])
    plt.title("Serie temporal")
    plt.xlabel("Fecha")
    plt.ylabel("Value")
    plt.savefig("../outputs/figures/time_series.png")
    plt.close()

    plt.figure()
    plt.bar(sectors, col_means)
    plt.xticks(rotation=45)
    plt.title("Promedio anual por sector")
    plt.savefig("../outputs/figures/sector_bar.png")
    plt.close()

    plt.figure()
    plt.plot(range(1, 13), row_sums)
    plt.title("Total mensual")
    plt.xlabel("Mes")
    plt.ylabel("Total")
    plt.savefig("../outputs/figures/monthly_trend.png")
    plt.close()


# printing to results.txt
def save_results(mean, std, max_row, min_row, col_means, row_sums):
    with open(f"../outputs/results_seed_{seed}.txt", "w") as f:
        f.write("carbon-analysis — Resultados\n\n")

        f.write(f"Seed: {seed}\n")
        f.write(f"País asignado: {country_asig}\n")
        f.write(f"Sector asignado: {sector_asig}\n")
        f.write(f"Año asignado: {year_asig}\n\n")

        f.write(f"Promedio: {mean:.4f}\n")
        f.write(f"Desviación estándar: {std:.4f}\n\n")

        f.write(f"Máximo: {max_row['date']} -> {max_row['value']:.4f}\n")
        f.write(f"Mínimo: {min_row['date']} -> {min_row['value']:.4f}\n\n")

        f.write(f"Sector con mayor promedio: {sectors[np.argmax(col_means)]}\n")
        f.write(f"Mes con mayor total: {np.argmax(row_sums) + 1}\n")


# main
def main():
    df = load_and_clean()
    subset, mean, std, max_row, min_row = analysis_part(df)
    A, col_means, row_sums = build_matrix(df)
    plot_all(subset, max_row, min_row, col_means, row_sums)
    save_results(mean, std, max_row, min_row, col_means, row_sums)


if __name__ == "__main__":
    main()
