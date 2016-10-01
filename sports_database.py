import psycopg2
connection = psycopg2.connect("dbname=sport_database user=sports_data")

cursor = connection.cursor()

name = input("what is the first name you want to search for?")

password = input("Password? ")

cursor.execute("SELECT * FROM person_data WHERE first_name = %s AND last_name = %s;" (name, password))

results = cursor.fetchall()

print(results)



cursor.close()
connection.close()
