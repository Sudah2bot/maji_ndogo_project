import pandas as pd


def run_strategic_analysis():
    print("--- STRATEGIC ANALYSIS ENGINE ---")

    # 1. Load copy from cleaning and the Pollution data
    sources = pd.read_csv("data/processed_water_data.csv")
    pollution = pd.read_csv("data/well_pollution.csv")

    # 2. Relational Join
    # We only care about pollution for 'wells'
    wells = sources[sources["type_of_water_source"] == "well"]
    well_analysis = pd.merge(wells, pollution, on="source_id")

    # 3. Calculate Crisis Metrics
    total_pop = sources["number_of_people_served"].sum()

    # Contaminated Population
    contaminated_pop = well_analysis[well_analysis["results"] != "Clean"][
        "number_of_people_served"
    ].sum()

    # how much are rivers relied
    river_pop = sources[sources["type_of_water_source"] == "river"][
        "number_of_people_served"
    ].sum()

    print(f"Total Region Population: {total_pop:,}")
    print("-" * 30)
    print(f"Contaminated Well Users: {contaminated_pop:,}")
    print(f"High Drought Risk (reliance on rivers): {river_pop:,}")
    print("-" * 30)

    # 4. Actionable Insight
    pct_at_risk = ((contaminated_pop + river_pop) / total_pop) * 100
    print(
        f"STRATEGIC CONCLUSION: {pct_at_risk:.1f}% of the population requires immediate intervention."
    )


if __name__ == "__main__":
    run_strategic_analysis()
