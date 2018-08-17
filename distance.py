from math import sin, cos, sqrt, atan2, radians

def travel_distance(location1_latitude, location1_longitude, location2_latitude, location2_longitude):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(location1_latitude)
    lon1 = radians(location1_longitude)
    lat2 = radians(location2_latitude)
    lon2 = radians(location2_longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
