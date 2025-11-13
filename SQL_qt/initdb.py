import sqlite3
import random

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

def random_int(start=1, end=100):
    a = random.randint(1, 100)
    return a


users_data  = [{'name':random_int(), 'soname':random_int(), 'age':random_int(), 'gender':random_int(),'wt':random_int()} for _ in range(100)]

cursor.execute("""CREATE TABLE IF NOT EXISTS projects (url TEXT, descr TEXT, income INTEGER)""")
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, soname TEXT, age INTEGER, gender TEXT, wt INTEGER)")
cursor.execute("INSERT INTO projects VALUES ('giraffes.io', 'Uber, but with giraffes', 1900),('dronesweaters.com', 'Clothes for cold drones', 3000),('hummingpro.io', 'Online humming courses', 120000)")

for user in users_data:
    cursor.execute("INSERT INTO users(name , soname , age , gender , wt ) VALUES (:name , :soname , :age , :gender , :wt )",user)

connection.commit()