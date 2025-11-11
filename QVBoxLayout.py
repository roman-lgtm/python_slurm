from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

layout = QFormLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(QPushButton('Pot'))
layout.addWidget(QPushButton('Mottob'))

label = QLabel('Top')
label.setAlignment(Qt.AlignCenter)
label1 = QLabel('Bottom')
label1.setAlignment(Qt.AlignCenter)

layout.addWidget(label)
layout.addWidget(label1)

window.setLayout(layout)
window.show()
app.exec()