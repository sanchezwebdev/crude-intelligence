from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_GET
def get_reserves_by_year(request):    
    # Define years of interest (1995–2021)
    years = [str(y) for y in range(1995, 2022)]

    with connection.cursor() as cursor:        
        # Retrieve top 5 countries by total reserves (from precomputed view)
        cursor.execute('SELECT country FROM vw_top25_oil_reserves ORDER BY total_reserves DESC, country LIMIT 5')
        countries = [row[0] for row in cursor.fetchall()]
        
        # Dynamically build SELECT columns for each year
        year_cols = ', '.join([f'"{y}"' for y in years])

        # Fetch reserves data per year for these top countries
        cursor.execute(f'''
            SELECT country, {year_cols}
            FROM vw_top25_oil_reserves
            WHERE country IN %s
        ''', [tuple(countries)])

        rows = cursor.fetchall()
    
    # Build a dictionary: { country: [yearly values...] }
    series = {row[0]: [float(v) if v is not None else 0.0 for v in row[1:]] for row in rows}

    # Return structured data for front-end visualization
    return JsonResponse({
        'years': years,
        'countries': countries,
        'series': series,
    })
