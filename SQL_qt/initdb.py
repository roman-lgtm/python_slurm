import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Text, DateTime, Boolean, ForeignKey
from datetime import datetime
import random

metadata = MetaData()

#Создаем енджин для создания таблиц и наполнения БД
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres")
engine.connect()

projects_table = Table('projects', metadata,
Column('url', Text(), primary_key=True),
    Column('descr', Text(), nullable=False),
    Column('income', Integer,  nullable=False)
)

users_table = Table('users', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('post_title', String(200), nullable=False),
                    Column('post_slug', String(200), nullable=False),
                    Column('content', Text(), nullable=False),
                    Column('user_id', Integer(), ForeignKey("users.id"))
                    )



def random_int(start=1, end=100):
    a = random.randint(1, 100)
    return a
#
#
# users_data  = [{'name':random_int(), 'soname':random_int(), 'age':random_int(), 'gender':random_int(),'wt':random_int()} for _ in range(100)]
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS projects (url TEXT, descr TEXT, income INTEGER)""")
# cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, soname TEXT, age INTEGER, gender TEXT, wt INTEGER)")
# cursor.execute("INSERT INTO projects VALUES ('giraffes.io', 'Uber, but with giraffes', 1900),('dronesweaters.com', 'Clothes for cold drones', 3000),('hummingpro.io', 'Online humming courses', 120000)")
#
# for user in users_data:
#     cursor.execute("INSERT INTO users(name , soname , age , gender , wt ) VALUES (:name , :soname , :age , :gender , :wt )",user)

