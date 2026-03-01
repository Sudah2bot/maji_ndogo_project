import os

import pandas as pd

# The clean name we gave it during the 'cp' step
DATA_PATH = "data/water_source.csv"


def run_audit():
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found!")
        return

    # Load the data
    df = pd.read_csv(DATA_PATH)

    print("--- MAJI NDOGO: INITIAL AUDIT ---")
    print(f"Total rows: {len(df)}")

    print("\nWater Source Types:")
    # This matches the column name in your uploaded file
    print(df["type_of_water_source"].value_counts())

    print("\nTotal People Served by Source Type:")
    # This calculates which source type provides for the most people
    print(
        df.groupby("type_of_water_source")["number_of_people_served"]
        .sum()
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    run_audit()
