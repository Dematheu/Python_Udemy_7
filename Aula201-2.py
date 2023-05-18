# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Botão 01')
botao.setStyleSheet('font-size: 40px; color: red')

botao2 = QPushButton('Botão 02')
botao2.setStyleSheet('font-size: 40px; color: blue')

botao3 = QPushButton('Botão 03')
botao3.setStyleSheet('font-size: 40px; color: green')

botao4 = QPushButton('Botão 04')
botao4.setStyleSheet('font-size: 40px; color: grey')

# Local central onde colocaremos outros Widgets.
central_widget = QWidget()

# Central Widget não recebe outros Widgets. Então criamos o Layout
layout = QGridLayout()

# Depois passamos que o layout do Central Widget é este que acabamos de criar
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 1, 3, 1, 1)
layout.addWidget(botao4, 2, 2, 1, 1)

central_widget.show()  # Adiciona o widget na hierarquia e exibe a janela
app.exec()  # O loop da aplicação
