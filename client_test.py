# open new terminal for test
import requests


# Only create in db
# {'coordinates_city': None}
res1 = requests.post('http://localhost:5000/api/v1/coordinate/city/create/Abaza')
if res1.ok:
    print(res1.json())


# {'coordinates_city': ['Abaza', '90.088581', '52.651662']}
res2 = requests.get('http://localhost:5000/api/v1/coordinate/city/create/Abaza')
if res2.ok:
    print(res2.json())


# {"distance":54071}
res3 = requests.get('http://localhost:5000/api/v1/distance/cities/Zhodino/Minsk')
if res3.ok:
    print(res3.json())


# {"weather_city":27}
res5 = requests.get('http://localhost:5000/api/v1/weather/city/Minsk')
if res5.ok:
    print(res5.json())


#{"all_data":{"data":
# [[1,"Minsk","27.561831","53.902284"],[2,"Moscow","37.622513","55.75322"],
# [3,"Brest","23.684568","52.094246"],[4,"Mogilev","30.330654","53.894548"],
# [6,"Grodno","23.829529","53.677839"],[7,"Gomel","31.014281","52.42416"],
# [8,"Vitebsk","30.202878","55.184217"],[9,"China","102.110187","32.278826"],
# [11,"Varshava","21.007139","52.23209"],[13,"Smolensk","32.045287","54.782635"],
# [16,"Zhodino","28.321572","54.09437"],[18,"Antaly","30.701668","36.885851"],
# [19,"Kaliningrad","20.510137","54.710162"],[20,"Piter","30.315877","59.939099"],
# [21,"Archangelsk","40.515762","64.539911"],[22, "Abaza", "90.088581", "52.651662"]]
# }}
res6 = requests.get('http://localhost:5000/api/v1')
if res6.ok:
    print(res6.json())