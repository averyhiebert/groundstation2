# UVic Rocketry Ground Station V2
This is the second version of UVic Rocketry's ground station software 
for receiving and visualizing live telemetry from a rocket using a
software-defined radio.  The previous version can be found [here](https://github.com/averyhiebert/groundstation).

The software is still under development and is not yet functional (although at
this point many of the individual pieces of functionality are implemented).  
It's been developed very slowly for the past 2 years, but if anyone (at UVic or
elsewhere) wants to take it up and build on it, that'd be great.

## Planned Functionality
The software will use the `rtl_fm` and `direwolf` programs to demodulate and
decode APRS data received via a software-defined radio, and will then display 
this data in a Python application built using the Qt4 framework and the 
QGIS mapping software.  

The project uses Python 2.7 and Qt4, since Python 3 and Qt5 were not 
supported by QGIS at the time when this project was begun.  Upgrading to
QGIS3/Python3/Qt5 should ideally occure eventually.

## Building & Running
Read `documentation/getting_started.md`

## Dependencies
The software has been developed mainly in Ubuntu and Linux Mint.  Since the 
application is primarily in Python, it should work across other platforms, 
but some dependencies might not be conveniently available for other OSes.

The PyQt4 Python bindings (`python-qt4`) for the Qt application framework 
are required, along with the pyqt4 dev tools (`pyqt4-dev-tools`) and the
visual interface designer (`qt4-designer`).

Additionally, the software QGIS (version 2.8, although other 2.x versions may 
also work) is required, along with the corresponding `qgis` python package.

The packages `rtl-sdr` and `direwolf` will eventually be required, but are not
yet necessary at this point in development. 

## Documentation
Look in the `documentation` folder for further documentation.

## License
This software is licensed under the MIT license, as described in `LICENSE.txt`.
