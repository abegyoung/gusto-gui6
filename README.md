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

![alt text](https://github.com/abegyoung/gusto-gui6/blob/main/Anritsu/images/main.jpg?raw=true)

