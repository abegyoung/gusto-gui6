import sys
import time
import serial
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
isB2=0
pixel=1

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self.setupUi(self)


        ### SIGNALS AND SLOTS ###

        #Comm
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_open.clicked.connect(self.btn_open_clicked)
        self.serverCommand.returnPressed.connect(self.sendcmd)       #main tab
        self.serverCommand_2.returnPressed.connect(self.sendcmd_2) #pid tab
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)

        #DAC spin buttons
        self.spinBox_01.valueChanged.connect(self.update_spin1_1)
        self.spinBox_02.valueChanged.connect(self.update_spin1_2)
        self.spinBox_03.valueChanged.connect(self.update_spin1_3)
        self.spinBox_04.valueChanged.connect(self.update_spin1_4)
        self.spinBox_05.valueChanged.connect(self.update_spin1_5)
        self.spinBox_06.valueChanged.connect(self.update_spin1_6)
        self.spinBox_07.valueChanged.connect(self.update_spin1_7)
        self.spinBox_08.valueChanged.connect(self.update_spin1_8)
        self.spinBox_09.valueChanged.connect(self.update_spin2_1)
        self.spinBox_10.valueChanged.connect(self.update_spin2_2)
        self.spinBox_11.valueChanged.connect(self.update_spin2_3)
        self.spinBox_12.valueChanged.connect(self.update_spin2_4)
        self.spinBox_13.valueChanged.connect(self.update_spin2_5)
        self.spinBox_14.valueChanged.connect(self.update_spin2_6)
        self.spinBox_15.valueChanged.connect(self.update_spin2_7)
        self.spinBox_16.valueChanged.connect(self.update_spin2_8)
        self.spinBox_17.valueChanged.connect(self.update_spin3_1)
        self.spinBox_18.valueChanged.connect(self.update_spin3_2)
        self.spinBox_19.valueChanged.connect(self.update_spin3_3)
        self.spinBox_20.valueChanged.connect(self.update_spin3_4)
        self.spinBox_21.valueChanged.connect(self.update_spin3_5)
        self.spinBox_22.valueChanged.connect(self.update_spin3_6)
        self.spinBox_23.valueChanged.connect(self.update_spin3_7)
        self.spinBox_24.valueChanged.connect(self.update_spin3_8)

        #PCA9502
        self.dcdc1.toggled.connect(self.btn_dcdc1_clicked)
        self.dcdc2.toggled.connect(self.btn_dcdc2_clicked)
        self.dcdc3.toggled.connect(self.btn_dcdc3_clicked)
        self.dcdc4.toggled.connect(self.btn_dcdc4_clicked)
        self.dcdc5.toggled.connect(self.btn_dcdc5_clicked)
        self.dcdc6.toggled.connect(self.btn_dcdc6_clicked)
        self.dcdc7.toggled.connect(self.btn_dcdc7_clicked)
        self.dcdc8.toggled.connect(self.btn_dcdc8_clicked)

        #PSAT Disables
        self.disa1.toggled.connect(self.btn_disa1_clicked)
        self.disa2.toggled.connect(self.btn_disa2_clicked)
        self.disa3.toggled.connect(self.btn_disa3_clicked)
        self.disa4.toggled.connect(self.btn_disa4_clicked)
        self.disa5.toggled.connect(self.btn_disa5_clicked)
        self.disa6.toggled.connect(self.btn_disa6_clicked)
        self.disa7.toggled.connect(self.btn_disa7_clicked)
        self.disa8.toggled.connect(self.btn_disa8_clicked)

        #PSAT Control
        self.spin_psat_dac_1.valueChanged.connect(self.update_psat_1)
        self.spin_psat_dac_2.valueChanged.connect(self.update_psat_2)
        self.spin_psat_dac_3.valueChanged.connect(self.update_psat_3)
        self.spin_psat_dac_4.valueChanged.connect(self.update_psat_4)
        self.spin_psat_dac_5.valueChanged.connect(self.update_psat_5)
        self.spin_psat_dac_6.valueChanged.connect(self.update_psat_6)
        self.spin_psat_dac_7.valueChanged.connect(self.update_psat_7)
        self.spin_psat_dac_8.valueChanged.connect(self.update_psat_8)

        #PID pixel control
        self.pixelButton_1.toggled.connect(self.pixelButton_1_clicked)
        self.pixelButton_2.toggled.connect(self.pixelButton_2_clicked)
        self.pixelButton_3.toggled.connect(self.pixelButton_3_clicked)
        self.pixelButton_4.toggled.connect(self.pixelButton_4_clicked)
        self.pixelButton_5.toggled.connect(self.pixelButton_5_clicked)
        self.pixelButton_6.toggled.connect(self.pixelButton_6_clicked)
        self.pixelButton_7.toggled.connect(self.pixelButton_7_clicked)
        self.pixelButton_8.toggled.connect(self.pixelButton_8_clicked)

        #PID gain control
        self.spin_pidsetpoint.valueChanged.connect(self.update_pid)
        self.spin_pidkp.valueChanged.connect(self.update_pidKp)
        self.spin_pidki.valueChanged.connect(self.update_pidKi)
        self.spin_pidkd.valueChanged.connect(self.update_pidKd)

        #PID monitor and toggle
        self.btn_pidmonitor.toggled.connect(self.pidmonitor_clicked)
        self.btn_pidtoggle.toggled.connect(self.pidtoggle_clicked)

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

        self.timer = QtCore.QTimer()               #Timer for pid a monitor
        self.timer.setInterval(25)
        self.timer.timeout.connect(self.update_plot)

    @QtCore.pyqtSlot()
    def update_plot(self):
      data = coreSERIAL.read_end(Ser, '\n').split()
      if(str(data[0])=="pidmon"):
        self.ydata1 = self.ydata1[1:] + [float(data[3])]        #Setpoint
        self.ydata2 = self.ydata2[1:] + [float(data[4])]        #Input
        self.ydata3 = self.ydata3[1:] + [float(data[5])]        #Output
        self.textEdit_sp.setText(str(data[3]))
        self.textEdit_pv.setText(str(data[4]))
        self.textEdit_ov.setText(str(data[5]))
      if self._plot_ref1 is None:
        plot_refs1 = self.mpl.canvas.ax.plot(self.xdata, self.ydata1, 'blue')
        plot_refs2 = self.mpl.canvas.ax.plot(self.xdata, self.ydata2, 'orange')
        self.mpl.canvas.ax.set_xlim(xmin=0, xmax=60)
        self.mpl.canvas.ax.set_ylim(ymin=20., ymax=40.)

        self.mpl.canvas.ax2 = self.mpl.canvas.ax.twinx()

        plot_refs3 = self.mpl.canvas.ax2.plot(self.xdata, self.ydata3, 'green')
        self.mpl.canvas.ax2.set_xlim(xmin=0, xmax=60)
        self.mpl.canvas.ax2.set_ylim(ymin=10000000, ymax=16777216)
        self._plot_ref1 = plot_refs1[0]
        self._plot_ref2 = plot_refs2[0]
        self._plot_ref3 = plot_refs3[0]
      else:
        self._plot_ref1.set_ydata(self.ydata1)
        self._plot_ref2.set_ydata(self.ydata2)
        self._plot_ref3.set_ydata(self.ydata3)
      self.mpl.canvas.draw()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def btn_refresh_clicked(self):

        # GET DATA
        cmd="status slow\r"
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end_multi(Ser, 'END\n').split()
        N=len(data)

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

        # Tab 1 Voltage rails
        self.textEdit_19.setText(str(v.n36V_MON_BUF))     #V36
        self.textEdit_20.setText(str(v.nSPARE_MON_BUF))   #V18
        self.textEdit_21.setText(str(v.p5V_ANA_MON))      #+5Vana
        self.textEdit_22.setText(str(v.pV_ANA_MON))       #+9Vana
        self.textEdit_23.setText(str(v.nV_ANA_MON_BUF))   #-9Vana
        self.textEdit_24.setText(str(v.p5V_ANA_MON))      #5V

        # Tab 2 Voltage rails
        self.textEdit_19c.setText(str(v.n36V_MON_BUF))     #V36
        self.textEdit_20c.setText(str(v.nSPARE_MON_BUF))   #V18
        self.textEdit_21c.setText(str(v.p5V_ANA_MON))      #+5Vana
        self.textEdit_22c.setText(str(v.pV_ANA_MON))       #+9Vana
        self.textEdit_23c.setText(str(v.nV_ANA_MON_BUF))   #-9Vana
        self.textEdit_24c.setText(str(v.p5V_REF_MON))      #5V REF
        self.textEdit_33.setText( str(v.p5V_MON))          #5V MON
        self.textEdit_25c.setText(str(v.SBC_3p3V))         #3.3V SBC 

        # Tab 2 Current rails
        self.textEdit_19c_2.setText(str(v.n36V_Imon))        #V36 current
        self.textEdit_21c_2.setText(str(v.p5V_ANA_Imon))     #+5Vana
        self.textEdit_22c_2.setText(str(v.p9V_ANA_Imon))     #+9Vana current
        self.textEdit_23c_2.setText(str(v.n9V_ANA_Imon))     #-9Vana current
        self.textEdit_26c_2.setText(str(v.p15V_Imon))        #15V synth current
        self.textEdit_27c_2.setText(str(v.p5V_SYNTH_Imon))   #5V synth current
        self.textEdit_28c_2.setText(str(v.p5V_CTRL_Imon))    #5V ctrl current


        # Iterate over QVBoxLayout items textEdit_AD590_[0-7]
        # Fill textEdit boxes using getattr() with field. Nice.
        for i in range(self.tempLayout.count()):
            field="B2_AD590_%d" % i
            self.tempLayout.itemAt(i).widget().setText(str(getattr(v, field)))

        self.textEdit_38.setText(str(v.B2_AD590_8))       #internal AD590 #1
        self.textEdit_39.setText(str(v.B2_AD590_9))       #internal AD590 #2
        self.textEdit_40.setText(str(v.B2_AD590_10))      #internal AD590 #3

        for i in range(0, 48):
          #self.multLayout.itemAt(i).widget().setText(str(i))
          if(i%2):
            field="B2_MultI_%d" % int((i+2)/2)
          else:
            field="B2_MultV_%d" % int((i+2)/2)
          self.multLayout.itemAt(i).widget().setText(str(getattr(v, field)))

        for i in range(0, 24):
          field="B2_DAC_%d" % (i+1)
          self.multLayout.itemAt(i+48).widget().blockSignals(True)
          self.multLayout.itemAt(i+48).widget().setValue(int(getattr(v, field)))
          self.multLayout.itemAt(i+48).widget().blockSignals(False)

        field="B2_dcdc_mask"
        mask=int(getattr(v, field), 2)
        for i in range(self.dcdcLayout.count()):
          self.dcdcLayout.itemAt(i).widget().blockSignals(True)
          self.dcdcLayout.itemAt(i).widget().setChecked((mask & (1<<i))>>i)
          self.dcdcLayout.itemAt(i).widget().blockSignals(False)

        self.textEdit_25.setText(str(v.B2_PSatV_1))
        self.textEdit_26.setText(str(v.B2_PSatV_2))
        self.textEdit_27.setText(str(v.B2_PSatV_3))
        self.textEdit_28.setText(str(v.B2_PSatV_4))
        self.textEdit_29.setText(str(v.B2_PSatV_5))
        self.textEdit_30.setText(str(v.B2_PSatV_6))
        self.textEdit_31.setText(str(v.B2_PSatV_7))
        self.textEdit_32.setText(str(v.B2_PSatV_8))

        self.spin_psat_dac_1.blockSignals(True)
        self.spin_psat_dac_1.setValue(int(v.B2_PSatDac_1))
        self.spin_psat_dac_1.blockSignals(False)
        self.spin_psat_dac_2.blockSignals(True)
        self.spin_psat_dac_2.setValue(int(v.B2_PSatDac_2))
        self.spin_psat_dac_2.blockSignals(False)
        self.spin_psat_dac_3.blockSignals(True)
        self.spin_psat_dac_3.setValue(int(v.B2_PSatDac_3))
        self.spin_psat_dac_3.blockSignals(False)
        self.spin_psat_dac_4.blockSignals(True)
        self.spin_psat_dac_4.setValue(int(v.B2_PSatDac_4))
        self.spin_psat_dac_4.blockSignals(False)
        self.spin_psat_dac_5.blockSignals(True)
        self.spin_psat_dac_5.setValue(int(v.B2_PSatDac_5))
        self.spin_psat_dac_5.blockSignals(False)
        self.spin_psat_dac_6.blockSignals(True)
        self.spin_psat_dac_6.setValue(int(v.B2_PSatDac_6))
        self.spin_psat_dac_6.blockSignals(False)
        self.spin_psat_dac_7.blockSignals(True)
        self.spin_psat_dac_7.setValue(int(v.B2_PSatDac_7))
        self.spin_psat_dac_7.blockSignals(False)
        self.spin_psat_dac_8.blockSignals(True)
        self.spin_psat_dac_8.setValue(int(v.B2_PSatDac_8))
        self.spin_psat_dac_8.blockSignals(False)

        self.textEdit_19d_1.setText(str(v.B2_GMONI_1))
        self.textEdit_19d_2.setText(str(v.B2_GMONI_2))
        self.textEdit_19d_3.setText(str(v.B2_GMONI_3))
        self.textEdit_19d_4.setText(str(v.B2_GMONI_4))
        self.textEdit_19d_5.setText(str(v.B2_GMONI_5))
        self.textEdit_19d_6.setText(str(v.B2_GMONI_6))
        self.textEdit_19d_7.setText(str(v.B2_GMONI_7))
        self.textEdit_19d_8.setText(str(v.B2_GMONI_8))
        self.textEdit_19d_V.setText(str(v.B2_GMONV))

        self.serverResponse.setText("Status done!")



    def update_pid(self):
        global Ser
        global pixel
        value = self.spin_pidsetpoint.value()
        cmd = "pid %d sp %f\r" % (pixel,value)
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_2.setText(str(data))

    def update_pidKp(self):
        global Ser
        global pixel
        value = self.spin_pidkp.value()
        cmd = "pid %d kp %f\r" % (pixel,value)
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_2.setText(str(data))

    def update_pidKi(self):
        global Ser
        global pixel
        value = self.spin_pidki.value()
        cmd = "pid %d ki %f\r" % (pixel,value)
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_2.setText(str(data))

    def update_pidKd(self):
        global Ser
        global pixel
        value = self.spin_pidkd.value()
        cmd = "pid %d kd %f\r" % (pixel,value)
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_2.setText(str(data))

    def pidmonitor_clicked(self, enabled):
        global pixel
        if enabled:
            cmd="pid %d monitor\r" % pixel
            Ser.write(cmd.encode())
            self.timer.start()
        else:
            cmd = "q\r"
            Ser.write(cmd.encode())
            data=coreSERIAL.read_end(Ser, '\n').split()
            self.serverResponse_2.setText(str(data))
            cmd = "\r"
            Ser.write(cmd.encode())
            self.timer.stop()

    def pidtoggle_clicked(self, enabled):
        pass

    def pixelButton_1_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 1 #CII #1

    def pixelButton_2_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 2 #CII #2

    def pixelButton_3_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 3  #NII #1

    def pixelButton_4_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 4  #NII #2

    def pixelButton_5_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 5 #CII #1

    def pixelButton_6_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 6 #CII #2

    def pixelButton_7_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 7  #NII #1

    def pixelButton_8_clicked(self, enabled):
        if enabled:
            global pixel
            pixel = 8  #NII #2

    def btn_open_clicked(self):
        global Ser
        Ser = serial.Serial(
            #port='/dev/ttyACM0',
            port='/dev/cu.usbmodemB2LO_CTRL1',
            baudrate=115200,
            timeout=1
        )
        cmd="id\r"
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n')
        isB2=int(data[16])

    def btn_close_clicked(self):
        global Ser
        Ser.close()
        Ser = 0

    #command window main tab
    def sendcmd(self):
        global Ser
        cmd= "%s\r" % self.serverCommand.text()
        Ser.write(cmd.encode())
        if (cmd.split()[0] == "help"):
            data=coreSERIAL.read_end_multi(Ser, 'END').split()
        else:
            data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse.setText(str(data))
        self.serverCommand.setText("")

    #command window pid tab
    def sendcmd_2(self):
        global Ser
        cmd= "%s\r" % self.serverCommand_2.text()
        Ser.write(cmd.encode())
        if (cmd.split()[0] == "help"):
            data=coreSERIAL.read_end_multi(Ser, 'END').split()
        else:
            data=coreSERIAL.read_end(Ser, '\n')
        self.serverResponse_2.setText(str(data))
        self.serverCommand_2.setText("")

    def update_spin1_1(self):
        global Ser
        value = self.spinBox_01.value()
        cmd="mult 1 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix1_Stg1_Vmon.setText(str(Vmon))
        self.Pix1_Stg1_Imon.setText(str(Imon))

    def update_spin1_2(self):
        global Ser
        value = self.spinBox_02.value()
        cmd="mult 2 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix2_Stg1_Vmon.setText(str(Vmon))
        self.Pix2_Stg1_Imon.setText(str(Imon))

    def update_spin1_3(self):
        global Ser
        value = self.spinBox_03.value()
        cmd="mult 3 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix3_Stg1_Vmon.setText(str(Vmon))
        self.Pix3_Stg1_Imon.setText(str(Imon))

    def update_spin1_4(self):
        global Ser
        value = self.spinBox_04.value()
        cmd="mult 4 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix4_Stg1_Vmon.setText(str(Vmon))
        self.Pix4_Stg1_Imon.setText(str(Imon))

    def update_spin1_5(self):
        global Ser
        value = self.spinBox_05.value()
        cmd="mult 5 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix5_Stg1_Vmon.setText(str(Vmon))
        self.Pix5_Stg1_Imon.setText(str(Imon))

    def update_spin1_6(self):
        global Ser
        value = self.spinBox_06.value()
        cmd="mult 6 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix6_Stg1_Vmon.setText(str(Vmon))
        self.Pix6_Stg1_Imon.setText(str(Imon))

    def update_spin1_7(self):
        global Ser
        value = self.spinBox_07.value()
        cmd="mult 7 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix7_Stg1_Vmon.setText(str(Vmon))
        self.Pix7_Stg1_Imon.setText(str(Imon))

    def update_spin1_8(self):
        global Ser
        value = self.spinBox_08.value()
        cmd="mult 8 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix8_Stg1_Vmon.setText(str(Vmon))
        self.Pix8_Stg1_Imon.setText(str(Imon))

    def update_spin2_1(self):
        global Ser
        value = self.spinBox_09.value()
        cmd="mult 9 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix1_Stg2_Vmon.setText(str(Vmon))
        self.Pix1_Stg2_Imon.setText(str(Imon))

    def update_spin2_2(self):
        global Ser
        value = self.spinBox_10.value()
        cmd="mult 10 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix2_Stg2_Vmon.setText(str(Vmon))
        self.Pix2_Stg2_Imon.setText(str(Imon))

    def update_spin2_3(self):
        global Ser
        value = self.spinBox_11.value()
        cmd="mult 11 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix3_Stg2_Vmon.setText(str(Vmon))
        self.Pix3_Stg2_Imon.setText(str(Imon))

    def update_spin2_4(self):
        global Ser
        value = self.spinBox_12.value()
        cmd="mult 12 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix4_Stg2_Vmon.setText(str(Vmon))
        self.Pix4_Stg2_Imon.setText(str(Imon))

    def update_spin2_5(self):
        global Ser
        value = self.spinBox_13.value()
        cmd="mult 13 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix5_Stg2_Vmon.setText(str(Vmon))
        self.Pix5_Stg2_Imon.setText(str(Imon))

    def update_spin2_6(self):
        global Ser
        value = self.spinBox_14.value()
        cmd="mult 14 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix6_Stg2_Vmon.setText(str(Vmon))
        self.Pix6_Stg2_Imon.setText(str(Imon))

    def update_spin2_7(self):
        global Ser
        value = self.spinBox_15.value()
        cmd="mult 15 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix7_Stg2_Vmon.setText(str(Vmon))
        self.Pix7_Stg2_Imon.setText(str(Imon))

    def update_spin2_8(self):
        global Ser
        value = self.spinBox_16.value()
        cmd="mult 16 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix8_Stg2_Vmon.setText(str(Vmon))
        self.Pix8_Stg2_Imon.setText(str(Imon))

    def update_spin3_1(self):
        global Ser
        value = self.spinBox_17.value()
        cmd="mult 17 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix1_Stg3_Vmon.setText(str(Vmon))
        self.Pix1_Stg3_Imon.setText(str(Imon))

    def update_spin3_2(self):
        global Ser
        value = self.spinBox_18.value()
        cmd="mult 18 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix2_Stg3_Vmon.setText(str(Vmon))
        self.Pix2_Stg3_Imon.setText(str(Imon))

    def update_spin3_3(self):
        global Ser
        value = self.spinBox_19.value()
        cmd="mult 19 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix3_Stg3_Vmon.setText(str(Vmon))
        self.Pix3_Stg3_Imon.setText(str(Imon))

    def update_spin3_4(self):
        global Ser
        value = self.spinBox_20.value()
        cmd="mult 20 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix4_Stg3_Vmon.setText(str(Vmon))
        self.Pix4_Stg3_Imon.setText(str(Imon))

    def update_spin3_5(self):
        global Ser
        value = self.spinBox_21.value()
        cmd="mult 21 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix5_Stg3_Vmon.setText(str(Vmon))
        self.Pix5_Stg3_Imon.setText(str(Imon))

    def update_spin3_6(self):
        global Ser
        value = self.spinBox_22.value()
        cmd="mult 22 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix6_Stg3_Vmon.setText(str(Vmon))
        self.Pix6_Stg3_Imon.setText(str(Imon))

    def update_spin3_7(self):
        global Ser
        value = self.spinBox_23.value()
        cmd="mult 23 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix7_Stg3_Vmon.setText(str(Vmon))
        self.Pix7_Stg3_Imon.setText(str(Imon))

    def update_spin3_8(self):
        global Ser
        value = self.spinBox_24.value()
        cmd="mult 24 %d\r" % value
        Ser.write(cmd.encode())
        data=coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        Vmon=float(data[3])
        Imon=float(data[6])
        self.Pix8_Stg3_Vmon.setText(str(Vmon))
        self.Pix8_Stg3_Imon.setText(str(Imon))




    def update_psat_1(self):
        global Ser
        value = self.spin_psat_dac_1.value()
        cmd = "psat %d %d\r" % (1, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 1
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_25.setText(str(volt))

    def update_psat_2(self):
        global Ser
        value = self.spin_psat_dac_2.value()
        cmd = "psat %d %d\r" % (2, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 2
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_26.setText(str(volt))

    def update_psat_3(self):
        global Ser
        value = self.spin_psat_dac_3.value()
        cmd = "psat %d %d\r" % (3, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 3
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_27.setText(str(volt))

    def update_psat_4(self):
        global Ser
        value = self.spin_psat_dac_4.value()
        cmd = "psat %d %d\r" % (4, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 4
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_28.setText(str(volt))

    def update_psat_5(self):
        global Ser
        value = self.spin_psat_dac_5.value()
        cmd = "psat %d %d\r" % (5, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 5
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_29.setText(str(volt))

    def update_psat_6(self):
        global Ser
        value = self.spin_psat_dac_6.value()
        cmd = "psat %d %d\r" % (6, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 6
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_30.setText(str(volt))

    def update_psat_7(self):
        global Ser
        value = self.spin_psat_dac_7.value()
        cmd = "psat %d %d\r" % (7, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 7
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_31.setText(str(volt))

    def update_psat_8(self):
        global Ser
        value = self.spin_psat_dac_8.value()
        cmd = "psat %d %d\r" % (8, value)
        Ser.write(cmd.encode())
        cmd = "pmon %d\r" % 8
        Ser.write(cmd.encode())
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_32.setText(str(volt))

    def btn_dcdc1_clicked(self, enabled):
        global Ser
        ch=1
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc2_clicked(self, enabled):
        global Ser
        ch=2
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc3_clicked(self, enabled):
        global Ser
        ch=3
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc4_clicked(self, enabled):
        global Ser
        ch=4
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc5_clicked(self, enabled):
        global Ser
        ch=5
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc6_clicked(self, enabled):
        global Ser
        ch=6
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc7_clicked(self, enabled):
        global Ser
        ch=7
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_dcdc8_clicked(self, enabled):
        global Ser
        ch=8
        cmd="dcdc %d 0\r" % ch
        if enabled:
            cmd="dcdc %d 1\r" % ch
        Ser.write(cmd.encode())                             #Send dcdc command
        data=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(data))

    def btn_disa1_clicked(self, enabled):
        global Ser
        ch=1
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_25.setText(str(volt))

    def btn_disa2_clicked(self, enabled):
        global Ser
        ch=2
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_26.setText(str(volt))

    def btn_disa3_clicked(self, enabled):
        global Ser
        ch=3
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_27.setText(str(volt))

    def btn_disa4_clicked(self, enabled):
        global Ser
        ch=4
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_28.setText(str(volt))

    def btn_disa5_clicked(self, enabled):
        global Ser
        ch=5
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_29.setText(str(volt))

    def btn_disa6_clicked(self, enabled):
        global Ser
        ch=6
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_30.setText(str(volt))

    def btn_disa7_clicked(self, enabled):
        global Ser
        ch=7
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_31.setText(str(volt))

    def btn_disa8_clicked(self, enabled):
        global Ser
        ch=8
        cmd="disable %d 1\r" % ch
        if enabled:
            cmd="disable %d 0\r" % ch
        Ser.write(cmd.encode())                             #Send disable command
        return1=coreSERIAL.read_end(Ser,'\n')
        self.serverResponse.setText(str(return1))
        time.sleep(.1)
        cmd = "pmon %d\r" % ch
        Ser.write(cmd.encode())                             #Read psat Voltage
        data = coreSERIAL.read_end(Ser, '\n').split()
        self.serverResponse.setText(str(data))
        volt = data[3]
        amps = data[5]
        self.textEdit_32.setText(str(volt))

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
