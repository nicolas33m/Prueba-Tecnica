import pandas as pd
import psycopg2
from datetime import datetime

file_path = "c:/Users/fatte/OneDrive/Escritorio/Test/Anexo Prueba Punto 2.xlsx"
xls = pd.ExcelFile(file_path)
conn = psycopg2.connect(
    host="bubble.db.elephantsql.com",
    port="5432",
    user="cbadfzzz",
    password="1ZF4H-GzIdZQoUuKybfxaLWwE0Zv73mI",
    database="cbadfzzz"
)
cursor = conn.cursor()

for sheet_name in xls.sheet_names:
    fecha_str = sheet_name.split()[0] + "-" + sheet_name.split()[1]
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.fillna(0,inplace=True)

    for index, row in df.iterrows():
        cursor.execute('INSERT INTO "Anexo Prueba Punto 2" (Fecha, "Compañía", "Cliente", "Contrato", "Tipo Contrato", "CDGF(Mbtud)", "Precio(Usd/Mbtu", "Nominación(Mbtud)", "Entrega Boca de pozo", "Entrega SNT Capacidad Terceros", "Entrega SNT Capacidad propia") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (fecha_str, row['Compañía'], row['Cliente'], row['CONTRATO'], row['Tipo Contrato '], row['CDGF (Mbtud) '], row['Precio (Usd/Mbtu)'], row['Nominación (Mbtud)'], row['Entrega Boca de pozo'], row['Entrega SNT Capacidad Terceros'], row['Entrega SNT Capacidad Propia'],))

conn.commit()
conn.close()
