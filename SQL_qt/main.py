from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sqlalchemy.orm import Session

from initdb import engine,YaProject

projects = []
with engine.connect() as conn:
    session=Session(bind=conn)
    projects= list(session.query(YaProject).all())
shema = {0:"col1",1:"col2",2:"col3",3:"col4",4:"col5"}

class TableModel(QAbstractTableModel):
    projects = []
    with engine.connect() as conn:
        session=Session(bind=conn)

    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            setattr(self.values[index.row()][index.column()], value)
            conn.execute(insert(users), values=[value])
            session.flush()
            session.commit()
            return True

    def setCustomData(self, data: dict):
        self.headers = list(shema.values())
        self.values = data

    def rowCount(self, parent):
        return len(max(self.values))

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return getattr(self.values[index.column()][index.row()])

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]

app = QApplication([])
model = TableModel()
model.setCustomData(projects)
view = QTableView()
view.setModel(model)
view.show()
app.exec()
