import os, sys

import unittest
import numpy

from sun_dataset_reader import SunDatasetReader

# mat = scipy.io.loadmat('file.mat')


class SUNDatasetReaderTest(unittest.TestCase) :
    dataset_reader = SunDatasetReader()

    def setUp( self ) :
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'good_dataset')
        print(test_data_path)
        self.dataset_reader.read(test_data_path)
        """ Set up for the test """

    def tearDown( self ) :
        """ Tear Down for the test """

    def test_retrieve_rgb_image( self ) :
        rgb_image = self.dataset_reader.get_rgb_image()
        self.assertEquals(rgb_image.shape, (427, 561, 3))

    def test_retrieve_full_res_rgb_image( self ) :
        rgb_image = self.dataset_reader.get_full_res_rgb_image()
        self.assertEquals(rgb_image.shape, (480, 640, 3))

    def test_retrieve_depth_image( self ) :
        depth_image = self.dataset_reader.get_depth_image()
        self.assertEquals(depth_image.shape, (427, 561))

    def test_retrieve_denoised_depth_image( self ) :
        depth_image = self.dataset_reader.get_depth_denoised_image()
        self.assertEquals(depth_image.shape, (427, 561))

    def test_retrieve_full_res_depth_image( self ) :
        rgb_image = self.dataset_reader.get_full_res_depth_image()
        self.assertEquals(rgb_image.shape, (480, 640))

    def test_retrieve_intrinsics( self ) :
        expected_intrinsics = [ [ 520.532, 0.0, 277.9258 ],
                                [ 0.0, 520.7444, 215.115 ],
                                [ 0.0, 0.0, 1.0 ] ]
        intrinsics = self.dataset_reader.get_intrinsics()
        self.assertTrue(numpy.allclose(intrinsics, expected_intrinsics))

    def test_retrieve_full_res_intrinsics( self ) :
        expected_fullres_intrinsics = [ [ 520.532, 0.0, 318.9258 ],
                                        [ 0.0, 520.7444, 260.115 ],
                                        [ 0.0, 0.0, 1.0 ] ]

        fullres_intrinsics = self.dataset_reader.get_full_res_intrinsics()
        self.assertTrue(numpy.allclose(fullres_intrinsics, expected_fullres_intrinsics))

    def test_retrieve_extrinsics( self ) :
        expected_extrinsics = [ [ 0.999997, -0.002568, -0.000358, 0.000000 ],
                                [ 0.002568, 0.961833, 0.273625, 0.000000 ],
                                [ -0.000358, -0.273625, 0.961836, 0.000000 ] ]
        full_extrinsics = self.dataset_reader.get_full_extrinsics()
        self.assertTrue(numpy.allclose(full_extrinsics, expected_extrinsics))

    def test_retrieve_segmentation_labels( self ) :
        expected_labels = [ 'wall', 'wall', 'monitor', 'monitor', 'window', 'window', 'window',
                            'floor', 'wall', 'mouse', 'keyboard', 'bottle', 'bottle', 'board',
                            'table', 'wall', 'bottle', 'bottle', 'wall', 'wall', 'wall', 'floor',
                            'cpu', 'table' ]
        labeled_image, labels = self.dataset_reader.get_segmentated_labels()
        self.assertListEqual(expected_labels, labels)

    # def test_retrieve_3d_annotations( self ) :
    #     annotation3D, labels3D = self.dataset_reader.get3DAnnotation()
    #     print(annotation3D)
    #     print(labels3D)

    # def test_retrieve3DAnnotationsLayout(self):
    #     annotation3DLayout, labels3DLayout = self.datasetReader.get3DAnnotationLayout()
    #     print(annotation3DLayout)
    #     print(labels3DLayout)

    # def test_retrieveAnnotation3DFinal(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))
    #
    # def test_retrieveAnnotation3DLayout(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))
    #
    # def test_retrieveScene(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))

if __name__ == '__main__':
    unittest.main()