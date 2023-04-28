import sys
import time
import serial
import datetime as dt
import numpy as np
from sys import argv, exit
from io import StringIO

import matplotlib

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

Ser=0
x = np.arange(600)
y = np.zeros(600)

def read_end(the_port, End):
  total_data=[];data=''
  while True:
    try:
      data=the_port.read(1)
    except:
      break
    if End in data:
      total_data.append(data[:data.find(End)])
      break
    total_data.append(data)
    if len(total_data)>1:
      # check if end_of_data was split
      last_pair=total_data[-2]+total_data[-1]
      if End in last_pair:
        total_data[-2]=last_pair[:last_pair.find(End)]
        total_data.pop()
        break
  return ''.join(total_data)


class Window(QMainWindow, form_class):
    def __init__(self):
      super().__init__(parent=None)
      self.setWindowTitle("QMainWindow")
      self.setCentralWidget(QLabel("I'm the Central Widget"))
      self._createMenu()
      self._createToolBar()
      self._createStatusBar()
      self.setupUi(self)

      ### SIGNALS AND SLOTS ###

      self.btn_close.clicked.connect(self.btn_close_clicked)
      self.btn_open.clicked.connect(self.btn_open_clicked)
      #self.serverCommand.connect(self.serverCommand, SIGNAL("returnPressed(void)"), self.sendcmd)

      self.runButton.toggled.connect(self.runButton_clicked)
      self.startButton.toggled.connect(self.startButton_clicked)

      ### TIMER ###

      self.timer = QtCore.QTimer(self)
      self.timer.setInterval(100)
      self.timer.timeout.connect(self.blink)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def start(self):
      self.timer.start()

    def stop(self):
      self.timer.stop()

    def startButton_clicked(self, enabled):
      global Ser
      cmd="STOP\n"
      if enabled:
        cmd="START\n"
      Ser.write(cmd.encode())
      #data=read_end(Ser, '\n')
      data=Ser.read(100).split()
      self.serverResponse.setText(str(data))
      self.serverCommand.setText("")

    def runButton_clicked(self, enabled):
      self.timer.stop()
      if enabled:
        self.timer.start()

    def btn_open_clicked(self):
      global Ser
      Ser = serial.Serial(
          port='/dev/cu.usbmodem142301',
          baudrate=19200,
          timeout=1
      )
      cmd="IDN?\n"
      Ser.write(cmd.encode())
      #data=read_end(Ser, '\n')
      data=Ser.read(100)
      self.serverResponse.setText(str(data))

    def btn_close_clicked(self):
      global Ser
      self.timer.stop()
      Ser.close()
      Ser = 0

    @QtCore.pyqtSlot()
    def blink(self):
      global Ser
      global x
      global y
      cmd="PWR?\n"
      Ser.write(cmd.encode())
      #data=read_end(Ser, '\n').split()
      data=Ser.read(100).split()
      self.dBm_textEdit.setText(str(float(data[0])))
      watt=(10**(float(data[0])/10))/1000
      watt_string = "{:.3e}".format(watt)
      self.watt_textEdit.setText(watt_string)
      #MAKE DATA
      y = np.roll(y, -1)
      #y[-1] = np.genfromtxt(StringIO(data[0])) #plot dBm
      y[-1] = np.genfromtxt(StringIO(watt_string)) #plot Watt
      #PLOT DATA
      self.mpl.canvas.ax.clear()
      #self.mpl.canvas.ax.set_xlim(xmin=0, xmax=600)
      #self.mpl.canvas.ax.set_ylim(ymin=9.0*(10**-5), ymax=4.0*(10**-4))
      self.mpl.canvas.ax.get_xaxis().grid(True)
      self.mpl.canvas.ax.get_yaxis().grid(True)
      self.mpl.canvas.ax.plot(x,y)
      self.mpl.canvas.draw()

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
