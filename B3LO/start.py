import sys
import time
import serial
import string
import datetime as dt
import numpy as np
import matplotlib
from sys import argv, exit
from io import StringIO
from collections import namedtuple

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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

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

        ### PLOTS ###
        self.xdata = list(range(60))
        self.ydata1 = [float(0.) for i in range(60)]
        self.ydata2 = [float(0.) for i in range(60)]
        self.ydata3 = [float(0.) for i in range(60)]
        self._plot_ref1 = None
        self._plot_ref2 = None
        self._plot_ref3 = None
        self.show()

        ### TIMERS ###

        self.timer1 = QtCore.QTimer()               #Timer for pid a monitor
        self.timer1.setInterval(25)
        self.timer1.timeout.connect(self.update_aplot)

        self.timer2 = QtCore.QTimer()               #Timer for pid f monitor
        self.timer2.setInterval(25)
        self.timer2.timeout.connect(self.update_fplot)

    @QtCore.pyqtSlot()
    def update_aplot(self):
      data = coreSERIAL.read_end(Ser, '\n').split()
      if(str(data[0])=="pidmon"):
        self.ydata1 = self.ydata1[1:] + [float(data[2])]        #Setpoint
        self.ydata2 = self.ydata2[1:] + [float(data[3])]        #Input
        self.ydata3 = self.ydata3[1:] + [float(data[4])]        #Output
        self.textEdit_4.setText(str(data[2]))
        self.textEdit_5.setText(str(data[3]))
        self.textEdit_6.setText(str(data[4]))
      if self._plot_ref1 is None:
        plot_refs1 = self.mpl.canvas.ax.plot(self.xdata, self.ydata1, 'blue')
        plot_refs2 = self.mpl.canvas.ax.plot(self.xdata, self.ydata2, 'orange')
        self.mpl.canvas.ax.set_xlim(xmin=0, xmax=60)
        self.mpl.canvas.ax.set_ylim(ymin=20., ymax=40.)

        self.mpl.canvas.ax2 = self.mpl.canvas.ax.twinx()

        plot_refs3 = self.mpl.canvas.ax2.plot(self.xdata, self.ydata3, 'green')
        self.mpl.canvas.ax2.set_xlim(xmin=0, xmax=60)
        self.mpl.canvas.ax2.set_ylim(ymin=30300, ymax=35200)
        self._plot_ref1 = plot_refs1[0]
        self._plot_ref2 = plot_refs2[0]
        self._plot_ref3 = plot_refs3[0]
      else:
        self._plot_ref1.set_ydata(self.ydata1)
        self._plot_ref2.set_ydata(self.ydata2)
        self._plot_ref3.set_ydata(self.ydata3)
      self.mpl.canvas.draw()

    @QtCore.pyqtSlot()
    def update_fplot(self):
      data = coreSERIAL.read_end(Ser, '\n').split()
      if(str(data[0])=="pidmon"):
        self.ydata1 = self.ydata1[1:] + [float(data[2])]        #Setpoint
        self.ydata2 = self.ydata2[1:] + [float(data[3])]        #Input
        self.ydata3 = self.ydata3[1:] + [float(data[4])]        #Output
        self.textEdit_1.setText(str(data[2]))
        self.textEdit_2.setText(str(data[3]))
        self.textEdit_3.setText(str(data[4]))
      if self._plot_ref1 is None:
        plot_refs1 = self.mpl_2.canvas.ax.plot(self.xdata, self.ydata1, 'blue')
        plot_refs2 = self.mpl_2.canvas.ax.plot(self.xdata, self.ydata2, 'orange')
        self.mpl_2.canvas.ax.set_xlim(xmin=0, xmax=60)
        self.mpl_2.canvas.ax.set_ylim(ymin=-0.2, ymax=0.2)

        self.mpl_2.canvas.ax2 = self.mpl_2.canvas.ax.twinx()

        plot_refs3 = self.mpl_2.canvas.ax2.plot(self.xdata, self.ydata3, 'green')
        self.mpl_2.canvas.ax2.set_xlim(xmin=0, xmax=60)
        self.mpl_2.canvas.ax2.set_ylim(ymin=0, ymax=60)
        self._plot_ref1 = plot_refs1[0]
        self._plot_ref2 = plot_refs2[0]
        self._plot_ref3 = plot_refs3[0]
      else:
        self._plot_ref1.set_ydata(self.ydata1)
        self._plot_ref2.set_ydata(self.ydata2)
        self._plot_ref3.set_ydata(self.ydata3)
      self.mpl_2.canvas.draw()

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
        self.serverResponse_4.setText(str(data))

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
        self.mult1_vmon.setText(str(Vmon))
        self.mult1_imon.setText(str(Imon))

    def update_multbias2(self):
        value = self.spin_bias2_dac.value()
        cmd="mult 2 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.mult2_vmon.setText(str(Vmon))
        self.mult2_imon.setText(str(Imon))

    def update_multbias3(self):
        value = self.spin_bias3_dac.value()
        cmd="mult 3 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.mult3_vmon.setText(str(Vmon))
        self.mult3_imon.setText(str(Imon))

    def update_qclbias1(self):
        value = self.spin_qcl1_dac.value()
        cmd="qcl 1 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        Vs  =float(data[10])
        self.qcl1_vmon.setText(str(Vmon))
        self.qcl1_imon.setText(str(Imon))
        self.qcl1_vsen.setText(str(Vs))

    def update_qclbias2(self):
        value = self.spin_qcl2_dac.value()
        cmd="qcl 2 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        Vs  =float(data[10])
        self.qcl2_vmon.setText(str(Vmon))
        self.qcl2_imon.setText(str(Imon))
        self.qcl2_vsen.setText(str(Vs))

    def update_qclbias3(self):
        value = self.spin_qcl3_dac.value()
        cmd="qcl 3 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        Vs  =float(data[10])
        self.qcl3_vmon.setText(str(Vmon))
        self.qcl3_imon.setText(str(Imon))
        self.qcl3_vsen.setText(str(Vs))

    def update_psat(self):
        value = self.spin_psat_dac.value()
        cmd = "psat %d\r" % (value)
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n', 2).split()
        self.serverResponse.setText(str(data))
        self.psatv.setText(str(float(data[5])))
        self.psati.setText(str(float(data[8])))

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
        self.qcl1_vmon.setText( str(float(data[3])))   #QCL 1 V
        self.qcl1_imon.setText( str(float(data[6])))   #QCL 1 I
        self.qcl1_vsen.setText(str(float(data[9])))   #QCL 1 Vsense
        self.qcl2_vmon.setText( str(float(data[13])))  #QCL 2 V
        self.qcl2_imon.setText( str(float(data[16])))  #QCL 2 I
        self.qcl2_vsen.setText(str(float(data[19])))  #QCL 2 Vsense
        self.qcl3_vmon.setText( str(float(data[23])))  #QCL 3 V
        self.qcl3_imon.setText( str(float(data[26])))  #QCL 3 I
        self.qcl3_vsen.setText(str(float(data[29])))  #QCL 3 Vsense

    def update_voicecoil(self):
        value = self.spin_voicecoil.value()
        cmd = "coil %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        self.vcoil_I.setText(str(float(data[2])))

    def btn_open_clicked(self):
        global Ser
        Ser = serial.Serial(
            #port='/Users/young/dev/vmodem2',
            port='/dev/cu.usbmodemB3LO_CTRL1',
            baudrate=115200,
            timeout=1
        )

    def btn_close_clicked(self):
        global Ser
        Ser.close()
        Ser = 0

    def sendcmd(self):
        cmd= "%s\r" % self.serverCommand.text()
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
        cmd= "%s\r" % self.serverCommand_4.text()
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_4.setText(str(data))
        self.serverCommand_4.setText("")

    def btn_refresh_clicked(self):

        # GET DATA
        cmd="status slow\r"
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
        N=68*2

        # translate +/- to p/n
        datan=[None]*N
        trantab = str.maketrans("+-.","pnp")
        for i in range(0,N,2):
            datan[i]=str(data[i]).translate(trantab)
            datan[i+1]=data[i+1]

        #define template named tuple
        Volts = namedtuple('Volts', datan[::2])

        #fill the tuple with data
        v = Volts._make(datan[1::2])

        self.rail_val_0.setText(str(v.p5V_REF_MON))
        self.rail_val_1.setText(str(v.n36V_MON_BUF))
        self.rail_val_2.setText(str(v.p5V_ANA_MON))
        self.rail_val_3.setText(str(v.pV_ANA_MON))
        self.rail_val_4.setText(str(v.nV_ANA_MON_BUF))
        self.rail_val_5.setText(str(v.p5V_MON))
        self.rail_val_6.setText(str(v.SBC_3p3V))

        self.out_val_v_0.setText(str(v.QCL_COIL_V))
        self.out_val_v_1.setText(str(v.QCL_HTR_V))
        self.out_val_v_2.setText(str(v.PSAT_Vmon))
        self.out_val_i_0.setText(str(v.QCL_COIL_I))
        self.out_val_i_1.setText(str(v.QCL_HTR_I))
        self.out_val_i_2.setText(str(v.PSAT_Imon))

        self.temp1.setText(str(v.B3_AD590_0))
        self.temp2.setText(str(v.B3_AD590_1))
        self.temp3.setText(str(v.B3_AD590_2))
        self.temp4.setText(str(v.B3_AD590_3))
        self.temp5.setText(str(v.B3_AD590_4))
        self.temp6.setText(str(v.B3_AD590_5))
        self.temp7.setText(str(v.B3_AD590_6))
        self.temp8.setText(str(v.B3_AD590_7))

        self.psatv.setText(str(v.B3_PSatV))
        self.psati.setText(str(v.B3_PSatV))
        self.spin_psat_dac.setValue(int(v.B3_PSatDac))

        self.qcl1_vmon.setText(str(v.QCL1_Vout))
        self.qcl1_imon.setText(str(v.QCL1_Imon))
        self.qcl1_vsen.setText(str(v.QCL1_Vsen))
        self.spin_qcl1_dac.setValue(int(v.QCL1_DAC))
        self.qcl2_vmon.setText(str(v.QCL2_Vout))
        self.qcl2_imon.setText(str(v.QCL2_Imon))
        self.qcl2_vsen.setText(str(v.QCL2_Vsen))
        self.spin_qcl2_dac.setValue(int(v.QCL2_DAC))
        self.qcl3_vmon.setText(str(v.QCL3_Vout))
        self.qcl3_imon.setText(str(v.QCL3_Imon))
        self.qcl3_vsen.setText(str(v.QCL3_Vsen))
        self.spin_qcl3_dac.setValue(int(v.QCL3_DAC))

        self.mult1_vmon.setText(str(v.B3_MULT1_V))
        self.mult1_imon.setText(str(v.B3_MULT1_I))
        self.spin_bias1_dac.setValue(int(v.B3_MULT1_bits))
        self.mult2_vmon.setText(str(v.B3_MULT2_V))
        self.mult2_imon.setText(str(v.B3_MULT2_I))
        self.spin_bias2_dac.setValue(int(v.B3_MULT2_bits))
        self.mult3_vmon.setText(str(v.B3_MULT3_V))
        self.mult3_imon.setText(str(v.B3_MULT3_I))
        self.spin_bias3_dac.setValue(int(v.B3_MULT3_bits))


    ### PID AMP TAB ###
    def btn_pidmonitor_clicked(self, enabled):
        if enabled:
            cmd = "pid a monitor\r"
            Ser.write(cmd.encode())
            self.timer1.start()
        else:
            cmd = "q\r"
            Ser.write(cmd.encode())
            data=coreSERIAL.read_end(Ser, '\n').split()
            self.serverResponse_3.setText(str(data))
            cmd = "\r"
            Ser.write(cmd.encode())
            self.timer1.stop()

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
            cmd = "pid f monitor\r"
            Ser.write(cmd.encode())
            self.timer2.start()
        else:
            cmd = "q\r"
            Ser.write(cmd.encode())
            data=coreSERIAL.read_end(Ser, '\n').split()
            self.serverResponse_4.setText(str(data))
            cmd = "\r"
            Ser.write(cmd.encode())
            self.timer2.stop()

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
