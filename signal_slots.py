from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#Создаем объект приложения
app = QApplication([])
#Создаем виджет
window = QWidget()

#Создаем кнопку
layout = QVBoxLayout ()

# Первая кнопка показывает простое сообщение
button_message = QPushButton("Показать сообщение")

# Радиокнопка для включения/выключения состояния
radio_button = QRadioButton("Включено")

# Кнопка для подсчета кликов
counter_button = QPushButton("Click count = 0")
count = 0  # Переменная для хранения текущего значения кликов

# Метка для отображения статуса радио-кнопки
label_status = QLabel("Радиокнопка выключена.")

# Добавляем элементы в макет
layout.addWidget(button_message)
layout.addWidget(radio_button)
layout.addWidget(label_status)  # Теперь метка постоянно присутствует в окне
layout.addWidget(counter_button)


#Определяем функцию которая будет вызываться когда пользователь нажмет кнопку
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

def increment_count():
    global count
    count += 1
    counter_button.setText(f'Click count = {count}')

# Обработка второй кнопки: смена статуса включен/выключен
def toggle_radio():
    if radio_button.isChecked():
        label_status.setText("Радиокнопка включена.")
    else:
        label_status.setText("Радиокнопка выключена.")

#Тут мы говорим программе что при нажатие кнопки должна быть вызвана наша функция (выше)
button_message.clicked.connect(on_button_clicked)
radio_button.toggled.connect(toggle_radio)
counter_button.clicked.connect(increment_count)

window.setLayout(layout)
window.show()

app.exec()