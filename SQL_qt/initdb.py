import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime

metadata = MetaData()


user = "postgres"
password = "12345"


#Создаем базу данных posgresql
connection = psycopg2.connect(user=user, password=password, database=user, host="localhost", port=5432)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

sql_create_database = cursor.execute("CREATE DATABASE IF NOT EXISTS roman_learn")
cursor.close()
connection.close()

#Создаем енджин для создания таблиц и наполнения БД
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres")
engine.connect()



def random_int(start=1, end=100):
    a = random.randint(1, 100)
    return a


users_data  = [{'name':random_int(), 'soname':random_int(), 'age':random_int(), 'gender':random_int(),'wt':random_int()} for _ in range(100)]

cursor.execute("""CREATE TABLE IF NOT EXISTS projects (url TEXT, descr TEXT, income INTEGER)""")
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, soname TEXT, age INTEGER, gender TEXT, wt INTEGER)")
cursor.execute("INSERT INTO projects VALUES ('giraffes.io', 'Uber, but with giraffes', 1900),('dronesweaters.com', 'Clothes for cold drones', 3000),('hummingpro.io', 'Online humming courses', 120000)")

for user in users_data:
    cursor.execute("INSERT INTO users(name , soname , age , gender , wt ) VALUES (:name , :soname , :age , :gender , :wt )",user)

