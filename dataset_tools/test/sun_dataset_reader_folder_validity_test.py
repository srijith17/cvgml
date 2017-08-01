import os
import unittest

from sun_dataset_reader import SunDatasetReader


class SUNDatasetReaderFolderValidityTest(unittest.TestCase) :
    datasetReader = SunDatasetReader()

    def setUp( self ) :
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_dataset_folder_does_not_exist( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'path_does_not_exist')
        try :
            self.datasetReader.read(test_data_path)
            self.fail('Did not throw expected execption')
        except :
            pass

    def test_retrieve_dataset_path( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        self.assertEqual(self.datasetReader.get_dataset_path, test_data_path)


if __name__ == '__main__':
    unittest.main()