import os
import unittest

import cv2

from SUNDatasetReader import SunDatasetReader


class DatasetVisualizerTests(unittest.TestCase) :
    datasetReader = SunDatasetReader()

    def setUp( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_displayRGBImage( self ) :
        rgb_image = self.datasetReader.get_rgb_image()
        cv2.imshow("rgb", rgb_image);
        cv2.waitKey(-1);

    def test_displayDepthImage( self ) :
        depth_image = self.datasetReader.get_depth_image()
        cv2.imshow("depth", depth_image);
        cv2.waitKey(-1);

