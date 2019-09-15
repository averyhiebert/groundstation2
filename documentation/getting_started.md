# Getting Started
This is a quick guide to installing the necessary dependencies, building,
and running the application.

## Install Dependencies

A list of commands for installing dependenceis in Ubuntu 18 (Bionic Beaver)
can be found in `install_dependencies.txt`.

## Build
In the `groundstation2` directory, run `make`.  This will compile all `.ui`
files into `.py` files using `pyuic5`.

## Run
In the `groundstation2` directory, run `python3 __init__.py`

(**NOTE:** When running the application in its current (unfinished) state, 
if you start the dummy data source by clicking the "Start" button on the 
"Controls" page, *you must also stop the data source before quitting 
the application* or else the process will continue running the 
background until you kill it manually.)
