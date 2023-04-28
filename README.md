# gusto-gui6
Fork of gusto-gut porting from pyqt4 and py27 to pyqt6 and py311

## Installation
### For Mac:
Oh Lord, Ventura has made me upgrade from pyqt4 and Python2.7 to pyqt6 and Python3.

Running in a virtual environment for now, so do once:
```
   python -m venv venv
   source venv/bin/activate

   python -m pip install pyqt6 pyqt6-tools pyserial numpy matplotlib
   python startup.py
```

when done working in the virtual environment: `deactivate`

## Anritsu
This gui displays the Anritsu MA24126A USB power meter head in mW, dBm, and a scrolling screen.

![alt text](https://github.com/abegyoung/gusto-gui6/blob/main/images/meter.jpg?raw=true)

## B3LO
This gui operates the B3LO controller on 4 tabs.

![alt text](https://github.com/abegyoung/gusto-gui6/blob/main/images/B3LO_mainTab.jpg?raw=true)

### Main Tab 
QCL bias setting is controled and monitor is displayed on the left panel.

SLED multplier and PSat settings are controlled disaplayed on the right panel.

A Server response window, refresh button, and communication buttons are at bottom.

### DCDC Tab
DCDC control is here.

### PID AMP Tab
B3LO amplitude pump level pid via optical vane is controlled here.

### PID FRQ Tab
B3LO frequency is controlled via SLED input and QCL bias is controlled from here.

### VCO REG Tab
Hittite synthesizer register settings may be read and written here.
