import os
import unittest

from SUNDatasetReader import SunDatasetReader


class SUNDatasetReaderEmptyFolderTest(unittest.TestCase) :
    datasetReader = SunDatasetReader()

    def setUp( self ) :
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'empty_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_retrieveRGBImage( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieveFullResRGBImage( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieveDepthImage( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieveFullResDepthImage( self ) :
        try :
            self.fail('Did not throw expected execption')
        except :
            pass