from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui

app = QApplication([])
label = QLabel('Hello World!')
label.setAlignment(Qt.AlignCenter)
label.setFont(QtGui.QFont('Times New Roman', 30))


label.show()
app.exec()


