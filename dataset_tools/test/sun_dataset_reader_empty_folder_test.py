import os
import unittest

from sun_dataset_reader import SunDatasetReader


class SUNDatasetReaderEmptyFolderTest(unittest.TestCase) :
    datasetReader = SunDatasetReader()

    def setUp( self ) :
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'empty_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_retrieve_rgb_image( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieve_full_res_rgb_image( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieve_depth_image( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieve_full_res_depth_image( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

if __name__ == '__main__':
    unittest.main()