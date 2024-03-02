from math import asin, cos, sin, sqrt
#from haversine import haversine, Unit

class LatLon:
    def __init__(self, lat:float, lon:float) -> None:
        self.lat = lat
        self.lon = lon

class GeoUtil:
    '''
    @staticmethod
    def distance_haversine(fromLatLon:LatLon, toLatLon:LatLon) -> float:
        return haversine((fromLatLon.lat, fromLatLon.lon), (toLatLon.lat, toLatLon.lon), unit = Unit.METERS)
    '''
    
    @staticmethod
    def distance(fromLatLon:LatLon, toLatLon:LatLon) -> float:
        earth_radius = 6370.996 * 1000
        pi_radius = 3.1415926 / 180.0
        
        radFromLat = fromLatLon.lat * pi_radius
        radFromLon = fromLatLon.lon * pi_radius
        radToLat = toLatLon.lat * pi_radius
        radToLon = toLatLon.lon * pi_radius
        
        diffLat = radFromLat - radToLat
        diffLon = radFromLon - radToLon
        
        distance = 2 * asin(sqrt(pow(sin(diffLat / 2), 2) + cos(radFromLat) * cos(radToLat) * pow(sin(diffLon / 2), 2)))
        distance = distance * earth_radius
        return round(distance,8)