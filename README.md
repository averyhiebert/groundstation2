# UVic Rocketry Ground Station V2
This is the second version of UVic Rocketry's ground station software 
for receiving and visualizing live telemetry from a rocket using a
software-defined radio.

The software is currently in early development and is not yet functional.

## Planned Functionality
The software will use the `rtl_fm` and `direwolf` programs to demodulate and
decode APRS data received via a software-defined radio, and will then display 
this data in a Python application built using the Qt4 framework and the 
QGIS mapping software.  

The project uses Python 2.7 and Qt4, since Python 3 and Qt5 are not yet
supported by QGIS.

## Building & Running
Read `documentation/getting_started.md`

## Dependencies
The software was developed using Ubuntu 16.  Since the application is primarily
in Python, it should work across other platforms, but many of the dependencies
may only be available for Linux.

The PyQt4 Python bindings (`python-qt4`) for the Qt application framework 
are required, along with the pyqt4 dev tools (`pyqt4-dev-tools`) and the
visual interface designer (`qt4-designer`).

The packages `rtl-sdr` and `direwolf` will eventually be required, but are not
yet necessary at this point in development.  Similarly, the QGIS application
will eventually be a dependency, but is not used at the moment.

## Documentation
Look in the `documentation` folder for further documentation.
