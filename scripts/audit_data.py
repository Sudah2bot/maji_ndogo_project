import os

import pandas as pd

# The clean name we gave it during the 'cp' step
DATA_PATH = "data/water_source.csv"


def run_audit():
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: {DATA_PATH} not found in the data/ folder!")
        return

    # Load the data
    df = pd.read_csv(DATA_PATH)

    print("  MAJI NDOGO: INITIAL DATA AUDIT  ")

    # 1. Basic Stats
    print(f"Total Records: {len(df):,}")

    # 2. Check for missing values
    null_counts = df.isnull().sum()
    print("\nMissing Values per Column:")
    print(null_counts)

    # 3. Water Source Distribution
    print("\nCounts by Water Source Type:")
    print(df["type_of_water_source"].value_counts())

    # 4. Impact Analysis
    print("\nTotal People Served by Source Type:")
    impact = (
        df.groupby("type_of_water_source")["number_of_people_served"]
        .sum()
        .sort_values(ascending=False)
    )
    print(impact.apply(lambda x: f"{x:,} people"))


if __name__ == "__main__":
    run_audit()
