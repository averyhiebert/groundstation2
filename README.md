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
this data in a Python application built using the Qt5 framework and the 
QGIS mapping software.  

The project uses Python 3, Qt5, and QGIS 3. 

## Building & Running
Read `documentation/getting_started.md`

## Dependencies
The software has been developed mainly in Ubuntu and Linux Mint.  Since the 
application is primarily in Python, it should work across other platforms, 
but some dependencies might not be conveniently available for other OSes.

See `documentation/install_dependencies.txt` for more information on installing
dependencies.  The main dependencies are Qt5 and the corresponding Python
bindings and dev tools, and the QGIS 3 software.

The packages `rtl-sdr` and `direwolf` will probably eventually be required, 
but are not yet necessary at this point in development. 

## Documentation
Look in the `documentation` folder for further documentation.

## License
This software is licensed under the MIT license, as described in `LICENSE.txt`.
