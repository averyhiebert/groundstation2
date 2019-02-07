import sys
from PyQt4 import QtGui, QtCore
from qgis.core import *
from qgis.gui import *

class MapTracker(QtGui.QWidget):
    def __init__(self, map_source="WMS"):
        ''' map_source should be a path to a file, OR the string "WMS". '''
        super(MapTracker, self).__init__()
        self.map_source = map_source

        self.initUI()

    def initUI(self):
        # Create a map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(QtGui.QColor(220,220,220,255))
        self.canvas.enableAntiAliasing(True)
        self.canvas.show()
        
        # Add mouse pan functionality
        self.toolPan = QgsMapToolPan(self.canvas)
        self.canvas.setMapTool(self.toolPan)

        # Add the base layer to the map
        self.setMapSource(self.map_source)


        # Add vector layer
        vl = QgsVectorLayer("Point", "temporary_points", "memory")
        pr = vl.dataProvider()

        vl.startEditing()

        # TEMPORARY: Add a point at 0, 0
        p = QgsFeature()
        p.setGeometry( QgsGeometry.fromPoint(QgsPoint(10,10)) )
        pr.addFeatures( [p])
        vl.commitChanges()

        QgsMapLayerRegistry.instance().addMapLayer(vl)
        # Have to do something to make this actually appear on the map?
        # Will figure this out later.
        #self.canvas.setLayerSet([QgsMapCanvasLayer(self.base_layer),vl]) (?)
        
        


    def setMapSource(self, path):
        ''' Set the base layer of the map. '''
        self.map_source = path
        if path == "WMS":
            url = "contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/jpeg&layers=OSM-WMS&layers=OSM-Overlay-WMS&layers=TOPO-WMS&layers=TOPO-OSM-WMS&styles=&styles=&styles=&styles=&url=http://ows.terrestris.de/osm/service?VERSION%3D1.1.1%26"
            self.base_layer = QgsRasterLayer(url, 'A base map', 'wms')
        else:
            self.base_layer = QgsRasterLayer(self.map_source,"rock lake")

        QgsMapLayerRegistry.instance().addMapLayer(self.base_layer)
        self.canvas.setExtent(self.base_layer.extent())
        self.canvas.setLayerSet([QgsMapCanvasLayer(self.base_layer)])

    @QtCore.pyqtSlot(object)
    def on_newData(self, new_data):
        ''' Handle incoming data points by putting a marker on the rocket's
        current location. '''
        lat = new_data["latitude"]
        lon = new_data["longitude"]


if __name__=="__main__":
        app = QgsApplication([],True)
        QgsApplication.setPrefixPath(u'/usr/',True)
        QgsApplication.initQgis()

        #m = MapTracker(map_source = "/home/avery/Desktop/rocketry/GIS stuff/albertaimagery/rocklakeimagery/rocklake.tif")
        m = MapTracker(map_source = "WMS")
        sys.exit(app.exec_())
