import os

import pandas as pd


def run_advanced_audit():
    print("--- RELATIONAL DATA AUDIT ---")

    # List of files we expect to have in the data folder
    required_files = [
        "water_source.csv",
        "well_pollution.csv",
        "infrastructure_cost.csv",
        "location.csv",
        "visits.csv",
        "water_source_related_crime.csv",
    ]

    # 1. Physical File Check
    missing = [f for f in required_files if not os.path.exists(f"data/{f}")]
    if missing:
        print(f"Missing files: {missing}")
        return

    # 2. Load tables
    sources = pd.read_csv("data/water_source.csv")
    pollution = pd.read_csv("data/well_pollution.csv")
    visits = pd.read_csv("data/visits.csv")

    print(f"Total Water Sources Found: {len(sources):,}")
    print(f"Total Pollution Records: {len(pollution):,}")
    print(f"Total Visit Logs: {len(visits):,}")

    # 3. Relational Integrity Check
    # Check if all pollution records have a matching source
    orphan_pollution = pollution[~pollution["source_id"].isin(sources["source_id"])]

    if orphan_pollution.empty:
        print("Integrity Check: All pollution records match valid water sources.")
    else:
        print(
            f"Warning: Found {len(orphan_pollution)} pollution records with no matching source!"
        )

    # 4. Data Gap Analysis
    nulls = sources.isnull().sum().sum()
    if nulls == 0:
        print("Quality Check: No missing values (nulls) found in primary source table.")
    else:
        print(f"Warning: Found {nulls} missing data points in the source table.")


if __name__ == "__main__":
    run_advanced_audit()
