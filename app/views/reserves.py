from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_GET
def get_reserves_by_year(request):    
    years = [str(y) for y in range(1995, 2022)]

    with connection.cursor() as cursor:        
        cursor.execute('SELECT country FROM vw_top25_oil_reserves ORDER BY total_reserves DESC, country LIMIT 5')
        countries = [row[0] for row in cursor.fetchall()]
        
        year_cols = ', '.join([f'"{y}"' for y in years])
        cursor.execute(f'''
            SELECT country, {year_cols}
            FROM vw_top25_oil_reserves
            WHERE country IN %s
        ''', [tuple(countries)])

        rows = cursor.fetchall()
    
    series = {row[0]: [float(v) if v is not None else 0.0 for v in row[1:]] for row in rows}

    return JsonResponse({
        'years': years,
        'countries': countries,
        'series': series,
    })