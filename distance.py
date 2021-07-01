import math
from manipulaate_db import check_insert_data, get_data, insert_to_db
from get_api_data import get_coords_yandex
EARTH_RADIUS = 6372795


def prepare_data(city):
    if check_insert_data(city):
        data = get_data(city)
        return data
    else:
        record_to_insert = get_coords_yandex(city)
        insert_to_db(record_to_insert)
        data = get_data(city)
        return data


def get_distance(city1, city2):
    data1 = prepare_data(city1)
    data2 = prepare_data(city2)
    city1, lon1, lat1 = data1
    city2, lon2, lat2 = data2

    lon1_rad = float(lon1) * math.pi / 180
    lon2_rad = float(lon2) * math.pi / 180
    lat1_rad = float(lat1) * math.pi / 180
    lat2_rad = float(lat2) * math.pi / 180

    cl1 = math.cos(lat1_rad)
    cl2 = math.cos(lat2_rad)
    sl1 = math.sin(lat1_rad)
    sl2 = math.sin(lat2_rad)
    delta = lon2_rad - lon1_rad
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    y = math.sqrt(math.pow(cl2 * sdelta, 2) + pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
    x = sl1 * sl2 + cl1 * cl2 * cdelta

    ad = math.atan2(y, x)
    dist = ad * EARTH_RADIUS
    dist = int(dist)
    print(
        f'\nFrom {city1} with coords({lon1}, {lat1}) \nto {city2} with coords({lon2}, {lat2}) \ndistance is {dist} meters or {dist / 1000} km')
    return dist