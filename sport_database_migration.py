import psycopg2
import csv
link = psycopg2.connect("dbname=sports_database user=sports_database")
cursor = link.cursor()
cursor.execute("DROP TABLE IF EXISTS sports_fun")
create_table = """
CREATE TABLE sports_fun (
id serial PRIMARY KEY,
rushing,
full_name varchar(20),
att numeric(3),
yds numeric(4),
avg numeric(4),
TD numeric(3),
rec numeric(2),
yds numeric(4),
avg numeric(4),
td numeric(2),
plays numeric(3),
yds numeric(4),
avg numeric(4),
td numeric(3),
);
"""
cursor.execute(create_table)
with open("sport_data") as open_file:
    stats = csv.reader(open_file)
    for row in stats:
        cursor.execute("insert into sports_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s");",
        (row[0]row[1]row[2]row[3]row[4]row[5]row[6]row[7]row[8]row[9]row[10]row[11]row[12]row[13]))



link.commit()

cursor.close()

link.close()
