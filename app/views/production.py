import pandas as pd
from django.db import connection
from plotly.offline import plot
import plotly.express as px

def production():
    # Query crude oil production data for 2021
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT country_name, value
            FROM oil_production_statistics
            WHERE year = 2021
            AND product = 'Crude oil'
        """)
        prod_results = cursor.fetchall()

    prod_df = pd.DataFrame(prod_results, columns=["country", "production"])

    # Query crude oil reserves data for 2021
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                "world_crude_oil_reserves_(billion)",
                "2021"
            FROM world_crude_oil_reserves_from_1995_to_2021
        """)
        reserves_results = cursor.fetchall()

    res_df = pd.DataFrame(reserves_results, columns=["country", "reserves"])
    res_df['reserves'] = pd.to_numeric(res_df['reserves'], errors='coerce')

    # Strip possible whitespace in country names to ensure merge accuracy
    prod_df['country'] = prod_df['country'].str.strip()
    res_df['country'] = res_df['country'].str.strip()

    # Merge production and reserves data to compute intensity metric
    merged_df = pd.merge(prod_df, res_df, on="country", how="left")
    merged_df["intensity"] = merged_df["production"] / merged_df["reserves"]

    # Calculate each country's share of total production
    total_production = prod_df["production"].sum()
    prod_df["share"] = prod_df["production"] / total_production

    # Separate major (≥1%) and minor (<1%) producers
    major_producers = prod_df[prod_df["share"] >= 0.01].copy()
    minor_producers = prod_df[prod_df["share"] < 0.01].copy()

    # Aggregate minor producers into a single "Other countries" row
    other_row = pd.DataFrame([{
        "country": "Other countries",
        "production": minor_producers["production"].sum()
    }])

    # Combine major producers with the "Other countries" row for final chart
    final_df = pd.concat([major_producers[["country", "production"]], other_row])

    # Create pie chart showing production share distribution
    fig_prod = px.pie(
        final_df,
        names="country",
        values="production",
        title="Oil Production Share by Country (2021)",
        template="plotly_white"
    )

    # Configure chart layout and interactivity
    fig_prod.update_layout(
        width=800,
        height=600,
        margin=dict(t=50, b=50, l=50, r=50),
        legend_itemclick=False,
        legend_itemdoubleclick=False
    )

    # Return chart as embeddable HTML div
    chart_production = plot(fig_prod, output_type="div")
    return chart_production
