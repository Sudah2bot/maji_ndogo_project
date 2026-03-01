import pandas as pd


def run_budget_calculator():
    print("--- INFRASTRUCTURE BUDGET CALCULATOR ---")

    # 1. Load the data
    sources = pd.read_csv("data/processed_water_data.csv")
    pollution = pd.read_csv("data/well_pollution.csv")
    costs = pd.read_csv("data/infrastructure_cost.csv")

    # Convert costs to a dictionary for easy lookup
    # creating a mapping for efficiency
    cost_map = dict(zip(costs["improvement"], costs["unit_cost_USD"]))

    # 2. Logic: Assign Costs based on Source Type and Quality
    # join sources with pollution to identify specific well needs
    well_data = pd.merge(
        sources[sources["type_of_water_source"] == "well"],
        pollution,
        on="source_id",
        how="left",
    )

    # Calculate Well Costs
    bio_wells = well_data[well_data["results"] == "Contaminated: Biological"].shape[0]
    chem_wells = well_data[well_data["results"] == "Contaminated: Chemical"].shape[0]

    well_cost = (bio_wells * cost_map["Install UV and RO filter"]) + (
        chem_wells * cost_map["Install RO filter"]
    )

    # Calculate River Costs (Drought Mitigation)
    river_sources = sources[sources["type_of_water_source"] == "river"].shape[0]
    river_cost = river_sources * cost_map["Drill well"]

    # Calculate Broken Tap Costs
    broken_taps = sources[
        sources["type_of_water_source"] == "tap_in_home_broken"
    ].shape[0]
    tap_cost = broken_taps * cost_map["Diagnose local infrastructure"]

    # 3. Final Summary
    total_budget = well_cost + river_cost + tap_cost

    print(f"WELL RESTORATION: ${well_cost:,}")
    print(f"RIVER CONVERSION (DROUGHT RELIEF): ${river_cost:,}")
    print(f"TAP REPAIRS: ${tap_cost:,}")
    print("-" * 40)
    print(f"TOTAL INVESTMENT REQUIRED: ${total_budget:,}")


if __name__ == "__main__":
    run_budget_calculator()
