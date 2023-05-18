import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':

    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Aplica o tema
    setupTheme()

    # Ícone da janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    # Grid (botões)
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa
    window.adjustFixedSize()
    window.show()
    app.exec()
