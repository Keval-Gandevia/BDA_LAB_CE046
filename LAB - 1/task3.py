from msilib.schema import File
import mysql.connector as msql
from lxml.builder import E

conn = msql.connect(host='localhost', user='root',
                    database='BDA_LAB_1', password='')
cursor = conn.cursor()
cursor.execute("SELECT * FROM cricket_data")

outfile = open("CricketDataXML.xml", "w")
rows = cursor.fetchall()
outfile.write('<?xml version="1.0" ?>\n')
outfile.write("<CRICKETDATA>\n")
for row in rows:
    outfile.write("  <ROW>\n")
    outfile.write('    <Id>%s</Id>\n' % row[0])
    outfile.write('    <Name>%s</Name>\n' % row[1])
    outfile.write('    <Fifty>%s</Fifty>\n' % row[2])
    outfile.write('    <Century>%s</Century>\n' % row[3])
    outfile.write('  </ROW>\n')
outfile.write('</CRICKETDATA>\n')
outfile.close()
