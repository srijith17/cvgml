import os
import unittest

import cv2

from sun_dataset_reader import SunDatasetReader


class DatasetVisualizerTests(unittest.TestCase) :
    dataset_reader = SunDatasetReader()

    def setUp( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test_data',
                                      'good_dataset')
        print(test_data_path)
        self.dataset_reader.read(test_data_path)
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_display_rgb_image( self ) :
        rgb_image = self.dataset_reader.get_rgb_image()
        cv2.imshow("rgb", rgb_image);
        cv2.waitKey(-1);

    def test_display_depth_image( self ) :
        depth_image = self.dataset_reader.get_depth_image()
        cv2.imshow("depth", depth_image/5);
        cv2.waitKey(-1);



if __name__ == '__main__':
    unittest.main()