from django.db import connection

def get_signals_on_route(data) -> list :
    
    # Extract the polyline from the API response and decode it
    encoded_polyline = data['routes'][0]['overview_polyline']['points']
    distance = 0.0005

    query = f"""
        SELECT ST_Y(location), ST_X(location), ip_address
        FROM main_trafficsignals
        WHERE ST_DWithin(location, ST_LineFromEncodedPolyline('{encoded_polyline}'), {distance})
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        queryset = cursor.fetchall()

    return queryset