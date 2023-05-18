# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão


import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Botão 01')
botao.setStyleSheet('font-size: 40px; color: red')
botao.show()  # Adiciona o widget na hierarquia e exibe a janela

botao2 = QPushButton('Botão 02')
botao2.setStyleSheet('font-size: 40px; color: blue')
botao2.show()  # Adiciona o widget na hierarquia e exibe a janela


app.exec()  # O loop da aplicação
