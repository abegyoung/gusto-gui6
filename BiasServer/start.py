#!/opt/local/bin/python2.7
import sys
import time
import socket
import datetime as dt
import numpy as np
from string import split
from StringIO import StringIO
from PyQt4 import QtCore, QtGui, uic

sport = 9001
serverip = '192.168.0.211'

import QLed
from sys import argv, exit
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QWidget, QPainter, QGridLayout, QSizePolicy, QStyleOption
from PyQt4.QtCore import pyqtSignal, Qt, QSize, QTimer, QByteArray, QRectF, pyqtProperty
from PyQt4.QtSvg import QSvgRenderer
from colorsys import rgb_to_hls, hls_to_rgb

execfile('QLedInclude.py')

from PyQt4.Qwt5.qplt import *

form_class = uic.loadUiType("mainwindow.ui")[0]

s=0
biasold=32768
pixel=1

numPoints = 80
start = 20000
stop = 45000

VOffset=-.35
VOffset_1=-.35
VOffset_2=-.35
VOffset_3=-.35
VOffset_4=-.35
VOffset_5=-.35
VOffset_6=-.35
VOffset_7=-.35
VOffset_8=-.35

def recv_end(the_socket, End):
   total_data=[];data=''
   while True:
      try:
         data=the_socket.recv(8192)
      except:
         break
      if End in data:
         total_data.append(data[:data.find(End)])
         break
      total_data.append(data)
      if len(total_data)>1:
         #check if end_of_data was split
         last_pair=total_data[-2]+total_data[-1]
         if End in last_pair:
            total_data[-2]=last_pair[:last_pair.find(End)]
            total_data.pop()
            break
   return ''.join(total_data)

