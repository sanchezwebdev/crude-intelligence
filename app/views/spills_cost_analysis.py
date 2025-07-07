from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.utils.formats import localize

COST_FIELDS = [
    'property_damage_costs',
    'lost_commodity_costs',
    'public/private_property_damage_costs',
    'emergency_response_costs',
    'environmental_remediation_costs',
    'other_costs',
    'all_costs'
]

def spills_cost_analysis(request):
    # Get filter values from GET params
    selected_year = request.GET.get('year')
    selected_pipeline = request.GET.get('pipeline_type')
    selected_liquid = request.GET.get('liquid_type')
    selected_state = request.GET.get('accident_state')
    selected_cause = request.GET.get('cause_category')
    selected_location = request.GET.get('pipeline_location')

    # Default to 'all_costs' if no cost field selected
    selected_cost_fields = request.GET.getlist('cost_fields') or ['all_costs']

    filters = []
    params = []

    # Dynamically build WHERE conditions and parameter list
    if selected_year:
        filters.append("accident_year = %s")
        params.append(selected_year)
    if selected_pipeline:
        filters.append("pipeline_type = %s")
        params.append(selected_pipeline)
    if selected_liquid:
        filters.append("liquid_type = %s")
        params.append(selected_liquid)
    if selected_state:
        filters.append("accident_state = %s")
        params.append(selected_state)
    if selected_cause:
        filters.append("cause_category = %s")
        params.append(selected_cause)
    if selected_location:
        filters.append("pipeline_location = %s")
        params.append(selected_location)

    where_clause = " AND ".join(filters) if filters else "1=1"

    # Explicitly quote field names for SQL safety
    quoted_cost_fields = [f'"{field}"' for field in COST_FIELDS]

    # Fetch filtered spill records including all cost fields
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT 
                accident_year, pipeline_location, pipeline_type, liquid_type,
                accident_state, cause_category, accident_city, accident_state,
                {', '.join(quoted_cost_fields)}
            FROM database
            WHERE {where_clause} AND accident_city IS NOT NULL AND accident_year <> 2017
            ORDER BY accident_year DESC
        """, params)

        rows = cursor.fetchall()

    table_data = []
    total_cost = 0.0

    # Iterate over results, calculate combined cost sum per record
    for row in rows:
        record = dict(zip([
            'accident_year', 'pipeline_location', 'pipeline_type', 'liquid_type',
            'accident_state', 'cause_category', 'accident_city', 'accident_state'
        ] + COST_FIELDS, row))

        included_cost = sum(record[field] or 0 for field in selected_cost_fields)
        record['calculated_cost'] = included_cost
        total_cost += included_cost
        table_data.append(record)

    # Return JSON payload for AJAX requests
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            'table_data': [
                {
                    'accident_year': row['accident_year'],
                    'pipeline_location': row['pipeline_location'],
                    'pipeline_type': row['pipeline_type'],
                    'liquid_type': row['liquid_type'],
                    'accident_state': row['accident_state'],
                    'cause_category': row['cause_category'],
                    'location': row['accident_city'],
                    'calculated_cost': round(row['calculated_cost']),
                }
                for row in table_data
            ],
            'total_cost': round(total_cost)
        })

    # Build dropdown/filter option lists
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT accident_year FROM database WHERE accident_year <> 2017 ORDER BY accident_year DESC")
        year_options = [str(row[0]) for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT pipeline_type FROM database WHERE pipeline_type IS NOT NULL AND accident_year <> 2017 ORDER BY pipeline_type")
        pipeline_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT liquid_type FROM database WHERE liquid_type IS NOT NULL AND accident_year <> 2017 ORDER BY liquid_type")
        liquid_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT accident_state FROM database WHERE accident_state IS NOT NULL AND accident_year <> 2017 ORDER BY accident_state")
        state_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT cause_category FROM database WHERE cause_category IS NOT NULL AND accident_year <> 2017 ORDER BY cause_category")
        cause_options = [row[0] for row in cursor.fetchall()]

        cursor.execute("SELECT DISTINCT pipeline_location FROM database WHERE pipeline_location IS NOT NULL AND accident_year <> 2017 ORDER BY pipeline_location")
        location_options = [row[0] for row in cursor.fetchall()]

    # Labels for each cost field
    cost_field_labels = {
        "property_damage_costs": "Property Damage",
        "lost_commodity_costs": "Lost Commodity",
        "public/private_property_damage_costs": "Public/Private Damage",
        "emergency_response_costs": "Emergency Response",
        "environmental_remediation_costs": "Environmental Remediation",
        "other_costs": "Other Costs",
        "all_costs": "All Costs"
    }

    cost_field_options = []
    for field in COST_FIELDS:
        cost_field_options.append({
            "field": field,
            "label": cost_field_labels.get(field, field.replace('_', ' ').title()),
            "checked": field in selected_cost_fields,
        })

    # Render template with computed data and filter context
    return render(request, 'spills_cost_analysis.html', {
        'table_data': table_data,
        'total_cost': total_cost,
        'year_options': year_options,
        'pipeline_options': pipeline_options,
        'liquid_options': liquid_options,
        'state_options': state_options,
        'cause_options': cause_options,
        'location_options': location_options,
        'selected_year': selected_year,
        'selected_pipeline': selected_pipeline,
        'selected_liquid': selected_liquid,
        'selected_state': selected_state,
        'selected_cause': selected_cause,
        'selected_location': selected_location,
        'cost_fields': COST_FIELDS,
        'selected_cost_fields': selected_cost_fields,
        'cost_field_options': cost_field_options
    })
