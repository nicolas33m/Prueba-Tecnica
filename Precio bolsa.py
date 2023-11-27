import requests
import psycopg2
db_config = {
    "host": "bubble.db.elephantsql.com",
    "port": "5432",
    "user": "cbadfzzz",
    "password": "1ZF4H-GzIdZQoUuKybfxaLWwE0Zv73mI",
    "database": "cbadfzzz"
}

api_url = "http://servapibi.xm.com.co/hourly"

params = {
    "MetricId":"PrecBolsNaci",
    "StartDate":"2023-11-01",
    "EndDate":"2023-11-23",
    "Entity":"Sistema"}

response = requests.post(api_url, json=params)
data = response.json()

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

if data:
    for item in data["Items"]:
        date = item["Date"]

        for hourly_entity in item["HourlyEntities"]:
            entity_id = hourly_entity["Id"]
            values = hourly_entity["Values"]

            cursor.execute('INSERT INTO "Precio Bolsa"("id", "Fecha", "Hora1", "Hora2","Hora3","Hora4","Hora5","Hora6","Hora7","Hora8","Hora9","Hora10","Hora11","Hora12","Hora13","Hora14","Hora15","Hora16","Hora17","Hora18","Hora19","Hora20","Hora21","Hora22","Hora23","Hora24") VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s);',
                           (entity_id, date, values["Hour01"],values["Hour02"],values["Hour03"],values["Hour04"],values["Hour05"],values["Hour06"],values["Hour07"],values["Hour08"],values["Hour09"],values["Hour10"],values["Hour11"],values["Hour12"],values["Hour13"],values["Hour14"],values["Hour15"],values["Hour16"],values["Hour17"],values["Hour18"],values["Hour19"],values["Hour20"],values["Hour21"],values["Hour22"],values["Hour23"],values["Hour24"]))
            conn.commit()

conn.close()

