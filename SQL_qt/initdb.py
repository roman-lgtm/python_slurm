from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Text, DateTime, Boolean, ForeignKey,insert
from sqlalchemy.orm import Session,declarative_base
import random

metadata = MetaData()

#Создаем енджин для создания таблиц и наполнения БД
engine = create_engine("postgresql+psycopg2://postgres:12345@localhost/postgres")
engine.connect()
Base = declarative_base()
meta = MetaData()




class YaProject(Base):
    __tablename__ = 'YA_project'
    id = Column(Integer, primary_key=True)
    col1 = Column(Integer, nullable=False)
    col2 = Column(Integer, nullable=False)
    col3 = Column(Integer, nullable=False)
    col4 = Column(Integer, nullable=False)
    col5 = Column(Integer, nullable=False)

def fill_ya_projects(engine):
    session = Session(bind=engine)

    for i in range(100):
        values = random.sample(range(0, 99999), 5)
        session.add_all(
            [
                YaProject(
                    col1=values[0],
                    col2=values[1],
                    col3=values[2],
                    col4=values[3],
                    col5=values[4],
                )
                for i in range(5)
            ]
        )
        session.flush()
    session.commit()

def init_db():
    with engine.connect() as conn:
        meta.drop_all(engine)
        meta.create_all(engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fill_ya_projects(engine)



if __name__ == '__main__':
    init_db()



    # def random_int(start=1, end=100):
    #     a = random.randint(1, 100)
    #     return a



# metadata.create_all(engine)
#СТАРЫЙ ВАРИАНТ ЧЕРЕЗ SQL_LIGHT
# users_data  = [{'name':random_int(), 'soname':random_int(), 'age':random_int(), 'gender':random_int(),'wt':random_int()} for _ in range(100)]
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS projects (url TEXT, descr TEXT, income INTEGER)""")
# cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, soname TEXT, age INTEGER, gender TEXT, wt INTEGER)")
# cursor.execute("INSERT INTO projects VALUES ('giraffes.io', 'Uber, but with giraffes', 1900),('dronesweaters.com', 'Clothes for cold drones', 3000),('hummingpro.io', 'Online humming courses', 120000)")
#
# for user in users_data:
#     cursor.execute("INSERT INTO users(name , soname , age , gender , wt ) VALUES (:name , :soname , :age , :gender , :wt )",user)
