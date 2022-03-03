from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from termcolor import cprint
import json
import os
import sys
import glob

import essentials

program_name = "dragonsshadowz"


class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)


class UIApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = 900
        self.window_height = 500

        self.setGeometry(80, 50, self.window_width, self.window_height)
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle(program_name)
        # self.setWindowIcon(QIcon('img/streaming.png'))

        self.colorDarkGreen = "#264653"
        self.colorGreen = "#2a9d8f"
        self.colorGreenArmy = "#6b705c"
        self.colorYellow = "#e9c46a"
        self.colorOrange = "#f4a261"
        self.colorRed = "#e76f51"

        self.widthBotButton = 100
        self.heightBotButton = 50
        self.posXBotButton = 20
        self.posYBotButton = 20

        # self.scroll = QScrollArea(self)
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        #self.scroll.setGeometry( 0, 100, self.window_width, self.window_height - 120)

        self.UISetups()

    def UISetups(self):
        self.BotButton01 = QPushButton('Bot 01', self)
        self.BotButton01.setGeometry(10, 50, 100, 70)
        self.BotButton01.setStyleSheet("QWidget {color: blue}")
        self.BotButton01.clicked.connect(self.on_click01)

        self.BotButton02 = QPushButton('Bot 02', self)
        self.BotButton02.setGeometry(10, 150, 100, 70)
        self.BotButton02.setStyleSheet("QWidget {color: black}")
        self.BotButton02.clicked.connect(self.on_click02)

        self.BotButton03 = QPushButton('Bot 03', self)
        self.BotButton03.setGeometry(10, 250, 100, 70)
        self.BotButton03.setStyleSheet("QWidget {color: black}")
        self.BotButton03.clicked.connect(self.on_click03)

        self.StatusBackgroundOuter = QFrame(self)
        self.StatusBackgroundOuter.setStyleSheet(
            "QWidget {border-radius: 5px; background-color:%s}" % self.colorRed)
        self.StatusBackgroundOuter.setGeometry(150, 50, 150, 100)

        self.StatusBackgroundInner = QFrame(self)
        self.StatusBackgroundInner.setStyleSheet(
            "QWidget {border-radius: 5px; background-color: white}")
        self.StatusBackgroundInner.setGeometry(160, 60, 130, 80)

        self.BotStatusLabel = QLabel(self)
        self.BotStatusLabel.setText("Bot status: ")
        self.BotStatusLabel.setStyleSheet(
            "QWidget {color: black; font-size: 15px; font-weight: bold}")
        self.BotStatusLabel.setGeometry(170, 40, 130, 80)

        self.BotStatusLabel01 = QLabel(self)
        self.BotStatusLabel01.setText("Offline ")
        self.BotStatusLabel01.setStyleSheet(
            "QWidget {color: red; font-size: 15px; font-weight: bold}")
        self.BotStatusLabel01.setGeometry(170, 70, 130, 80)

        # Description
        self.DescBackgroundOuter = QFrame(self)
        self.DescBackgroundOuter.setStyleSheet(
            "QWidget {border-radius: 5px; background-color:%s}" % self.colorDarkGreen)
        self.DescBackgroundOuter.setGeometry(350, 50, 250, 100)

        self.DescBackgroundInner = QFrame(self)
        self.DescBackgroundInner.setStyleSheet(
            "QWidget {border-radius: 5px; background-color: white}")
        self.DescBackgroundInner.setGeometry(360, 60, 230, 80)

        self.BotDescLabel = QLabel(self)
        self.BotDescLabel.setText("This is Bot 01.")
        self.BotDescLabel.setStyleSheet(
            "QWidget {color: black; font-size: 15px; font-weight: bold}")
        self.BotDescLabel.setGeometry(370, 40, 230, 80)

        # Terminal
        self.TerminalBackgroundOuter = QFrame(self)
        self.TerminalBackgroundOuter.setStyleSheet(
            "QWidget {border-radius: 5px; background-color:%s}" % self.colorDarkGreen)
        self.TerminalBackgroundOuter.setGeometry(150, 175, 450, 300)

        self.TerminalBackgroundInner = QFrame(self)
        self.TerminalBackgroundInner.setStyleSheet(
            "QWidget {border-radius: 5px; background-color: black}")
        self.TerminalBackgroundInner.setGeometry(155, 180, 440, 290)

        self.BotTerminalLog = ScrollLabel(self)
        self.BotTerminalLog.setText('')
        self.BotTerminalLog.setStyleSheet(
            "QWidget {color: green; font-size: 10px; background-color: black}")
        self.BotTerminalLog.setGeometry(160, 185, 430, 280)

    @pyqtSlot()
    def on_click01(self):
        self.BotButton01.setStyleSheet("QWidget {color: blue}")
        self.BotButton02.setStyleSheet("QWidget {color: black}")
        self.BotButton03.setStyleSheet("QWidget {color: black}")

        self.BotStatusLabel01.setText("Offline ")
        self.BotStatusLabel01.setStyleSheet(
            "QWidget {color: red; font-size: 15px; font-weight: bold}")
        self.StatusBackgroundOuter.setStyleSheet(
            "QWidget {border-radius: 5px; background-color:%s}" % self.colorRed)
        self.BotDescLabel.setText("This is Bot 01.")

    def on_click02(self):
        self.BotButton01.setStyleSheet("QWidget {color: black}")
        self.BotButton02.setStyleSheet("QWidget {color: blue}")
        self.BotButton03.setStyleSheet("QWidget {color: black}")

        self.BotStatusLabel01.setText("Online ")
        self.BotStatusLabel01.setStyleSheet(
            "QWidget {color: green; font-size: 15px; font-weight: bold}")
        self.StatusBackgroundOuter.setStyleSheet(
            "QWidget {border-radius: 5px; background-color:%s}" % self.colorGreen)
        self.BotDescLabel.setText("This is Bot 02.")

    def on_click03(self):
        self.BotButton01.setStyleSheet("QWidget {color: black}")
        self.BotButton02.setStyleSheet("QWidget {color: black}")
        self.BotButton03.setStyleSheet("QWidget {color: blue}")


def Main():
    app = QApplication(sys.argv)
    w = UIApp()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    Main()
