import pandas as pd
from django.db import connection
import plotly.express as px

def spills():    
    with connection.cursor() as cursor:
        # Query total unintentional oil release per state for 2010
        cursor.execute("""
            SELECT "accident_state", SUM("unintentional_release_(barrels)") AS total_spilled
            FROM database
            WHERE "accident_year" = 2010
            AND "accident_state" IS NOT NULL
            GROUP BY "accident_state"
        """)
        spill_rows = cursor.fetchall()
        df_spill = pd.DataFrame(spill_rows, columns=["state", "total_spilled"])
       
        # Fetch total pipeline miles per state for normalization
        cursor.execute("""
            SELECT state_code, pipeline_miles
            FROM pipeline_miles_per_state
        """)
        miles_rows = cursor.fetchall()
        df_miles = pd.DataFrame(miles_rows, columns=["state", "pipeline_miles"])
   
    # Merge spill data with miles data to enable per-mile normalization
    df = pd.merge(df_spill, df_miles, on="state")

    # Calculate spillage rate per pipeline mile
    df["spill_per_mile"] = df["total_spilled"] / df["pipeline_miles"]
    df["spill_per_mile"].fillna(0, inplace=True)
    
    # Create choropleth map of normalized spill rates
    fig = px.choropleth(
        df,
        locations="state",
        locationmode="USA-states",
        color="spill_per_mile",
        scope="usa",
        color_continuous_scale="Reds",
        labels={"spill_per_mile": "Spillage per Miles"},
        title="Pipeline Oil Spillage per Pipeline Mile by U.S. State (2010)",
    )
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

    chart_choropleth = fig.to_html(full_html=False)

    return chart_choropleth
