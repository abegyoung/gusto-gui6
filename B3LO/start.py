import sys
import time
import serial
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

Ser=0

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

      #Comm
      self.btn_close.clicked.connect(self.btn_close_clicked)
      self.btn_open.clicked.connect(self.btn_open_clicked)

      #PCA9502
      self.dcdc1.toggled.connect(self.btn_dcdc1_clicked)
      self.dcdc2.toggled.connect(self.btn_dcdc2_clicked)
      self.dcdc3.toggled.connect(self.btn_dcdc3_clicked)
      self.dcdc4.toggled.connect(self.btn_dcdc4_clicked)
      self.dcdc5.toggled.connect(self.btn_dcdc5_clicked)
      self.dcdc6.toggled.connect(self.btn_dcdc6_clicked)
      self.dcdc7.toggled.connect(self.btn_dcdc7_clicked)
      self.dcdc8.toggled.connect(self.btn_dcdc8_clicked)

      #QCL ON QCL MODE
      self.qcl_on.toggled.connect(self.btn_qclonoff_clicked)
      self.qcl_mode.toggled.connect(self.imodeButton_clicked)

      #DAC spin buttons
      self.spin_bias1_dac.valueChanged.connect(self.update_multbias1)
      self.spin_bias2_dac.valueChanged.connect(self.update_multbias2)
      self.spin_bias3_dac.valueChanged.connect(self.update_multbias3)
      self.spin_qcl1_dac.valueChanged.connect(self.update_qclbias1)
      self.spin_qcl2_dac.valueChanged.connect(self.update_qclbias2)
      self.spin_qcl3_dac.valueChanged.connect(self.update_qclbias3)

      ### TIMER ###

      #self.timer = QtCore.QTimer(self)
      #self.timer.setInterval(100)
      #self.timer.timeout.connect(self.blink)

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



    ### DCDC TAB ###

    def btn_dcdc1_clicked(self, enabled):
      cmd="dcdc 1 0\r"
      if enabled:
        cmd="dcdc 1 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

    def btn_dcdc2_clicked(self, enabled):
      cmd="dcdc 2 0\r"
      if enabled:
        cmd="dcdc 2 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))
 
    def btn_dcdc3_clicked(self, enabled):
      cmd="dcdc 3 0\r"
      if enabled:
        cmd="dcdc 3 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

    def btn_dcdc4_clicked(self, enabled):
      cmd="dcdc 4 0\r"
      if enabled:
        cmd="dcdc 4 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

    def btn_dcdc5_clicked(self, enabled):
      cmd="dcdc 5 0\r"
      if enabled:
        cmd="dcdc 5 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

    def btn_dcdc6_clicked(self, enabled):
      cmd="dcdc 6 0\r"
      if enabled:
        cmd="dcdc 6 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

    def btn_dcdc7_clicked(self, enabled):
      cmd="dcdc 7 0\r"
      if enabled:
        cmd="dcdc 7 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))
 
    def btn_dcdc8_clicked(self, enabled):
      cmd="dcdc 8 0\r"
      if enabled:
        cmd="dcdc 8 1\r"
      Ser.write(cmd.encode())
      #returns=coreSERIAL.read_end(Ser,'\n')
      returns = Ser.read(100)
      self.serverResponse.setText(str(returns))

    def imodeButton_clicked(self, enabled):
      cmd="mode 0\r"
      if enabled:
        cmd="mode 1\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse.setText(str(data))

    def update_multbias1(self):
      value = self.spin_bias1_dac.value()
      cmd="mult 1 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      self.textEdit_7.setText(str(Vmon))
      self.textEdit_8.setText(str(Imon))

    def update_multbias2(self):
      value = self.spin_bias2_dac.value()
      cmd="mult 2 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      self.textEdit_9.setText(str(Vmon))
      self.textEdit_10.setText(str(Imon))

    def update_multbias3(self):
      value = self.spin_bias3_dac.value()
      cmd="mult 3 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      self.textEdit_11.setText(str(Vmon))
      self.textEdit_12.setText(str(Imon))

    def update_qclbias1(self):
      value = self.spin_qcl1_dac.value()
      cmd="qcl 1 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      Vs  =float(data[10])
      self.textEdit_1.setText(str(Vmon))
      self.textEdit_2.setText(str(Imon))
      self.textEdit_41.setText(str(Vs))

    def update_qclbias2(self):
      value = self.spin_qcl2_dac.value()
      cmd="qcl 2 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      Vs  =float(data[10])
      self.textEdit_3.setText(str(Vmon))
      self.textEdit_4.setText(str(Imon))
      self.textEdit_42.setText(str(Vs))

    def update_qclbias3(self):
      value = self.spin_qcl3_dac.value()
      cmd="qcl 3 %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      Vmon=float(data[3])
      Imon=float(data[6])
      Vs  =float(data[10])
      self.textEdit_5.setText(str(Vmon))
      self.textEdit_6.setText(str(Imon))
      self.textEdit_43.setText(str(Vs))

    def btn_qclonoff_clicked(self, enabled):
      if enabled:
        cmd="qcl on\r"
      else:
        cmd="qcl off\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse.setText(str(returns))

      time.sleep(0.5)

      cmd="qcl\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
      self.textEdit_1.setText( str(float(data[3])))   #QCL 1 V
      self.textEdit_2.setText( str(float(data[6])))   #QCL 1 I
      self.textEdit_41.setText(str(float(data[9])))   #QCL 1 Vsense
      self.textEdit_3.setText( str(float(data[13])))  #QCL 2 V
      self.textEdit_4.setText( str(float(data[16])))  #QCL 2 I
      self.textEdit_42.setText(str(float(data[19])))  #QCL 2 Vsense
      self.textEdit_5.setText( str(float(data[23])))  #QCL 3 V
      self.textEdit_6.setText( str(float(data[26])))  #QCL 3 I
      self.textEdit_43.setText(str(float(data[29])))  #QCL 3 Vsense



    def btn_open_clicked(self):
      global Ser
      Ser = serial.Serial(
          #port='/Users/young/dev/vmodem0',
          port='/dev/cu.usbmodemB3LO_CTRL1',
          baudrate=19200,
          timeout=1
      )

    def btn_close_clicked(self):
      global Ser
      Ser.close()
      Ser = 0

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
