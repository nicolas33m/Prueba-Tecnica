import requests
import psycopg2
db_config = {
    "host": "bubble.db.elephantsql.com",
    "port": "5432",
    "user": "cbadfzzz",
    "password": "1ZF4H-GzIdZQoUuKybfxaLWwE0Zv73mI",
    "database": "cbadfzzz"
}

api_url = "http://servapibi.xm.com.co/daily"

params = {
    "MetricId": "VoluUtilDiarEner",
    "StartDate": "2023-11-01",
    "EndDate": "2023-11-23",
    "Entity": "Embalse"
}

response = requests.post(api_url, json=params)
data = response.json()

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

if data:
    for item in data["Items"]:
        date = item["Date"]

        for daily_entity in item["DailyEntities"]:
            entity_id = daily_entity["Id"]
            entity_name = daily_entity["Name"]
            value = daily_entity["Value"]

            cursor.execute('INSERT INTO "Hidrologia"("Id", "Name", "Date", "Value") VALUES (%s, %s, %s, %s);',
                           (entity_id, entity_name, date, value))
            conn.commit()

conn.close()

