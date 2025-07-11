from collections import defaultdict
from django.db import connection
from plotly.offline import plot
import plotly.graph_objs as go
from .utils import standardize_date

def get_price_chart():

    # Fetch WTI data (from Yahoo Finance style source)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT date, close
            FROM all_fuels_data
            WHERE ticker = 'CL=F'
            ORDER BY date
        """)
        wti_data = cursor.fetchall()

     # Fetch Brent data
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT date, price
            FROM brentoilprices
            ORDER BY date
        """)
        brent_data = cursor.fetchall()

     # Fetch generic crude oil price data
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT date, price
            FROM crude_oil_price
            ORDER BY date
        """)
        crude_price_data = cursor.fetchall()

    # Combine price data from multiple sources into a unified structure by date
    combined = defaultdict(lambda: {'wti': None, 'brent': None, 'crude': None})

    # Fill combined dict with WTI data
    for raw_date, close_price in wti_data:
        date_obj = standardize_date(raw_date)
        combined[date_obj]['wti'] = close_price

    # Fill combined dict with Brent data
    for raw_date, price in brent_data:
        date_obj = standardize_date(raw_date)
        combined[date_obj]['brent'] = price

    # Fill combined dict with Crude data
    for raw_date, price in crude_price_data:
        date_obj = standardize_date(raw_date)
        combined[date_obj]['crude'] = price

 # Sort dates to ensure time series consistency
    sorted_dates = sorted(combined.keys())
    dates = [d.isoformat() for d in sorted_dates]
    wti_prices = [combined[d]['wti'] for d in sorted_dates]
    brent_prices = [combined[d]['brent'] for d in sorted_dates]
    crude_prices = [combined[d]['crude'] for d in sorted_dates]

    # Create Plotly figure with filled area lines for each price type
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=wti_prices, mode='lines', name='WTI',
                             fill='tozeroy', line=dict(color='blue'),
                             fillcolor='rgba(0, 0, 255, 0.4)'))
    fig.add_trace(go.Scatter(x=dates, y=brent_prices, mode='lines', name='Brent',
                             line=dict(color='orange'),
                             fillcolor='rgba(255, 165, 0, 0.2)'))
    fig.add_trace(go.Scatter(x=dates, y=crude_prices, mode='lines', name='Crude',
                             fill='tozeroy', line=dict(color='green'),
                             fillcolor='rgba(0, 128, 0, 0.2)'))

    fig.update_layout(
        title="Crude Oil Prices Over Time",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_white"
    )

    return plot(fig, output_type='div')
