# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Hello World!')

botao1 = QPushButton('Botão 01')
botao1.setStyleSheet('font-size: 40px; color: red')

botao2 = QPushButton('Botão 02')
botao2.setStyleSheet('font-size: 40px; color: blue')

botao3 = QPushButton('Botão 03')
botao3.setStyleSheet('font-size: 40px; color: green')

botao4 = QPushButton('Botão 04')
botao4.setStyleSheet('font-size: 40px; color: grey')

# Central Widget não recebe outros Widgets. Então criamos o Layout
layout = QGridLayout()

# Depois passamos que o layout do Central Widget é este que acabamos de criar
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 1, 3, 1, 1)
layout.addWidget(botao4, 2, 2, 1, 1)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def other_slot(checked):
    print('Está marcado?', checked)


@Slot()
def another_slot(action):
    def inner():
        other_slot(action.isChecked())
    return inner


status_bar = window.statusBar()
status_bar.showMessage('Mostra mensagem na barra de Status')

menu = window.menuBar()
first_menu = menu.addMenu('File')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Segunda ação')
second_action.setCheckable(True)
second_action.toggled.connect(other_slot)
second_action.hovered.connect(another_slot(second_action))

botao1.clicked.connect(another_slot(second_action))


window.show()
app.exec()  # O loop da aplicação
