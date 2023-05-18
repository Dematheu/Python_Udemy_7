# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 448)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridMain = QGridLayout()
        self.gridMain.setObjectName(u"gridMain")
        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName(u"labelResult")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignCenter)

        self.gridMain.addWidget(self.labelResult, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineName = QLineEdit(self.centralwidget)
        self.lineName.setObjectName(u"lineName")
        font1 = QFont()
        font1.setPointSize(12)
        self.lineName.setFont(font1)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName(u"labelName")
        font2 = QFont()
        font2.setPointSize(18)
        self.labelName.setFont(font2)
        self.labelName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 1)

        self.ButtonSend = QPushButton(self.centralwidget)
        self.ButtonSend.setObjectName(u"ButtonSend")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.ButtonSend.setFont(font3)

        self.gridLayout_2.addWidget(self.ButtonSend, 0, 2, 1, 1)


        self.gridMain.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridMain)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 756, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"Nothing Here", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Seu Nome:", None))
        self.ButtonSend.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

