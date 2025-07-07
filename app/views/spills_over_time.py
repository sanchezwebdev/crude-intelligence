from django.shortcuts import render
from django.db import connection
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

def spills_over_time(request):
    # Compose SQL joining annual spill count and quantity
    sql = """
    SELECT 
    s1.year,
    s1."large_oil_spills_(>700_tonnes)" AS large_spills,
    s1."medium_oil_spills_(7_700_tonnes)" AS medium_spills,
    s2."quantity_of_oil_spilled" AS quantity_spilled
    FROM spills1_number_oil_spills s1
    LEFT JOIN spills2_quantity_oil_spills s2
    ON s1.year = s2.year
    ORDER BY s1.year
    """     
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    # Create DataFrame to handle both count and volume data together
    df = pd.DataFrame(rows, columns=['year', 'large_spills', 'medium_spills', 'quantity_spilled'])
    df.fillna(0, inplace=True)

    # Create figure with stacked bars (counts) and secondary axis line (quantity)
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=df['year'],
        y=df['large_spills'],
        name='Large Oil Spills (>700 tonnes)'
    ))

    fig.add_trace(go.Bar(
        x=df['year'],
        y=df['medium_spills'],
        name='Medium Oil Spills (7–700 tonnes)'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['quantity_spilled'],
        mode='lines+markers',
        name='Quantity of Oil Spilled (tonnes)',
        yaxis='y2'  # Assign to secondary Y-axis
    ))

    fig.update_layout(
        title='Oil Spills Overview Over Time',
        xaxis=dict(title='Year'),
        yaxis=dict(
            title='Number of Oil Spills',
            showgrid=False,
        ),
        yaxis2=dict(
            title='Quantity of Oil Spilled (tonnes)',
            overlaying='y',  # Overlays on first y-axis
            side='right',
            showgrid=False
        ),
        barmode='stack',  # Stacked bars for spill count
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=80, b=40),
        height=600,
        template='plotly_white'
    )

    chart_div = plot(fig, output_type='div', include_plotlyjs=True)

    # Render with Plotly chart embedded
    return render(request, 'spills_over_time.html', {'chart': chart_div})
