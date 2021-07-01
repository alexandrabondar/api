import psycopg2
dict_list_cities = {}


def connect_to_db():
    conn = psycopg2.connect(dbname='about_city', user='root',
                            password='root', host='localhost')
    return conn


def get_data(city):
    conn = connect_to_db()
    cursor = conn.cursor()
    place_query = '''select name_place, lon, lat from cityapp_city WHERE name_place=%s;'''
    city_variable = (city,)
    cursor.execute(place_query, city_variable)
    record = cursor.fetchone()
    print(f'Check the table with records. Record: {record}')
    cursor.close()
    conn.close()
    return record


def check_insert_data(city):
    record = get_data(city)
    if not record:
        return False
    else:
        return True


def insert_to_db(record_to_insert):
    conn = connect_to_db()
    cursor = conn.cursor()
    insert_query = "INSERT INTO cityapp_city (name_place, lon, lat) VALUES(%s, %s, %s);"
    cursor.execute(insert_query, record_to_insert)
    conn.commit()
    cursor.close()
    conn.close()


def all_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    all_query = '''select * from cityapp_city;'''
    cursor.execute(all_query)
    result = cursor.fetchall()
    dict_list_cities['data'] = result
    cursor.close()
    conn.close()
    return dict_list_cities
