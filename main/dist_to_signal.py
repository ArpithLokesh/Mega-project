import polyline
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # Distance in km
    return d

def distance_along_route(poly, end_loc):
    points = polyline.decode(poly) # Decodes the polyline to get a list of latitude-longitude pairs

    # Find the two closest points on the polyline to the start and end locations
    start_index = 0
    end_index = min(range(len(points)), key=lambda i: haversine(end_loc[0], end_loc[1], points[i][0], points[i][1]))

    distance = 0
    for i in range(start_index, end_index):
        lat1, lon1 = points[i]
        lat2, lon2 = points[i+1]
        distance += haversine(lat1, lon1, lat2, lon2)
    
    return distance