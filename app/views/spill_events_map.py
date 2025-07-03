from django.shortcuts import render
import plotly.graph_objects as go
from plotly.offline import plot
from django.db import connection

def spill_events_map(request):    
    selected_year = request.GET.get('year')
    selected_pipeline = request.GET.get('pipeline_type')
    selected_liquid = request.GET.get('liquid_type')
    selected_cause = request.GET.get('cause_category')
    
    filters = []
    params = []
    
    if selected_year:
        filters.append("accident_year = %s")
        params.append(selected_year)
    else:
        selected_year = '2016'
        filters.append("accident_year = %s")
        params.append('2016')
    
    if selected_pipeline:
        filters.append("pipeline_type = %s")
        params.append(selected_pipeline)

    if selected_liquid:
        filters.append("liquid_type = %s")
        params.append(selected_liquid)

    if selected_cause:
        filters.append("cause_category = %s")
        params.append(selected_cause)

    where_clause = " AND ".join(filters)
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT accident_year FROM database WHERE accident_year <> 2017 ORDER BY accident_year DESC")
        year_options = [str(row[0]) for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT pipeline_type FROM database WHERE pipeline_type IS NOT NULL ORDER BY pipeline_type")
        pipeline_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT liquid_type FROM database WHERE liquid_type IS NOT NULL ORDER BY liquid_type")
        liquid_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT cause_category FROM database WHERE cause_category IS NOT NULL ORDER BY cause_category")
        cause_options = [row[0] for row in cursor.fetchall()]
    
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT 
                accident_latitude,
                accident_longitude,
                all_costs,
                accident_city,
                accident_state,
                accident_year,
                pipeline_type,
                liquid_type,
                cause_category
            FROM database 
            WHERE {where_clause}
                AND accident_latitude IS NOT NULL 
                AND accident_longitude IS NOT NULL 
                AND all_costs IS NOT NULL
                AND accident_city IS NOT NULL
                AND accident_state IS NOT NULL
                AND accident_year <> 2017
            ORDER BY all_costs DESC
        """, params)

        rows = cursor.fetchall()

    spill_data = []
    for row in rows:
        lat, lon, cost, city, state, year, pipeline_type, liquid_type, cause_category = row
        if cost > 0 and -90 <= lat <= 90 and -180 <= lon <= 180:
            spill_data.append({
                "lat": float(lat),
                "lon": float(lon),
                "cost": float(cost),
                "location": f"{city}, {state}",
                "year": year,
                "pipeline_type": pipeline_type,
                "liquid_type": liquid_type,
                "cause_category": cause_category,
                "cost": float(cost)
            })


    if not spill_data:
        return render(request, 'spills_cost_analysis.html', {
            'plot_html': f'<div>No spill data found for selected filters</div>',
            'table_data': [],
            'year_options': year_options,
            'pipeline_options': pipeline_options,
            'liquid_options': liquid_options,
            'cause_options': cause_options,
            'selected_year': selected_year,
            'selected_pipeline': selected_pipeline,
            'selected_liquid': selected_liquid,
            'selected_cause': selected_cause,
        })

    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[spill["lon"] for spill in spill_data],
        lat=[spill["lat"] for spill in spill_data],
        text=[f"{spill['location']}<br>Cost: ${spill['cost']:,.2f}<br>Year: {spill['year']}" for spill in spill_data],
        mode='markers',
        marker=dict(
            size=[max(8, min(50, spill["cost"] / 10000)) for spill in spill_data],
            color='#e5383b',
            opacity=0.8,
            sizemode='diameter',
            sizemin=8,
            line=dict(width=2, color='darkred')
        ),
        hovertemplate='<b>%{text}</b><extra></extra>'
    ))

    fig.update_geos(
        scope="usa",
        projection_type="albers usa",
        showland=True,
        landcolor="#f0f0f0",
        showlakes=True,
        lakecolor="#cce7ff",
        showocean=False,
        showcountries=False,
        showcoastlines=False,
        showframe=False,
        resolution=50
    )

    fig.update_layout(
        title=f"Oil Spill Cost Analysis - {selected_year} ({len(spill_data)} incidents)",
        title_font_size=20,
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor="#ffffff",
        font=dict(color="#333333"),
        showlegend=False
    )

    plot_html = plot(fig, output_type='div', include_plotlyjs=True)

    return render(request, 'spill_events_map.html', {
        'plot_html': plot_html,
        'table_data': spill_data,
        'year_options': year_options,
        'pipeline_options': pipeline_options,
        'liquid_options': liquid_options,
        'cause_options': cause_options,
        'selected_year': selected_year,
        'selected_pipeline': selected_pipeline,
        'selected_liquid': selected_liquid,
        'selected_cause': selected_cause,
    })