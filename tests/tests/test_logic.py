import os

import pandas as pd


def test_processed_file_exists():
    assert os.path.exists("data/processed_water_data.csv"), (
        "The cleaning script failed to produce the copy!"
    )


def test_budget_non_negative():
    costs = pd.read_csv("data/infrastructure_cost.csv")
    assert (costs["unit_cost_KSH"] >= 0).all(), (
        "Found a negative cost! The budget engine will be corrupted."
    )


def test_location_integrity():
    crimes = pd.read_csv("data/water_source_related_crime.csv")
    locations = pd.read_csv("data/location.csv")

    orphans = crimes[~crimes["loc_id"].isin(locations["location_id"])]
    assert orphans.empty, (
        f"Found {len(orphans)} crimes linked to locations that don't exist!"
    )
