from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Исходные данные
headers = ["Name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]


class TableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data
        self.headers = headers

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return QVariant()

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.headers[section]
        return QVariant()

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            # Меняем данные в нашем списке _data, но сначала преобразуем из кортежа в лист
            row = list(self._data[index.row()])
            row[index.column()] = value
            self._data[index.row()] = tuple(row)
            return True
        return False


    def flags(self, index):
        # Разрешаем редактирование + стандартные флаги
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable


app = QApplication([])
model = TableModel(rows, headers)
view = QTableView()
view.setModel(model)
view.setEditTriggers(QAbstractItemView.DoubleClicked)
view.show()
app.exec()