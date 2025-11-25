from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sqlalchemy.orm import Session,declarative_base
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Text, DateTime, Boolean, ForeignKey, \
    insert, values
from initdb import engine,YaProject

projects = []
with engine.connect() as conn:
    session = Session(bind=conn)
    projects = list(session.query(YaProject).all())
shema = {0: "col1", 1: "col2", 2: "col3", 3: "col4", 4: "col5"}

class TableModel(QAbstractTableModel):
    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable

    def setData(self, index, value, role):
        if role != Qt.EditRole:
            return False
        field_name = shema[index.column()]
        obj = self.values[index.row()]
        setattr(obj, field_name, value)




    def setCustomData(self, data: dict):
        self.headers = list(shema.values())
        self.values = data

    def rowCount(self, parent):
        return len(self.values)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return getattr(self.values[index.row()],shema[index.column()])

    def headerData(self, section, orientation, role):
        if (role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal):
            return QVariant()
        return self.headers[section]



app = QApplication([])
model = TableModel()
model.setCustomData(projects)
view = QTableView()
view.setModel(model)



view.resizeColumnsToContents()
view.horizontalHeader().setStretchLastSection(True)

view.show()
app.exec()
