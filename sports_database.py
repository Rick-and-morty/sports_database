import psycopg2

connection = psycopg2.connect("dbname=sport_database")

cursor = connection.cursor()

name = input("what is the first name you want to search for?").title()

name1 = input("last name ").title()

cursor.execute("SELECT * FROM sport_database WHERE first_name = %s AND last_name = %s;", (name, name1))

results = cursor.fetchall()
print(results)

def add_player():
    #if choice == "add":
    id_num = 21
    first_name = input("enter first name: ").title()
    last_name = input("enter last name: ").title()
    att = input("enter attempts: ")
    rushyds = input("enter yards rushing: ")
    rushavg = input("enter average rush yards: ")
    rushTD = input("enter rushing TD's: ")
    rec = input("enter recieving: ")
    recyds = input("enter receiving yards: ")
    recavg = input("enter receiving: ")
    recTD = input("enter receiving TD's: ")
    plays = input("enter plays made: ")
    scrimyds = input("enter scrimmage yards: ")
    scrimavg = input("enter scrimmaging avg yards: ")
    scrimTD = input("enter scrimmage TD's: ")

    cursor.execute("""INSERT INTO sport_database (id, first_name, last_name, att, rushyds,
        rushavg, rushTD, rec, recyds, recavg, recTD, plays, scrimyds, scrimavg, scrimTD)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (id_num, first_name, last_name, att, rushyds, rushavg, rushTD, rec, recyds,
        recavg, recTD, plays, scrimyds, scrimavg, scrimTD))
    
    connection.commit()


add_player()
cursor.close()

connection.close()
