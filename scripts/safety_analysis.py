import pandas as pd


def run_deep_safety_analysis():
    print("---  ADVANCED SAFETY & SOURCE CORRELATION ---")

    # 1. Load tables
    sources = pd.read_csv("data/processed_water_data.csv")
    crimes = pd.read_csv("data/water_source_related_crime.csv")
    locations = pd.read_csv("data/location.csv")
    visits = pd.read_csv("data/visits.csv")

    # 2. Using left_on and right_on
    # crimes uses 'loc_id', locations uses 'location_id'
    crime_loc = pd.merge(crimes, locations, left_on="loc_id", right_on="location_id")

    # 3. Complete the Triple Join
    # merge with visits (using location_id) and then sources (using source_id)
    safety_map = pd.merge(
        crime_loc, visits[["location_id", "source_id"]], on="location_id"
    )
    final_analysis = pd.merge(safety_map, sources, on="source_id")

    # 4. The Insight
    source_danger_ranking = final_analysis["type_of_water_source"].value_counts()

    print("CRIME DISTRIBUTION BY WATER SOURCE TYPE:")
    print(source_danger_ranking)
    print("-" * 40)

    if not source_danger_ranking.empty:
        top_danger = source_danger_ranking.index[0].replace("_", " ").title()
        print(
            f"STRATEGIC ACTION: {top_danger} locations need immediate security patrols."
        )


if __name__ == "__main__":
    run_deep_safety_analysis()
