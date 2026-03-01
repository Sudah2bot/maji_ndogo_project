import os

import pandas as pd


def clean_water_data():
    print("--- DATA CLEANING & STANDARDIZATION ---")

    # Loading raw data
    input_path = "data/water_source.csv"
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Check your data/ folder!")
        return

    df = pd.read_csv(input_path)

    # removing invisible spaces and fixing case sensitivity
    df["type_of_water_source"] = df["type_of_water_source"].str.lower().str.strip()

    # Priority Status
    # we can add intelligence to the data.
    # High-risk sources for the drought are 'river' and 'tap_in_home_broken'
    def define_priority(source):
        if source in ["river", "tap_in_home_broken"]:
            return "CRITICAL"
        elif source == "well":
            return "HIGH (Requires Pollution Check)"
        else:
            return "STANDARD"

    df["priority_status"] = df["type_of_water_source"].apply(define_priority)

    # Saving the copy
    # never overwrite the original; we save a processed version.
    output_path = "data/processed_water_data.csv"
    df.to_csv(output_path, index=False)

    print(f"Success: {len(df):,} records standardized.")
    print("New Feature Created: 'priority_status'")
    print(f"Cleaned data saved to: {output_path}")


if __name__ == "__main__":
    clean_water_data()
