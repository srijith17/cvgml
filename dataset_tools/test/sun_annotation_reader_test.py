import os
import unittest

from AnnotationReader import AnnotationReader


class SUNDatasetAnnotationReaderTest(unittest.TestCase) :
    annotation_reader = AnnotationReader()

    def setUp( self ) :
        self.test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'good_dataset')
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_retrieveNumberOf3DAnnotations( self ) :
        annotation_file = self.annotation_reader.get_3d_annotation_file(self.test_data_path)
        annotation_data = self.annotation_reader.read_json_file(annotation_file)
        numberOfAnnot = self.annotation_reader.get_number_of_3d_annotations(annotation_data)
        self.assertEquals(numberOfAnnot, 16)

    def test_retrieveReadBoundingBox3DAnnotations( self ) :
        annotation_file = self.annotation_reader.get_3d_annotation_file(self.test_data_path)
        annotation_data = self.annotation_reader.read_json_file(annotation_file)
        numberOfAnnot = self.annotation_reader.get_number_of_3d_annotations(annotation_data)
        for i in range(0, numberOfAnnot) :
            if self.annotation_reader.annotated_data_exists(annotation_data, i) :
                self.annotation_reader.read_bounding_box(annotation_data, i)