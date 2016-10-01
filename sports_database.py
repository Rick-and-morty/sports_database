import psycopg2

connection = psycopg2.connect("dbname=sport_database")

cursor = connection.cursor()

name = input("what is the first name you want to search for?").title()

name1 = input("last name ").title()

cursor.execute("SELECT * FROM sport_database WHERE first_name = %s AND last_name = %s;", (name, name1))

results = cursor.fetchall()

print(results)

cursor.close()

connection.close()
