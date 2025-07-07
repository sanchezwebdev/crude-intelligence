import pandas as pd
from django.shortcuts import render
from django.db import connection
from plotly.offline import plot
import plotly.graph_objs as go

# ==============================
# Generate oil consumption heatmap
# ==============================
def consumption():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM oil_consumption_by_country_1965_to_2023")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    # Identify columns that represent years
    years = [col for col in df.columns if col.isdigit()]

    # Convert year columns to numeric values, handling missing or bad data
    df[years] = df[years].apply(pd.to_numeric, errors='coerce')

    # Select top 30 countries/entities by their 2023 consumption
    df_top = df.nlargest(30, "2023")  

    # Prepare data for heatmap
    z = df_top[years].values
    y = df_top["entity"].tolist()
    x = years

    # Create Plotly heatmap figure
    fig_heat = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y,
        colorscale="YlGnBu",
        colorbar=dict(title="Level"),
        zmin=0
    ))

    # Update layout with titles and styling
    fig_heat.update_layout(
        title={
            'text': "Consumption Heatmap By Country (1965–2023)",
            'y': 0.98,
        },
        xaxis_title="Year",
        yaxis_title="Entity",
        template="plotly_white",
        height=600,
        width=800,
    )

    consumption_heatmap = plot(fig_heat, output_type='div', config={"responsive": True})

    return consumption_heatmap
    