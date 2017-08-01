import os
import sys

import numpy
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

from sun_dataset_reader import SunDatasetReader

datasetReader = SunDatasetReader()
test_data_path = os.path.join(os.getcwd(), '..','..', 'dataset_tools','test','test_data',
                              'good_dataset')
print(test_data_path)
datasetReader.read(test_data_path)
vertices = datasetReader.get_point_cloud()

rgb_image = datasetReader.get_rgb_image()
vertices_rgb = rgb_image.reshape(rgb_image.shape[ 0 ] * rgb_image.shape[ 1 ],
                                 rgb_image.shape[ 2 ])


minimum_z_distance = numpy.min(vertices[vertices[:,2]>0,:])
vertices[:,2] = vertices[:,2] > 0 - minimum_z_distance
print(minimum_z_distance)
r_channel = numpy.copy(vertices_rgb[:,0])
vertices_rgb[:,0] = vertices_rgb[:,2]
vertices_rgb[:,2] = r_channel

vertices_rgb = vertices_rgb.astype(numpy.float32)/ 255.0

vertices_alpha = numpy.ones((vertices_rgb.shape[ 0 ], 1))
vertices_rgba = numpy.hstack((vertices_rgb, vertices_alpha))

app = QtGui.QApplication([ ])
w = gl.GLViewWidget()
w.opts[ 'distance' ] = 1
w.opts[ 'elevation' ] = -90
w.opts[ 'azimuth' ] = -90

w.show()
w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

g = gl.GLGridItem()
g.scale(0.1, 0.1, 0.1)
w.addItem(g)

point_cloud = gl.GLScatterPlotItem()
point_cloud.setData(pos = vertices , color = vertices_rgba,
                                   size = 2.0)
w.addItem(point_cloud)

if __name__ == '__main__' :
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION') :
        QtGui.QApplication.instance().exec_()
