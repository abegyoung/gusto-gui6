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
      self.setupUi(self)

      ### SIGNALS AND SLOTS ###

      #Comm
      self.btn_open.clicked.connect(self.btn_open_clicked)
      self.btn_close.clicked.connect(self.btn_close_clicked)
      self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
      self.serverCommand.returnPressed.connect(self.sendcmd)
      self.serverCommand_2.returnPressed.connect(self.sendcmd_2)
      self.serverCommand_3.returnPressed.connect(self.sendcmd_3)
      self.serverCommand_4.returnPressed.connect(self.sendcmd_4)

      #QCL ON QCL MODE
      self.qcl_on.toggled.connect(self.btn_qclonoff_clicked)
      self.qcl_mode.toggled.connect(self.imodeButton_clicked)

      #PCA9502
      self.dcdc1.toggled.connect(self.btn_dcdc1_clicked)
      self.dcdc2.toggled.connect(self.btn_dcdc2_clicked)
      self.dcdc3.toggled.connect(self.btn_dcdc3_clicked)
      self.dcdc4.toggled.connect(self.btn_dcdc4_clicked)
      self.dcdc5.toggled.connect(self.btn_dcdc5_clicked)
      self.dcdc6.toggled.connect(self.btn_dcdc6_clicked)
      self.dcdc7.toggled.connect(self.btn_dcdc7_clicked)
      self.dcdc8.toggled.connect(self.btn_dcdc8_clicked)

      #DAC spin buttons
      self.spin_bias1_dac.valueChanged.connect(self.update_multbias1)
      self.spin_bias2_dac.valueChanged.connect(self.update_multbias2)
      self.spin_bias3_dac.valueChanged.connect(self.update_multbias3)
      self.spin_qcl1_dac.valueChanged.connect(self.update_qclbias1)
      self.spin_qcl2_dac.valueChanged.connect(self.update_qclbias2)
      self.spin_qcl3_dac.valueChanged.connect(self.update_qclbias3)

      #AMPILTUDE PID
      self.spin_pidkp.valueChanged.connect(self.update_pidkp)
      self.spin_pidki.valueChanged.connect(self.update_pidki)
      self.spin_pidkd.valueChanged.connect(self.update_pidkd)
      self.spin_pidsp.valueChanged.connect(self.update_pidsp)
      self.btn_pidmonitor.toggled.connect(self.btn_pidmonitor_clicked)

      #FREQUENCY PID
      self.spin_pidkp_2.valueChanged.connect(self.update_pidkp_2)
      self.spin_pidki_2.valueChanged.connect(self.update_pidki_2)
      self.spin_pidkd_2.valueChanged.connect(self.update_pidkd_2)
      self.spin_pidsp_2.valueChanged.connect(self.update_pidsp_2)
      self.btn_pidmonitor_2.toggled.connect(self.btn_pidmonitor_2_clicked)

      #PSAT Control
      self.spin_psat_dac.valueChanged.connect(self.update_psat)

      #SYNTH Control
      self.spin_synth_freq.valueChanged.connect(self.update_synth)
      self.synthButton.toggled.connect(self.synthButton_clicked)
      self.btn_lock_status.clicked.connect(self.btn_lock_status_clicked)

      #Voice Coil
      self.spin_voicecoil.valueChanged.connect(self.update_voicecoil)

      ### TIMER ###

      #self.timer = QtCore.QTimer(self)
      #self.timer.setInterval(100)
      #self.timer.timeout.connect(self.blink)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    ### DCDC TAB ###

    def btn_dcdc1_clicked(self, enabled):
      cmd="dcdc 1 0\r"
      if enabled:
        cmd="dcdc 1 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))

    def btn_dcdc2_clicked(self, enabled):
      cmd="dcdc 2 0\r"
      if enabled:
        cmd="dcdc 2 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))
 
    def btn_dcdc3_clicked(self, enabled):
      cmd="dcdc 3 0\r"
      if enabled:
        cmd="dcdc 3 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))

    def btn_dcdc4_clicked(self, enabled):
      cmd="dcdc 4 0\r"
      if enabled:
        cmd="dcdc 4 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))

    def btn_dcdc5_clicked(self, enabled):
      cmd="dcdc 5 0\r"
      if enabled:
        cmd="dcdc 5 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))

    def btn_dcdc6_clicked(self, enabled):
      cmd="dcdc 6 0\r"
      if enabled:
        cmd="dcdc 6 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))

    def btn_dcdc7_clicked(self, enabled):
      cmd="dcdc 7 0\r"
      if enabled:
        cmd="dcdc 7 1\r"
      Ser.write(cmd.encode())
      returns=coreSERIAL.read_end(Ser,'\n')
      self.serverResponse_2.setText(str(returns))
 
    def btn_dcdc8_clicked(self, enabled):
      cmd="dcdc 8 0\r"
      if enabled:
        cmd="dcdc 8 1\r"
      Ser.write(cmd.encode())
      #returns=coreSERIAL.read_end(Ser,'\n')
      returns = Ser.read(100)
      self.serverResponse_2.setText(str(returns))

    def synthButton_clicked(self, enabled):
      cmd = ["dcdc 6 0\r", "dcdc 2 0\r", "setsynth init\r"]
      if enabled:
        cmd = ["dcdc 6 1\r", "dcdc 2 1\r", "setsynth init\r"]
      for i in range(0, 3):
        Ser.write(cmd[i].encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse_2.setText(str(data))
        time.sleep(1)

    def update_synth(self):
      value = self.spin_synth_freq.value()
      cmd = "setsynth freq %.6f\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_2.setText(str(data))

    def btn_lock_status_clicked(self):
      cmd = "setsynth read 15\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse_2.setText(str(data))
      #if int(data.split()[3],16):
      #  self.led_3.leds[0].valueTrue()
      #else:
      #  self.led_3.leds[0].valueFalse()



    ### Main Tab ###

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

    def update_psat(self):
      value = self.spin_psat_dac.value()
      cmd = "psat %d\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      self.textEdit_psatv.setText(str(float(data[2])))
      self.textEdit_psati.setText(str(float(data[5])))

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

    def update_voicecoil(self):
      value = self.spin_voicecoil.value()
      cmd = "coil %d\r" % value
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse.setText(str(data))
      self.textEdit_30.setText(str(float(data[2])))

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

    def sendcmd(self):
      cmd= "%s\r" % self.serverCommand.text()
      print(cmd)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse.setText(str(data))
      self.serverCommand.setText("")

    def sendcmd_2(self):
      cmd= "%s\r" % self.serverCommand_2.text()
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse_2.setText(str(data))
      self.serverCommand_2.setText("")

    def sendcmd_3(self):
      cmd= "%s\r" % self.serverCommand_3.text()
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse_3.setText(str(data))
      self.serverCommand_3.setText("")

    def sendcmd_4(self):
      cmd= "%s\r" % self.serverCommand_3.text()
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n')
      self.serverResponse_4.setText(str(data))
      self.serverCommand_4.setText("")

    def btn_refresh_clicked(self):

      # GET DATA
      cmd="voltages\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
      N=28

      # translate +/- to p/n
      datan=[None]*N
      for i in range(0,N,2):
        datan[i]=str(data[i]).translate(string.maketrans('+-.','pnp'))
        datan[i+1]=data[i+1]

      #define template named tuple
      Volts = namedtuple('Volts', datan[::2])

      #fill the tuple with data
      v = Volts._make(datan[1::2])

      self.rail0.setText(str("p5V_REF_MON"))
      self.rail1.setText(str("n36V_MON_BUF"))
      self.rail2.setText(str("p5V_ANA_MON"))
      self.rail3.setText(str("pV_ANA_MON"))
      self.rail4.setText(str("nV_ANA_MON_BUF"))
      self.rail5.setText(str("p5V_MON"))
      self.rail6.setText(str("SBC_3p3V"))
      self.rail_val_0.setText(str(v.p5V_REF_MON))
      self.rail_val_1.setText(str(v.n36V_MON_BUF))
      self.rail_val_2.setText(str(v.p5V_ANA_MON))
      self.rail_val_3.setText(str(v.pV_ANA_MON))
      self.rail_val_4.setText(str(v.nV_ANA_MON_BUF))
      self.rail_val_5.setText(str(v.p5V_MON))
      self.rail_val_6.setText(str(v.SBC_3p3V))

      self.out0.setText(str("QCL_COIL_V"))
      self.out1.setText(str("QCL_HTR_V"))
      self.out2.setText(str("PSAT_Vmon"))
      self.out_val_v_0.setText(str(v.QCL_COIL_V))
      self.out_val_v_1.setText(str(v.QCL_HTR_V))
      self.out_val_v_2.setText(str(v.PSAT_Vmon))
      self.out_val_i_0.setText(str(v.QCL_COIL_I))
      self.out_val_i_1.setText(str(v.QCL_HTR_I))
      self.out_val_i_2.setText(str(v.PSAT_Imon))
      cmd="temps\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
      self.textEdit_temp1.setText(str(100.*float(data[2+0*3])-273))
      self.textEdit_temp2.setText(str(100.*float(data[2+1*3])-273))
      self.textEdit_temp3.setText(str(100.*float(data[2+2*3])-273))
      self.textEdit_temp4.setText(str(100.*float(data[2+3*3])-273))
      self.textEdit_temp5.setText(str(100.*float(data[2+4*3])-273))
      self.textEdit_temp6.setText(str(100.*float(data[2+5*3])-273))
      self.textEdit_temp7.setText(str(100.*float(data[2+6*3])-273))
      self.textEdit_temp8.setText(str(100.*float(data[2+7*3])-273))

      cmd="psat\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.textEdit_psatv.setText(str(float(data[2])))
      self.textEdit_psati.setText(str(float(data[5])))
      self.spin_psat_dac.setValue(int(data[8]))

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

      cmd="qcl 1\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.spin_qcl1_dac.setValue(int(data[5]))
      cmd="qcl 2\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.spin_qcl2_dac.setValue(int(data[5]))
      cmd="qcl 3\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.spin_qcl3_dac.setValue(int(data[5]))

      cmd="mult\r"
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
      self.serverResponse.setText(str(data))
      self.textEdit_7.setText(str(data[3]))
      self.textEdit_8.setText(str(data[6]))
      self.spin_bias1_dac.setValue(int(data[9]))
      self.textEdit_9.setText(str(data[13]))
      self.textEdit_10.setText(str(data[16]))
      self.spin_bias2_dac.setValue(int(data[19]))
      self.textEdit_11.setText(str(data[23]))
      self.textEdit_12.setText(str(data[26]))
      self.spin_bias3_dac.setValue(int(data[29]))


    ### PID AMP TAB ###
    def btn_pidmonitor_clicked(self, enabled):
      if enabled:
        cmd = "pid a monitor\r"
        global x
        global y1
        global y2
        global y3
        x = np.arange(0,60)
        y1 = np.zeros(60)
        y2 = np.zeros(60)
        y3 = np.zeros(60)
        #self.timer1.start()
      else:
        cmd = "q\r"
        #self.timer1.stop()
      Ser.write(cmd.encode())

    def update_pidkp(self):
      value = self.spin_pidkp.value()
      cmd="pid a kp %.1f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_3.setText(str(data))

    def update_pidki(self):
      value = self.spin_pidki.value()
      cmd="pid a ki %.1f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_3.setText(str(data))

    def update_pidkd(self):
      value = self.spin_pidkd.value()
      cmd="pid a kd %.4f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_3.setText(str(data))

    def update_pidsp(self):
      value = self.spin_pidsp.value()
      cmd="pid a sp %.1f\r" % (float(value))
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_3.setText(str(data))


################## FRQUENCY PID #######################
    def btn_pidmonitor_2_clicked(self, enabled):
      if enabled:
        cmd = "pid a monitor\r"
        global x2
        global y21
        global y22
        global y23
        x2 = np.arange(0,60)
        y21 = np.zeros(60)
        y22 = np.zeros(60)
        y23 = np.zeros(60)
        #self.timer3.start()
      else:
        cmd = "q\r"
        #self.timer3.stop()
      Ser.write(cmd.encode())

    def update_pidkp_2(self):
      value = self.spin_pidkp_2.value()
      cmd="pid f kp %.1f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_4.setText(str(data))

    def update_pidki_2(self):
      value = self.spin_pidki_2.value()
      cmd="pid f ki %.1f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_4.setText(str(data))

    def update_pidkd_2(self):
      value = self.spin_pidkd_2.value()
      cmd="pid f kd %.4f\r" % (value)
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_4.setText(str(data))

    def update_pidsp_2(self):
      value = self.spin_pidsp_2.value()
      cmd="pid f sp %.3f\r" % (float(value))
      Ser.write(cmd.encode())
      data=coreSERIAL.read_end(Ser, '\n').split()
      self.serverResponse_4.setText(str(data))

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
