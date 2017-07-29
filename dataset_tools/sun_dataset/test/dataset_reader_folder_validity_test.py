import os
import unittest

from SUNDatasetReader import SunDatasetReader


class SUNDatasetReaderFolderValidityTest(unittest.TestCase) :
    datasetReader = SunDatasetReader()

    def setUp( self ) :
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_dataSetFolderDoesnotExist( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'path_does_not_exist')
        try :
            self.datasetReader.read(test_data_path)
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieveDataSetPath( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        self.assertEqual(self.datasetReader.get_dataset_path, test_data_path)