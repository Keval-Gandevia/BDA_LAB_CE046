import json
import collections
import mysql.connector as msql

conn = msql.connect(host='localhost', user='root',
                    database='BDA_LAB_1', password='')
cursor = conn.cursor()
cursor.execute("SELECT * FROM cricket_data")
rows = cursor.fetchall()

objects_list = []

for row in rows:
    d = collections.OrderedDict()
    d["Id"] = row[0]
    d["Name"] = row[1]
    d["Fifty"] = row[2]
    d["Century"] = row[3]
    objects_list.append(d)

j = json.dumps(objects_list)

with open("CricketDataJSON.json", "w") as f:
    f.write(j)
