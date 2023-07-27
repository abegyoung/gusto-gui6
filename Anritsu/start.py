import sys
import time
import serial
import datetime as dt
import numpy as np
from sys import argv, exit
from io import StringIO
import coreSERIAL
import matplotlib.pyplot as plt

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
i=0
t_start=0


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

      #PLOT
      self.xdata = list(range(60))
      self.ydata1 = [float(0.) for i in range(60)]
      self._plot_ref1 = None
      self.show()


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
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse.setText(str(data))
      self.serverCommand.setText("")

    def runButton_clicked(self, enabled):
      self.timer.stop()
      if enabled:
        self.timer.start()

    def btn_open_clicked(self):
      global Ser
      Ser = serial.Serial(
          port='COM6', #COM6 is for windows. Linux e.g. '/dev/ttyACM0',
          baudrate=19200,
          timeout=1
      )
      cmd="IDN?\n"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse.setText(str(data))

    def btn_close_clicked(self):
      global Ser
      global i
      self.timer.stop()
      Ser.close()
      Ser = 0

    @QtCore.pyqtSlot()
    def blink(self):
      global Ser
      global i
      global t_start
      cmd="PWR?\n"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.dBm_textEdit.setText(str(float(data[0])))
      watt=(10**(float(data[0])/10))/1000
      watt_string = "{:.3e}".format(watt)
      self.watt_textEdit.setText(watt_string)
      #MAKE DATA
      self.ydata1 = self.ydata1[1:] + [np.genfromtxt(StringIO(watt_string))]        #Setpoint
      if self._plot_ref1 is None:
        #t_start = time.time()
        #i=1
        
        self.mpl.canvas.ax.get_xaxis().grid(True)
        self.mpl.canvas.ax.get_yaxis().grid(True)  
        self.mpl.canvas.ax.set_xlim(0,50)
        self.mpl.canvas.ax.set_ylim(0,5E-7)
        self.mpl.canvas.draw()
        self.background = self.mpl.canvas.copy_from_bbox(self.mpl.canvas.ax.bbox)
        plot_refs1 = self.mpl.canvas.ax.plot(self.xdata, self.ydata1, 'blue')
        self._plot_ref1 = plot_refs1[0]
      else:  
        #i=i+1
        self._plot_ref1.set_ydata(self.ydata1)
        self.mpl.canvas.restore_region(self.background)
        # draw the point on the screen
        self.mpl.canvas.ax.draw_artist(self._plot_ref1)
        # blit the axes
        self.mpl.canvas.blit(self.mpl.canvas.ax.bbox)
        #tx = 'Mean Frame Rate:\n {fps:.3f}FPS'.format(fps= ((i+1) / (time.time() - t_start)) ) 
        #print(tx)
  
      
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