import pandas as pd
from django.shortcuts import render
from django.db import connection
from plotly.offline import plot
import plotly.graph_objs as go
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# ========================
# Choropleth data endpoint
# ========================
@require_GET
def choropleth_data(request):
    metric = request.GET.get("metric", "spill_per_mile")
    cause_category = request.GET.get("cause_category", None)    
        
    with connection.cursor() as cursor:
        if metric == "cause_category" and cause_category:
            cursor.execute("""
                SELECT accident_state, COUNT(*) AS total_spills
                FROM database
                WHERE accident_year = 2010
                  AND accident_state IS NOT NULL
                GROUP BY accident_state
            """)
            total_spills_rows = cursor.fetchall()
            df_total = pd.DataFrame(total_spills_rows, columns=["state", "total_spills"])

            cursor.execute("""
                SELECT accident_state, COUNT(*) AS cause_spills
                FROM database
                WHERE accident_year = 2010
                  AND accident_state IS NOT NULL
                  AND cause_category = %s
                GROUP BY accident_state
            """, [cause_category])
            cause_spills_rows = cursor.fetchall()
            df_cause = pd.DataFrame(cause_spills_rows, columns=["state", "cause_spills"])

            df = pd.merge(df_total, df_cause, on="state", how="left")
            df["cause_spills"] = df["cause_spills"].fillna(0)

            df["value"] = df["cause_spills"] 
            data_json = df[["state", "value"]].to_dict(orient="records")

            return JsonResponse({"data": data_json})
        
        # Handle other metrics (total spilled, incidents per 1000 miles, spill per mile)
        else:
            cursor.execute("""
                SELECT accident_state, COUNT(*) AS total_spilled
                FROM database
                WHERE accident_year = 2010
                AND accident_state IS NOT NULL
                GROUP BY accident_state
            """)
            spill_rows = cursor.fetchall()
            df_spill = pd.DataFrame(spill_rows, columns=["state", "total_spilled"])
            
            cursor.execute("""
                SELECT state_code, pipeline_miles
                FROM pipeline_miles_per_state
            """)
            miles_rows = cursor.fetchall()
            df_miles = pd.DataFrame(miles_rows, columns=["state", "pipeline_miles"])

            cursor.execute("""
                SELECT accident_state, COUNT(*) AS total_incidents
                FROM database
                WHERE accident_year = 2010
                AND accident_state IS NOT NULL
                GROUP BY accident_state
            """)
            incident_rows = cursor.fetchall()
            df_incidents = pd.DataFrame(incident_rows, columns=["state", "total_incidents"])

            df = pd.merge(df_incidents, df_miles, on="state", how="inner")
            df = pd.merge(df, df_spill, on="state", how="left")  

            df["total_spilled"] = df["total_spilled"].fillna(0)
            df["spill_per_mile"] = df["total_spilled"] / df["pipeline_miles"]
            df["value_incidents_per_1000_miles"] = (df["total_incidents"] / df["pipeline_miles"]) * 1000

           
            if metric == "total_spilled":
                df["value"] = df["total_spilled"]
            elif metric == "incidents_per_1000_miles":
                df["value"] = df["value_incidents_per_1000_miles"]
            else: 
                df["value"] = df["spill_per_mile"]

            df["value"].fillna(0, inplace=True)
            df = df[["state", "value"]]
            data_json = df.to_dict(orient="records")

            return JsonResponse({"data": data_json})


# ========================
# Cause categories endpoint
# ========================        
@require_GET
def cause_categories(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT cause_category
            FROM (
            SELECT DISTINCT cause_category
            FROM database
            WHERE cause_category IS NOT NULL
            ) AS sub
            ORDER BY 
            CASE 
                WHEN cause_category = 'NATURAL FORCE DAMAGE' THEN 0
                WHEN cause_category > 'NATURAL FORCE DAMAGE' THEN 1
                ELSE 2
            END,
            cause_category DESC;
        """)
        rows = cursor.fetchall()        
        causes = [row[0] for row in rows]

    return JsonResponse({"causes": causes})

# ========================
# Fetch oil reserves data
# ========================
def fetch_reserve_data():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "world_crude_oil_reserves_from_1995_to_2021" WHERE "world_crude_oil_reserves_(billion)" = %s',['World'])
        row = cursor.fetchone()
        colnames = [desc[0] for desc in cursor.description]

    df = pd.DataFrame([row], columns=colnames)

    year_columns = [col for col in df.columns if col.isdigit()]
    df_years = df[year_columns].astype(float).T
    df_years.index.name = "Year"
    df_years.columns = ["World Reserves (Billion Barrels)"]
    df_years.reset_index(inplace=True)

    return df_years

# ========================
# Create reserves chart
# ========================
def crude_reserves_chart():
    df = fetch_reserve_data()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Year"],
        y=df["World Reserves (Billion Barrels)"],
        mode="lines",
        fill="tozeroy",
        name="World Crude Oil Reserves"
    ))

    fig.update_layout(
        title="World Crude Oil Reserves Over Time",
        xaxis_title="Year",
        yaxis_title="Billion Barrels",
        template="plotly_dark"
    )

    return plot(fig, output_type="div")        