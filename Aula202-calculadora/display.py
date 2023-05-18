# from typing import TYPE_CHECKING

# if TYPE_CHECKING:   -> para prevnir circular import
#     from buttons import Button
#     from info import Info
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    # Definir funcionalidade para tecla
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        # Configurado tecla enter, bckspc e clear.
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isBackspace = key in [KEYS.Key_Backspace]
        isClear = key in [KEYS.Key_C, KEYS.Key_Escape]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus,
                             KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]

        if isEnter or text == '=':
            # Emite um sinal quando a tecla é pressionada.
            self.eqPressed.emit()
            # Ignora a tecla no display.
            return event.ignore()

        if isBackspace:
            self.delPressed.emit()
            return event.ignore()

        if isClear:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator or text == '^':
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
