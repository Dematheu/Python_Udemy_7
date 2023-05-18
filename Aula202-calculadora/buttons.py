import math

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import ConvertToNumber, isEmpty, isNumOrDot, isValidNumber
from variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Base para determinar o 'layout' da grid (a ordem dos botões).
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window

        # Valor inicial da equação (acima do display)
        self._equation = ''
        self._equationInitialValue = '-----'
        self.equation = self._equationInitialValue

        # Valores dos números e operadores
        self._left = None
        self._right = None
        self._op = None

        # Faz a GRID
        self._makeGrid()

    # Getter e setter para os valores da equação (acima do display)
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # Cria a grid usando a base (Grid Mask)
    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for row_number, row_data in enumerate(self._grid_mask):
            for column_number, button_txt in enumerate(row_data):
                button = Button(button_txt)

                if not isNumOrDot(button_txt) and not isEmpty(button_txt):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertToDisplay, button_txt)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = ConvertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        # Verifica se o número é válido
        if not isValidNumber(newDisplayValue):
            return  # Se não for válido, retorna antes e não adicina nada.

        # Se for válido, retorna o número digitado.
        self.display.insert(text)
        self.display.setFocus()

    # Limpa o display e a equação.
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    # Determina o operador.
    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # deverá ser o numero left
        self.display.clear()               # limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem
        # adicionar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        # Se houver algo no número left,
        # não fazemos nada. Aguardamos o outro número (right)
        if self._left is None:
            self._left = ConvertToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Conta incompleta.')
            return

        self._right = ConvertToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Número muito grande.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'Error':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok)
        msgBox.exec()
