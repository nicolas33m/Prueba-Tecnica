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
   "MetricId": "DemaOR",
    "StartDate": "2023-11-01",
    "EndDate": "2023-11-23",
    "Entity": "Agente"}

response = requests.post(api_url, json=params)
data = response.json()

conn = psycopg2.connect(**db_config)
cursor = conn.cursor()

if data:
    for item in data["Items"]:
        date = item["Date"]
    
        for hourly_entity in item["HourlyEntities"]:
            entity_id = hourly_entity["Id"]
            code = hourly_entity["Values"]["code"]
            values = hourly_entity["Values"]

            cursor.execute('INSERT INTO "Demanda por OR"("id", "Fecha","code", "hora1", "hora2","hora3","hora4","hora5","hora6","hora7","hora8","hora9","hora10","hora11","hora12","hora13","hora14","hora15","hora16","hora17","hora18","hora19","hora20","hora21","hora22","hora23","hora24") VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s);',
                           (entity_id, date, code, values.get("Hour01") or None, values.get("Hour02") or None, values.get("Hour03") or None, values.get("Hour04") or None, values.get("Hour05") or None, values.get("Hour06") or None, values.get("Hour07") or None, values.get("Hour08") or None, values.get("Hour09") or None, values.get("Hour10") or None, values.get("Hour11") or None, values.get("Hour12") or None, values.get("Hour13") or None, values.get("Hour14") or None, values.get("Hour15") or None, values.get("Hour16") or None, values.get("Hour17") or None, values.get("Hour18") or None, values.get("Hour19") or None, values.get("Hour20") or None, values.get("Hour21") or None, values.get("Hour22") or None, values.get("Hour23") or None, values.get("Hour24") or None))
            conn.commit()

conn.close()