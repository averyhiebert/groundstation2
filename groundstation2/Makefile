all: ui

ui:
	pyuic4 -w mainWindow.ui -o mainWindow_UI.py
	$(MAKE) -C dummy_map
	$(MAKE) -C data_sources/dummy_source

clean:
	find . -name "*.pyc" -type f -delete
	find . -name "*_UI.py" -type f -delete
	
