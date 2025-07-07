import pandas as pd
from django.shortcuts import render
from django.db import connection
from plotly.offline import plot
import plotly.graph_objs as go

def trade_flow():    
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT originname, destinationname, SUM(quantity) as total_quantity
            FROM data
            WHERE quantity > 0 AND year = 2024
            GROUP BY originname, destinationname
            ORDER BY total_quantity DESC
            LIMIT 100
        """)
        rows = cursor.fetchall()

    sources = []
    targets = []
    values = []

    # Build source, target, value lists from query results
    for origin, destination, quantity in rows:
        if origin and destination:
            sources.append(origin)
            targets.append(destination)
            values.append(quantity)

    # Create unique label list and index maps for Sankey
    labels = list(set(sources + targets))
    source_indices = [labels.index(s) for s in sources]
    target_indices = [labels.index(t) for t in targets]

    # Define a color palette for the links; repeat if needed
    palette = [
        "rgba(31, 119, 180, 0.6)", "rgba(255, 127, 14, 0.6)", "rgba(44, 160, 44, 0.6)",
        "rgba(214, 39, 40, 0.6)", "rgba(148, 103, 189, 0.6)", "rgba(140, 86, 75, 0.6)",
        "rgba(227, 119, 194, 0.6)", "rgba(127, 127, 127, 0.6)", "rgba(188, 189, 34, 0.6)",
        "rgba(23, 190, 207, 0.6)"
    ]
    link_colors = [palette[i % len(palette)] for i in range(len(values))]

    # Construct Sankey diagram
    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color="blue"
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=values,
            color=link_colors
        )
    )])

    fig_sankey.update_layout(        
        title=dict(
            text="Oil Trade Flows Between Entities",
            x=0.12,  # Left-aligned title positioning
            xanchor='center'
        ),
        font_size=12,
        template="plotly_white",
        height=800,
        width=1600,        
    )

    chart_sankey = plot(fig_sankey, output_type='div')

    return chart_sankey
