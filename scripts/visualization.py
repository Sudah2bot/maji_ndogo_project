import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_visuals():
    print("--- GENERATING STRATEGIC VISUALS ---")

    # 1. Loading the processed data
    df = pd.read_csv("data/processed_water_data.csv")

    # Setting style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 7))

    # 2. Create the bar chart
    # We aggregate the data to show total people served per source type
    chart_data = (
        df.groupby("type_of_water_source")["number_of_people_served"]
        .sum()
        .reset_index()
    )
    chart_data = chart_data.sort_values("number_of_people_served", ascending=False)

    sns.barplot(
        data=chart_data,
        x="type_of_water_source",
        y="number_of_people_served",
        palette="viridis",
    )

    # 3. Formatting
    plt.title(
        "Maji Ndogo: Total Population Reliance by Water Source", fontsize=16, pad=20
    )
    plt.ylabel("Total People Served (Millions)", fontsize=12)
    plt.xlabel("Water Source Type", fontsize=12)
    plt.xticks(rotation=45)

    # Add a note about the 'Critical' status
    plt.text(
        0,
        -0.1,
        "* Note: 'River' and 'Broken Tap' represent high-risk drought zones.",
        transform=plt.gca().transAxes,
        color="red",
        fontsize=10,
    )

    # 4. Saving the output
    os.makedirs("output", exist_ok=True)
    output_path = "output/priority_chart.png"
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)  # High resolution for GitHub

    print(f"Success: Visual report saved to {output_path}")


if __name__ == "__main__":
    generate_visuals()
