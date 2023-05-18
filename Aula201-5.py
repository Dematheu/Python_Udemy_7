# Trabalhando com classes e herança no PySide6

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Botão
        self.botao1 = self.make_button('Botão 01')
        self.botao2 = self.make_button('Botão 02')
        self.botao3 = self.make_button('Botão 03')
        self.botao4 = self.make_button('Botão 04')

        # Central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Hello World!')

        # Layout
        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 1, 3, 1, 1)
        self.grid_layout.addWidget(self.botao4, 2, 1, 1, 3)

        # Status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostra mensagem na barra de Status')

        # Menu Bar
        self.menu = self.menuBar()

        # Ações do Menu
        self.first_menu = self.menu.addMenu('File')
        self.first_action = self.first_menu.addAction('Primeira ação')
        self.first_action.triggered.connect(self.slot_example)

        self.second_action = self.first_menu.addAction('Segunda ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.other_slot)
        self.second_action.hovered.connect(self.other_slot)

    @Slot()
    def slot_example(self, status_bar):  # Muda a mensagem do Status bar
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def other_slot(self):  # Segunda ação marcada
        print('Está marcado?', self.second_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(f'font-size: 40px; color:red')
        btn.clicked.connect(self.other_slot)
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação
