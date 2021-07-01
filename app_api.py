from flask import Flask, jsonify, request, abort
from get_api_data import get_weather_yandex, get_coords_yandex
from manipulaate_db import check_insert_data, insert_to_db, get_data, all_data
from distance import get_distance

app_api = Flask(__name__)


@app_api.route("/api/v1/coordinate/city/create/<string:name_place>/", methods=['GET', 'POST'])
def create_city(name_place):
    if name_place:

        if request.method == 'GET':
            if check_insert_data(city=name_place):
                data = get_data(city=name_place)
                return jsonify({'coordinates_city': data}), 200
            else:
                abort(404)
        else:
            if not check_insert_data(city=name_place):
                record = get_coords_yandex(place=name_place)
                data = insert_to_db(record)
                return jsonify({'coordinates_city': data}), 201
            else:
                abort(404)
    else:
        return app_api.register_error_handler(404)


@app_api.route("/api/v1/distance/cities/<string:name_place1>/<string:name_place2>/", methods=['POST'])
# POST /api/v1/distance/cities/Minsk/Minsk/ HTTP/1.1" 200
# GET /api/v1/distance/cities/Minsk/Minsk/ HTTP/1.1" 405
def distance_city(name_place1, name_place2):
    if name_place1 and name_place2:
        distance = get_distance(name_place1, name_place2)
        return jsonify({'distance': distance}), 200
    else:
        return app_api.register_error_handler(404)


@app_api.route("/api/v1/weather/city/<string:name_place>/", methods=['GET'])
def weather_city(name_place):
    if name_place:
        weather = get_weather_yandex(name_place)
        return jsonify({'weather_city': weather}), 200
    else:
        return app_api.register_error_handler(404)


@app_api.route('/api/v1/')
def check_list_cities():
    list_cities = all_data()
    return jsonify({'all_data': list_cities})


if __name__ == '__main__':
    app_api.run()
