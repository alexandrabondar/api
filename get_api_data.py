import requests


def get_coords_yandex(place):
    print(f'Get info from yandex api about city {place}')
    api_key = '554460af-543f-4ea4-ad52-9ff6b81d1d41'
    req = 'https://geocode-maps.yandex.ru/1.x/?format=json&apikey=' + api_key + '&geocode=' + place
    result = requests.get(req)
    found_city = result.json()['response']['GeoObjectCollection']['featureMember']
    try:
        most_relevant = found_city[0]
    except IndexError:
        print('Api with this city or street nothing to find, check your name of city')
    else:
        lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
        return place, lon, lat


def get_weather_yandex(place):
    print(f'Get info from yandex api about weather in {place}')
    api_key = '0a9a5a24-926c-45af-b3ca-5299817a0333'
    city, lon, lat = get_coords_yandex(place)
    url = 'https://api.weather.yandex.ru/v2/forecast?lat=' + lat + '&lon=' + lon
    headers = {'X-Yandex-API-Key': api_key}
    result = requests.get(url, headers=headers)
    avg_temp = result.json()['forecasts'][0]['parts']['day']['temp_avg']
    return avg_temp