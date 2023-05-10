import sys
import time
import socket
import datetime as dt
import numpy as np
from sys import argv, exit
from io import StringIO

import matplotlib
import coreSERIAL

from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QWidget,
)

form_class = uic.loadUiType("mainwindow.ui")[0]

s=0
sport = 9001
serverip = '192.168.1.100'

xy = np.zeros((8,2))

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self.setupUi(self)

        ### SIGNALS AND SLOTS ###

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_open.clicked.connect(self.btn_open_clicked)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.blink)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def getbias(self):
        cmd="getcurrents\n"
        s.send(cmd.encode())
        data=coreSERIAL.recv_end(s,'\n').split()
        for pixel in range(1,9,1):
            xy[pixel-1,0] = pixel
            xy[pixel-1,1] = float(data[pixel])

        self.lcdNumber_1.display(str("{:.1f}".format(xy[0,1])))
        self.lcdNumber_2.display(str("{:.1f}".format(xy[1,1])))
        self.lcdNumber_3.display(str("{:.1f}".format(xy[2,1])))
        self.lcdNumber_4.display(str("{:.1f}".format(xy[3,1])))
        self.lcdNumber_5.display(str("{:.1f}".format(xy[4,1])))
        self.lcdNumber_6.display(str("{:.1f}".format(xy[5,1])))
        self.lcdNumber_7.display(str("{:.1f}".format(xy[6,1])))
        self.lcdNumber_8.display(str("{:.1f}".format(xy[7,1])))

        #PLOT
        self.mpl.canvas.ax.clear()
        self.mpl.canvas.ax.set_xlim(xmin=0, xmax=9)
        self.mpl.canvas.ax.set_ylim(ymin=0, ymax=130)
        #self.mpl.canvas.ax.autoscale(enable='False')
        self.mpl.canvas.ax.get_xaxis().grid(True)
        self.mpl.canvas.ax.get_yaxis().grid(True)
        self.mpl.canvas.ax.plot(xy[0:8,0],xy[0:8,1], marker="s")
        self.mpl.canvas.draw()

    @QtCore.pyqtSlot()
    def blink(self):
        self.getbias()

    def btn_close_clicked(self):
        global s
        s.close()
        del s
        self.timer.stop()

    def btn_open_clicked(self):
        global s
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((serverip, sport))
        s.settimeout(30)
        self.timer.start()

def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
