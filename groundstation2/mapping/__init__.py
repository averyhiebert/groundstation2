import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from qgis.core import *
from qgis.gui import *

def print_extent(ext):
        # (TEMP)
        xmin = ext.xMinimum()
        xmax = ext.xMaximum()
        ymin = ext.yMinimum()
        ymax = ext.yMaximum()
        coords = "%f,%f,%f,%f" %(xmin, xmax, ymin, ymax)
        print(coords)

#class MapTracker(QtGui.QWidget):
class MapTracker(QtWidgets.QWidget):
    newData = QtCore.pyqtSignal(object)

    def __init__(self,parent=None):
        ''' base_layer_source should be a path to a file, OR the string "WMS". '''
        base_layer_source="WMS"
        super(MapTracker, self).__init__(parent)
        self.base_layer_source = base_layer_source
        self.newData.connect(self.on_newData)

        self.initUI()

    def initUI(self):
        # Create a map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(QtGui.QColor(220,220,220,255))
        # Optional, might be slower but prettier:
        self.canvas.enableAntiAliasing(True)

        # Insert canvas into self
        _layout = QtGui.QVBoxLayout(self)
        _layout.addWidget(self.canvas)
        self.canvas.show()
       
        # Add mouse pan functionality
        self.toolPan = QgsMapToolPan(self.canvas)
        self.canvas.setMapTool(self.toolPan)

        # Used when adding line segments to map:
        self.prev_lon_lat = None

        # Add the base layer to the map
        #  (Note: this adds several properties corresponding to map layers)
        self.setUpMap(self.base_layer_source)
        pass



    def setUpMap(self, path):
        ''' Set the base layer of the map. '''
        # Create the base layer of the map, possibly loaded from a file
        #  (e.g. geotiff or something)
        if path == "WMS":
            url = "contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/jpeg&layers=OSM-WMS&layers=OSM-Overlay-WMS&layers=TOPO-WMS&layers=TOPO-OSM-WMS&styles=&styles=&styles=&styles=&url=http://ows.terrestris.de/osm/service?VERSION%3D1.1.1%26"
            self.base_layer = QgsRasterLayer(url, 'OpenStreetMap', 'wms')
        else:
            self.base_layer = QgsRasterLayer(path,"base map")

        self.canvas.setExtent(self.base_layer.extent())
        self.canvas.setLayers([self.base_layer])

        # ====================================================================
        # Create a point layer tracking the current location of the rocket
        self.location_layer = QgsVectorLayer(
            "Point","Current Rocket Location","memory")
        self.location_pr = self.location_layer.dataProvider()

        symbol = QgsMarkerSymbol.createSimple({'name':'triangle','color':'red'})
        self.location_layer.renderer().setSymbol(symbol)

        # ====================================================================
        # Create a polyline layer of line segments tracking the rocket.
        # (We use individual line segments so that each can eventually contain
        #  additional attributes - altitude, time, GPS lock, continuity, etc.)
        self.history_layer = QgsVectorLayer(
            "MultiLineString","Rocket Trajectory","memory")
        self.history_pr = self.history_layer.dataProvider()
        symbol = QgsLineSymbol.createSimple(
            {'color':'red'})
        self.history_layer.renderer().setSymbol(symbol)

        # ====================================================================
        # Put all these things onto the map
        self.canvas.setLayers([self.location_layer,
            self.history_layer,self.base_layer])
        # TODO: Choose where to set the default extent (i.e. camera location)
        #   of the map.
        

    @QtCore.pyqtSlot(object)
    def on_newData(self, new_data):
        ''' Handle incoming data points by putting a marker on the rocket's
        current location and adding a line segment from the previous location
        to the current location.
        
        In the future, we will also add attributes to the line segments.'''
        lon = new_data["longitude"]
        lat = new_data["latitude"]

        # Clear existing marker and replace with new one
        self.location_pr.deleteFeatures(
            [f.id() for f in self.location_layer.getFeatures()])
        p = QgsFeature()
        p.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(lon,lat)))
        self.location_pr.addFeatures([p])

        # Create & add line segment.
        if self.prev_lon_lat == None:
            self.prev_lon_lat = (lon, lat)
        segment = QgsFeature()
        segment.setGeometry(QgsGeometry.fromPolylineXY(
            [QgsPointXY(*self.prev_lon_lat),QgsPointXY(lon,lat)]))
        self.history_pr.addFeatures([segment])

        self.prev_lon_lat = (lon, lat) # Update "previous lon/lat"

        self.canvas.refresh()


if __name__=="__main__":
        app = QgsApplication([],True)
        QgsApplication.setPrefixPath(u'/usr/',True)
        QgsApplication.initQgis()
        print("test")

        #m = MapTracker(base_layer_source = "/home/avery/Desktop/rocketry/GIS stuff/albertaimagery/rocklakeimagery/rocklake.tif")
        m = MapTracker()

        # Test update function by sending random data on a timer.
        timer = QtCore.QTimer()
        import random
        def rand_loc():
            return {
                "latitude":random.randint(-80,80),
                "longitude":random.randint(-170,170)
            }
        timer.timeout.connect(lambda: m.newData.emit(rand_loc()))
        timer.start(1000)

        sys.exit(app.exec_())
