from django.shortcuts import render
from app.models import Data  
import plotly.graph_objects as go
from plotly.offline import plot
from django.db.models import Sum

def oil_trade_flows(request):
    colors = ["#e3f2fd","#bbdefb","#90caf9","#64b5f6","#42a5f5","#2196f3","#1e88e5","#1976d2","#1565c0","#0d47a1"]

    top_origins = (
        Data.objects
        .values('originname')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')[:100]
    )
    top_origin_names = [item['originname'] for item in top_origins]
   
    globe_records = Data.objects.filter(
        origin_lat__isnull=False,
        origin_lon__isnull=False,
        dest_lat__isnull=False,
        dest_lon__isnull=False,
        originname__in=top_origin_names,
        quantity__gt=1000
    ).exclude(originname="World")[:800]

    fig = go.Figure()

    unique_origins = list(dict.fromkeys(record.originname for record in globe_records))
    origin_colors = {origin: colors[i % len(colors)] for i, origin in enumerate(unique_origins)}

    for record in globe_records:
        fig.add_trace(go.Scattergeo(
            lon=[record.origin_lon, record.dest_lon],
            lat=[record.origin_lat, record.dest_lat],
            mode='lines',
            line=dict(width=1.5, color=origin_colors.get(record.originname, colors[0])),
            opacity=0.7,
            showlegend=False
        ))

    fig.update_geos(
        projection_type="orthographic",
        projection_rotation=dict(lon=-90, lat=20),
        showland=True,
        landcolor="#d2b48c",
        showocean=True,
        oceancolor="#a2cffe",
        showlakes=True,
        lakecolor="#80bfff",
        showcountries=True,
        countrycolor="#8b7765",
        coastlinecolor="#5f4b32",
        resolution=50
    )

    fig.update_layout(
        title="Global Oil Trade Flows (2024)",
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor="#f0f0f0",
        font=dict(color="#333333")
    )

    plot_html = plot(fig, output_type='div', include_plotlyjs=True)
    
    table_records = Data.objects.filter(
        origin_lat__isnull=False,
        origin_lon__isnull=False,
        dest_lat__isnull=False,
        dest_lon__isnull=False,
        quantity__gt=1000
    ).exclude(originname="World").order_by('-quantity')[:414]
   
    table_data = [
        {
            'origin': rec.originname,
            'destination': rec.destinationname,
            'quantity': rec.quantity,
        }
        for rec in table_records
    ]

    return render(request, 'oil_trade_flows.html', {
        'plot_html': plot_html,
        'table_data': table_data,
    })
