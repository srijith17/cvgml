import os

import cv2
import numpy
import scipy.io


class SunDatasetReader :
    dataset_path = ''

    def read( self, file_path ) :
        if os.path.isdir(file_path) :
            self.dataset_path = file_path
        else :
            raise Exception('invlaid path')

    @property
    def get_dataset_path( self ) :
        return self.dataset_path

    @staticmethod
    def read_image( image_path, image_file_name ) :
        if os.path.isdir(image_path) :
            if len(image_file_name) <= 0 :
                image_file_name = os.listdir(image_path)[ 0 ]
            image_path = os.path.join(image_path, image_file_name)

            if os.path.isfile(image_path) :
                image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            else :
                raise Exception('image does not exist')
        else :
            raise Exception('folder does not exist')
        return image

    def get_rgb_image( self ) :
        rgb_path = os.path.join(self.dataset_path, 'image')
        return self.read_image(rgb_path, '')

    def get_depth_image( self ) :
        depth_path = os.path.join(self.dataset_path, 'depth')


        depth_image = self.read_image(depth_path, '')
        depth_image = scipy.bitwise_or(scipy.right_shift(depth_image, 3),
                                       scipy.left_shift(depth_image, 13));
        depth_image = depth_image / 1000;
        # depth_image(depth_image > 8) = 8;
        return depth_image

    def get_full_res_rgb_image( self ) :
        fullres_rgb_path = os.path.join(self.dataset_path, 'fullres')
        head, tail = os.path.split(self.dataset_path)
        file_name = tail + '.jpg'
        return self.read_image(fullres_rgb_path, file_name)

    def get_depth_denoised_image( self ) :
        denoised_depth_path = os.path.join(self.dataset_path, 'depth_bfx')
        return self.read_image(denoised_depth_path, '')

    def get_full_res_depth_image( self ) :
        fullres_depth_path = os.path.join(self.dataset_path, 'fullres')
        head, tail = os.path.split(self.dataset_path)
        file_name = tail + '_abs.png'
        return self.read_image(fullres_depth_path, file_name)

    def get_intrinsics( self ) :
        intrinsics_path = os.path.join(self.dataset_path, 'intrinsics.txt')
        return numpy.genfromtxt(intrinsics_path, delimiter = '')

    def get_full_res_intrinsics( self ) :
        fullres_intrinsics_path = os.path.join(self.dataset_path, 'fullres', 'intrinsics.txt')
        fullres_instrinsics = numpy.genfromtxt(fullres_intrinsics_path, delimiter = '')
        return fullres_instrinsics.reshape(3, 3)

    def get_full_extrinsics( self ) :
        extrinsics_folder_path = os.path.join(self.dataset_path, 'extrinsics')
        extrinsics_file_path = os.path.join(extrinsics_folder_path,
                                            os.listdir(extrinsics_folder_path)[ 0 ])
        return numpy.genfromtxt(extrinsics_file_path, delimiter = '')

    def get_segmentated_labels( self ) :
        semented_mat_file = os.path.join(self.dataset_path, 'seg.mat')
        segmentation_mat = scipy.io.loadmat(semented_mat_file)
        labeled_image = segmentation_mat[ 'seglabel' ]
        labels_string = segmentation_mat[ 'names' ]
        labels = [ str(''.join(letter)) for letter_array in labels_string[ 0 ] for letter in
                   letter_array ]
        return labeled_image, labels

    def get_point_cloud( self ) :
        depth_image = self.get_depth_image()
        intrinsics = self.get_intrinsics()
        return self.create_point_cloud_data(depth_image, intrinsics)

    @staticmethod
    def create_point_cloud_data( depth_image, intrinsics ) :
        depth_height = depth_image.shape[ 0 ]
        depth_width = depth_image.shape[ 1 ]

        point_cloud = numpy.zeros((depth_height * depth_width, 3),
                                  dtype = numpy.float)
        print (intrinsics[ 0, 2 ], intrinsics[ 0, 0 ])
        for w_index in range(depth_width) :
            for h_index in range(depth_height) :
                point_cloud_index = h_index * depth_width + w_index
                depth_value = depth_image[ h_index, w_index ]
                point_cloud[ point_cloud_index, 2 ] = depth_value
                point_cloud[ point_cloud_index, 0 ] = depth_value \
                                                      * ((w_index - intrinsics[ 0, 2 ]) /
                                                        intrinsics[ 0, 0 ])

                point_cloud[ point_cloud_index, 1 ] = depth_value \
                                                      * ((h_index - intrinsics[ 1, 2 ]) /
                                                        intrinsics[ 1, 1 ])

        return point_cloud
