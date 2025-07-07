import pandas as pd
from django.shortcuts import render
from django.db import connection
from .price_chart import get_price_chart
from .production import production
from .consumption import consumption
from .trade_flows import trade_flow
from .spills_choropleth import spills

# ====================================
# Home view: aggregates all main charts
# ====================================

def home(request):

    # Generate individual charts and visual components
    chart_prices = get_price_chart()
    chart_production = production()
    consumption_heatmap = consumption()
    chart_sankey = trade_flow()
    chart_choropleth = spills()

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vw_top25_oil_reserves')
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

    df_reserves = pd.DataFrame(rows, columns=columns)

    # Sort year columns in descending order (latest year first)
    years_only = [col for col in columns if col not in ('country', 'total_reserves')]

    # Order countries by total reserves descending
    country_order = df_reserves.sort_values('total_reserves', ascending=False)['country'].tolist()

    # Sort year columns in descending order (latest year first)
    years_only_sorted_desc = sorted(years_only, key=int, reverse=True)

     # Create a list of year options for dropdown or display, including "total_reserves" as default
    years = ['total_reserves'] + years_only_sorted_desc

    context = {
        'chart_prices': chart_prices,
        'chart_production': chart_production,
        'consumption_heatmap': consumption_heatmap,
        'chart_sankey': chart_sankey,
        "chart_choropleth": chart_choropleth,        
        'years': years,
        'default_year': 'total_reserves',
        'country_order': country_order
    }

    return render(request, 'index.html', context)