class MyWindowClass(QtGui.QMainWindow, form_class):
   def __init__(self, parent=None):
      QtGui.QWidget.__init__(self, parent)
      self.setupUi(self)

      self.btn_zeropots.clicked.connect(self.btn_zeropots_clicked)      #OK
      self.btn_setbias.clicked.connect(self.btn_setbias_clicked)        #OK
      self.spinVoltage.connect(self.spinVoltage, SIGNAL("valueChanged(int)"),self.btn_setbias_clicked)
      self.spinLNA.connect(self.spinLNA, SIGNAL("valueChanged(int)"),self.update_LNA)
      self.btn_sweep.clicked.connect(self.btn_sweep_clicked)
      self.pid1.toggled.connect(self.btn_pid1_clicked)
      self.pid2.toggled.connect(self.btn_pid2_clicked)
      self.pid3.toggled.connect(self.btn_pid3_clicked)
      self.pid4.toggled.connect(self.btn_pid4_clicked)
      self.relayButton.toggled.connect(self.relayButton_clicked)
      self.vmodeButton.toggled.connect(self.vmodeButton_clicked)
      self.spinSV1.connect(self.spinSV1, SIGNAL("valueChanged(double)"),self.update_pidSV1)
      self.spinSV2.connect(self.spinSV2, SIGNAL("valueChanged(double)"),self.update_pidSV2)
      self.spinSV3.connect(self.spinSV3, SIGNAL("valueChanged(double)"),self.update_pidSV3)
      self.spinSV4.connect(self.spinSV4, SIGNAL("valueChanged(double)"),self.update_pidSV4)
      self.spinDC1.connect(self.spinDC1, SIGNAL("valueChanged(double)"),self.update_pidDC1)
      self.spinDC2.connect(self.spinDC2, SIGNAL("valueChanged(double)"),self.update_pidDC2)
      self.spinDC3.connect(self.spinDC3, SIGNAL("valueChanged(double)"),self.update_pidDC3)
      self.spinDC4.connect(self.spinDC4, SIGNAL("valueChanged(double)"),self.update_pidDC4)

      self.spindV_1.connect(self.spindV_1, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_2.connect(self.spindV_2, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_3.connect(self.spindV_3, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_4.connect(self.spindV_4, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_5.connect(self.spindV_5, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_6.connect(self.spindV_6, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_7.connect(self.spindV_7, SIGNAL("valueChanged(double)"),self.update_spindV)
      self.spindV_8.connect(self.spindV_8, SIGNAL("valueChanged(double)"),self.update_spindV)

      self.spinnumSweep.connect(self.spinnumSweep, SIGNAL("valueChanged(int)"),self.update_sweepnum)
      self.sweepstart.connect(self.sweepstart, SIGNAL("valueChanged(int)"),self.update_sweepstart)
      self.sweepstop.connect(self.sweepstop, SIGNAL("valueChanged(int)"),self.update_sweepstop)
      
      self.pixelButton_1.toggled.connect(self.pixelButton_1_clicked)
      self.pixelButton_2.toggled.connect(self.pixelButton_2_clicked)
      self.pixelButton_3.toggled.connect(self.pixelButton_3_clicked)
      self.pixelButton_4.toggled.connect(self.pixelButton_4_clicked)
      self.pixelButton_5.toggled.connect(self.pixelButton_5_clicked)
      self.pixelButton_6.toggled.connect(self.pixelButton_6_clicked)
      self.pixelButton_7.toggled.connect(self.pixelButton_7_clicked)
      self.pixelButton_8.toggled.connect(self.pixelButton_8_clicked)
      self.btn_close.clicked.connect(self.btn_close_clicked)
      self.btn_open.clicked.connect(self.btn_open_clicked)
      self.serverCommand.connect(self.serverCommand, SIGNAL("returnPressed(void)"), self.sendcmd)

      self.ipAddress.connect(self.ipAddress, SIGNAL("returnPressed(void)"), self.updateIP)
      self.TCPport.connect(self.TCPport, SIGNAL("returnPressed(void)"), self.updatePORT)

      self.dcbias1.toggled.connect(self.btn_dcbias1_clicked)
      self.dcbias2.toggled.connect(self.btn_dcbias2_clicked)
      self.dcdc1.toggled.connect(self.btn_dcdc1_clicked)
      self.dcdc2.toggled.connect(self.btn_dcdc2_clicked)
      self.dcdc3.toggled.connect(self.btn_dcdc3_clicked)
      self.dcdc4.toggled.connect(self.btn_dcdc4_clicked)
      self.dcdc5.toggled.connect(self.btn_dcdc5_clicked)
      #self.updateDCDC.clicked.connect(self.updateDCDC_clicked)

      self.set_irid.toggled.connect(self.set_irid_clicked)

      self.timer = QtCore.QTimer(self)
      self.timer.setInterval(10000)
      self.timer.timeout.connect(self.blink)

   def start(self):
     self.timer.start()

   def stop(self):
     self.timer.stop()

   def updateDCDC_clicked(self, enabled):
     cmd= "setpower\n";
     s.send(cmd)
     data=recv_end(s, 'EOF')
     powerstate=data.split()
     amcState     =int(powerstate[9])
     N2synthState =int(powerstate[16])
     N2paState    =int(powerstate[22])
     C2synthState =int(powerstate[29])
     C2paState    =int(powerstate[36])
     if(N2paState    ==0): self.dcdc1.setChecked(False)
     if(N2paState    ==1): self.dcdc1.setChecked(True)
     if(amcState     ==0): self.dcdc2.setChecked(False)
     if(amcState     ==1): self.dcdc2.setChecked(True)
     if(N2synthState ==0): self.dcdc3.setChecked(False)
     if(N2synthState ==1): self.dcdc3.setChecked(True)
     if(C2paState    ==0): self.dcdc4.setChecked(False)
     if(C2paState    ==1): self.dcdc4.setChecked(True)
     if(C2synthState ==0): self.dcdc5.setChecked(False)
     if(C2synthState ==1): self.dcdc5.setChecked(True)

   @QtCore.pyqtSlot()
   def blink(self):
          self.updateDCDC_clicked(self);

   def sendcmd(self):
     cmd= "%s\n" % self.serverCommand.text()
     s.send(cmd)
     data=recv_end(s, '\n')
     self.serverResponse.setText(str(data))
     self.serverCommand.setText("")
     if(cmd=="pid\n"):
       pidstate=data.split()
       N21_pid =int(pidstate[19])
       N22_pid =int(pidstate[3])
       C21_pid =int(pidstate[67])
       C22_pid =int(pidstate[35])
       O11_pid =int(pidstate[51])
       if(N21_pid==0): self.pid1.setChecked(False)
       if(N21_pid==1): self.pid1.setChecked(True)
       if(N22_pid==0): self.pid2.setChecked(False)
       if(N22_pid==1): self.pid2.setChecked(True)
       if(C21_pid==0): self.pid3.setChecked(False)
       if(C21_pid==1): self.pid3.setChecked(True)
       if(C22_pid==0): self.pid4.setChecked(False)
       if(C22_pid==1): self.pid4.setChecked(True)

   def updateIP(self):
     serverip = self.ipAddress.text()
     self.serverResponse.setText("ip address updated")

   def updatePORT(self):
     sport = self.TCPport.text()
     self.serverResponse.setText("TCP port updated")
     
   def btn_dcbias1_clicked(self, enabled):
     dacvalue = int(0.0*(65535/20)+32768)
     if enabled:
       dacvalue = int((9.0-3.0)*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (2,dacvalue)
     s.send(cmd)
     return1=recv_end(s,'\n')
     cmd="pid dacs 1 %d %d\n" % (6,dacvalue)
     s.send(cmd)
     return2=recv_end(s,'\n')
     self.serverResponse.setText(str(return1)+'\n'+str(return2))

   def btn_dcbias2_clicked(self, enabled):
     dacvalue = int(0.0*(65535/20)+32768)
     if enabled:
       dacvalue = int((6.0-3.0)*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (5,dacvalue)
     s.send(cmd)
     return1=recv_end(s,'\n')
     cmd="pid dacs 1 %d %d\n" % (8,dacvalue)
     s.send(cmd)
     return2=recv_end(s,'\n')
     self.serverResponse.setText(str(return1)+'\n'+str(return2))

   def btn_dcdc1_clicked(self, enabled):
     cmd="setpower pa14 0\n"
     if enabled:
       cmd="setpower pa14 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_dcdc2_clicked(self, enabled):
     cmd="setpower amc 0\n"
     if enabled:
       cmd="setpower amc 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_dcdc3_clicked(self, enabled):
     cmd="setpower synth14 0\n"
     if enabled:
       cmd="setpower synth14 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_dcdc4_clicked(self, enabled):
     cmd="setpower pa19 0\n"
     if enabled:
       cmd="setpower pa19 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_dcdc5_clicked(self, enabled):
     cmd="setpower synth19 0\n"
     if enabled:
       cmd="setpower synth19 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_pid1_clicked(self, enabled):
     cmd="pid 8 0\n"
     if enabled:
       cmd="pid 8 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_pid2_clicked(self, enabled):
     cmd="pid 5 0\n"
     if enabled:
       cmd="pid 5 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_pid3_clicked(self, enabled):
     cmd="pid 2 0\n"
     if enabled:
       cmd="pid 2 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_pid4_clicked(self, enabled):
     cmd="pid 6 0\n"
     if enabled:
       cmd="pid 6 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_pid5_clicked(self, enabled):
     cmd="pid 7 0\n"
     if enabled:
       cmd="pid 7 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def vmodeButton_clicked(self, enabled):
     #Set zero bias first
     cmd="zerobias\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))
     cmd="setfeedback --mask 0\n"
     if enabled:
       cmd="setfeedback --mask 255\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def relayButton_clicked(self, enabled):
     cmd="setpower relay 0\n"
     if enabled:
       cmd="setpower relay 1\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_spindV(self):
      global VOffset_1
      global VOffset_2
      global VOffset_3
      global VOffset_4
      global VOffset_5
      global VOffset_6
      global VOffset_7
      global VOffset_8
      VOffset_1 = self.spindV_1.value()
      VOffset_2 = self.spindV_2.value()
      VOffset_3 = self.spindV_3.value()
      VOffset_4 = self.spindV_4.value()
      VOffset_5 = self.spindV_5.value()
      VOffset_6 = self.spindV_6.value()
      VOffset_7 = self.spindV_7.value()
      VOffset_8 = self.spindV_8.value()

   def update_sweepnum(self):
     global numPoints
     numPoints = self.spinnumSweep.value()

   def update_sweepstart(self):
     global start
     start = self.sweepstart.value()

   def update_sweepstop(self):
     global stop
     stop = self.sweepstop.value()

   def update_pidSV1(self):
     dacvalue = self.spinSV1.value()
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 0 %d %d\n" % (8,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidSV2(self):
     dacvalue = self.spinSV2.value()
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 0 %d %d\n" % (5,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidSV3(self):
     dacvalue = self.spinSV3.value()
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 0 %d %d\n" % (2,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidSV4(self):
     dacvalue = self.spinSV4.value()
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 0 %d %d\n" % (6,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidDC1(self):
     dacvalue = self.spinDC1.value()-3.0
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (8,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidDC2(self):
     dacvalue = self.spinDC2.value()-3.0
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (5,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidDC3(self):
     dacvalue = self.spinDC3.value()-3.0
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (2,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def update_pidDC4(self):
     dacvalue = self.spinDC4.value()-3.0
     dacvalue = int(dacvalue*(65535/20)+32768)
     cmd="pid dacs 1 %d %d\n" % (6,dacvalue)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))

   def btn_zeropots_clicked(self):
     global biasold
     biasold=32768
     cmd="zerobias\n"
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))
          
   def btn_setbias_clicked(self):
     global biasold
     global pixel
     global VOffset
     biasnew = self.spinVoltage.value()
     if(biasnew != biasold):
       cmd="setbias --chan %d --dac %d\n" % (pixel, biasnew)
       s.send(cmd)
       data=recv_end(s,'\n')
       self.serverResponse.setText(str(data))
       biasold=biasnew
     cmd="getbias --chan %d\n" % pixel
     s.send(cmd)
     data=recv_end(s,'\n').split()
     self.serverResponse.setText(str(data))
     voltage=float(data[1]) + float(VOffset)
     current=float(data[4])
     resistance="{:.2f}".format(1000*voltage/current)
     self.editVoltage.setText(str(voltage))
     self.editCurrent.setText(str(current))
     self.editResistance.setText(str(resistance))

   def update_LNA(self):
     global pixel
     value = self.spinLNA.value()
     cmd="setLNA --chan %d --dac %d\n" % (pixel, value)
     s.send(cmd)
     data=recv_end(s,'\n')
     self.serverResponse.setText(str(data))
     cmd="getLNA --chan %d\n" % pixel
     s.send(cmd)
     data=recv_end(s,'\n').split()
     self.serverResponse.setText(str(data))
     LNAV=float(data[1])
     LNAmA=float(data[4])
     self.LNAVoltage.setText(str(LNAV))
     self.LNACurrent.setText(str(LNAmA))

   def btn_sweep_clicked(self):
     global pixel
     global numPoints
     global start
     global stop
     global VOffset
     cmd="getbias --chan %d\n" % pixel
     s.send(cmd)
     data=recv_end(s, '\n').split()
     #sweep -v to +v
     cmd="sweep --chan %d --start %d --stop %d --num %d\n" % (pixel, start, stop, numPoints)
     s.send(cmd)
     data=recv_end(s,'EOF')
     xytp = np.genfromtxt(StringIO(data[0:len(data)-4]),delimiter=" ", usecols=(3,6))
     xytp[0:(numPoints-1),0] += VOffset
     #sweep +v to -v
     if self.set_bid.isChecked():
        cmd="sweep --chan %d --stop %d --start %d --num %d\n" % (pixel, stop, start, numPoints)
        s.send(cmd)
        data=recv_end(s,'EOF')
        xytp2 = np.genfromtxt(StringIO(data[0:len(data)-4]),delimiter=" ", usecols=(3,6))
        xytp2[0:(numPoints-1),0] += VOffset
     #PLOT
     self.mpl.canvas.ax.clear()
     self.mpl.canvas.ax.set_xlim(xmin=-2, xmax=2)
     self.mpl.canvas.ax.set_ylim(ymin=-40, ymax=40)
     self.mpl.canvas.ax.autoscale(enable='False')
     self.mpl.canvas.ax.get_xaxis().grid(True)
     self.mpl.canvas.ax.get_yaxis().grid(True)
     self.mpl.canvas.ax.plot(xytp[0:(numPoints-1),0],xytp[0:(numPoints-1),1], marker="None")
     if self.set_bid.isChecked():
        self.mpl.canvas.ax.plot(xytp2[0:(numPoints-1),0],xytp2[0:(numPoints-1),1], color="Red")
     if self.set_ivp.isChecked():
        self.mpl.canvas.ax.plot(xytp[0:(numPoints-1),0],10*xytp[0:(numPoints-1),2])
     self.mpl.canvas.draw()
     if self.saveIV.isChecked():
        today=dt.date.today()
        time=dt.datetime.now().time()
        d=dt.datetime.combine(today,time)
        fname=d.strftime("%m%d_%H%M%S.txt")
        comment = "%s" % self.IVsweep_text.text()
        print comment
        if self.set_bid.isChecked():
           arr = np.array(np.hstack([xytp[0:(numPoints-1),0:2],xytp2[0:(numPoints-1),0:2]]))
           np.savetxt(fname, arr, fmt='%s', header=comment)
        else:
           arr = np.array(xytp[0:(numPoints-1),0:2])
           np.savetxt(fname, arr, fmt='%s', header=comment)

   def pixelButton_1_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 1 #CII #1
       VOffset = self.spindV_1.value()

   def pixelButton_2_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 2 #CII #2
       VOffset = self.spindV_2.value()

   def pixelButton_3_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 3  #NII #1
       VOffset = self.spindV_3.value()

   def pixelButton_4_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 4  #NII #2
       VOffset = self.spindV_4.value()

   def pixelButton_5_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 5 #CII #1
       VOffset = self.spindV_5.value()

   def pixelButton_6_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 6 #CII #2
       VOffset = self.spindV_6.value()

   def pixelButton_7_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 7  #NII #1
       VOffset = self.spindV_7.value()

   def pixelButton_8_clicked(self, enabled):
     if enabled:
       global pixel
       global VOffset
       pixel = 8  #NII #2
       VOffset = self.spindV_8.value()

   def set_irid_clicked(self, enabled):
     global serverip
     serverip = '192.168.0.104'
     if enabled:
        serverip = '192.168.0.104'

   def btn_close_clicked(self):
      global s
      s.close()
      del s
      self.timer.stop()
      self.led.leds[0].valueFalse()

   def btn_open_clicked(self):
      try:
         global s
         s  =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         s.connect((serverip, sport))
         self.led.leds[0].valueTrue()
      except socket.error, exc:
         self.led.leds[0].valueFalse()
      s.settimeout(30)
      #self.timer.start()

def main():
  app = QtGui.QApplication(sys.argv)
  myWindow = MyWindowClass(None)
  myWindow.show()
  app.exec_()

if __name__ == '__main__':
  main()

