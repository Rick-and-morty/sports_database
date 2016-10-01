import psycopg2
import csv
link = psycopg2.connect("dbname=sport_database user=sport_database")

cursor = link.cursor()
cursor.execute("DROP TABLE IF EXISTS sport_database;")

create_table = """
CREATE TABLE sport_database (
    id serial PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(20),
    att int,
    rushyds int,
    rushavg int,
    rushTD int,
    rec int,
    recyds int,
    recavg int,
    recTD int,
    plays int,
    scrimyds int,
    scrimavg int,
    scrimTD int
);
"""

cursor.execute(create_table)

with open("sport_stats.csv") as open_file:
    stats = csv.reader(open_file)

    for row in stats:
        cursor.execute("insert into sport_database values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
            row[10], row[11]))


link.commit()
cursor.close()

link.close()
