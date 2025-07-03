from django.shortcuts import render
from django.db import connection
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.offline import plot

def spills_over_time(request):
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

    df = pd.DataFrame(rows, columns=['year', 'large_spills', 'medium_spills', 'quantity_spilled'])
    
    df.fillna(0, inplace=True)

    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=df['year'],
        y=df['large_spills'],
        name='Large Oil Spills (>700 tonnes)'
    ))

    fig.add_trace(go.Bar(
        x=df['year'],
        y=df['medium_spills'],
        name='Medium Oil Spills (7-700 tonnes)'
    ))
    
    fig.add_trace(go.Scatter(
        x=df['year'],
        y=df['quantity_spilled'],
        mode='lines+markers',
        name='Quantity of Oil Spilled (tonnes)',
        yaxis='y2'
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
            overlaying='y',
            side='right',
            showgrid=False
        ),
        barmode='stack',
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=40, r=40, t=80, b=40),
        height=600,
        template='plotly_white'
    )

    chart_div = plot(fig, output_type='div', include_plotlyjs=True)

    return render(request, 'spills_over_time.html', {'chart': chart_div})
