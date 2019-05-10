# Getting Started
This is a quick guide to installing the necessary dependencies, building,
and running the application.

## Install Dependencies
(Note: This guide was written well after I installed these dependencies myself.
If anything isn't working for you, let me know so that I can update it.)

The application requires Python 2.7 to run.  If you do not have python 2.7 on
installed (you probably do, if you're using Ubuntu 16 as recommended), 
install it.

You'll also want `make`, which you likely already have installed.  If not
installed, on Ubuntu run :
```
sudo apt-get update
sudo apt-get install make
```

This application is built using the PyQt4 Framework.  To install PyQt4
dependencies, run
```
sudo apt-get update
sudo apt-get install python-qt4 
sudo apt-get install pyqt4-dev-tools qt4-designer 
```

(If you're wondering: the `python-qt4` package gives python bindings for the Qt
application framework.  The package `qt4-designer` is a
WYSIWYG design tool which is used to edit the `.ui` files that define
the application's visual interface.  The `pyqt4-dev-tools` package
contains the `pyuic4` utility, which we use to compile the `.ui` files into
python files.)

Finally, install the following dependencies via pip:
```
pip install pyqtgraph
```

## Build
In the `groundstation2` directory, run `make`.  This will compile all `.ui`
files into `.py` files using `pyuic4`.

## Run
In the `groundstation2` directory, run `python __init__.py`

(**NOTE:** When running the application in its current (unfinished) state, 
if you start the dummy data source by clicking the "Start" button on the 
"Controls" page, *you must also stop the data source before quitting 
the application* or else the process will continue running the 
background until you kill it manually.)
