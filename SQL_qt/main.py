from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import sys

if not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    sys.exit()

app = QApplication([])
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()

model = QSqlTableModel(None, db)
model.setTable("projects")
model.select()
view = QTableView()
view.setModel(model)

user_model = QSqlTableModel(None, db)
user_model.setTable("users")
user_model.select()
users_view = QTableView()
users_view.setModel(user_model)

# Основная форма окна с двумя вкладками
tab_widget = QTabWidget()
tab_widget.addTab(view, "Проекты")
tab_widget.addTab(users_view, "Пользователи")

window = QWidget()
layout = QVBoxLayout(window)
layout.addWidget(tab_widget)
window.setWindowTitle('Projects & Users')
window.resize(800, 600)
window.show()
app.exec()