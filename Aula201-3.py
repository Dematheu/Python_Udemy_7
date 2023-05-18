# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window -> setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#               -> Widget 4 (botao4)
#   -> show
# -> exec
import sys

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


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


# Status bar
status_bar = window.statusBar()
status_bar.showMessage('Mostra mensagem na barra de Status')

# Menu bar
menu = window.menuBar()
first_menu = menu.addMenu('File')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(lambda: slot_example(status_bar))


window.show()
app.exec()  # O loop da aplicação
