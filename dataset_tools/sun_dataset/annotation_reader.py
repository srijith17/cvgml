import json
import os

import numpy


class GroundTruth(object) :
    x = 0
    y = 0
    zmin = 0
    zmax = 0
    label = ''
    centroid = [ 0, 0, 0 ]
    basis = [ ]
    coeffs = [ ]
    orientation = [ ]
    pass


class AnnotationReader :
    # def get3DAnnotationLayout(self):
    #     annotation_file = os.path.join(self.dataset_path, 'annotation3Dlayout', 'index.json')
    #     annotation3D, labels3D = self.read3DAnnotationFile(annotation_file)
    #     pass

    def get_3d_annotation( self, dataset_path ) :
        annotation_file = self.get_3d_annotation_file(dataset_path)
        pass

    @staticmethod
    def get_3d_annotation_file( dataset_path ) :
        return os.path.join(dataset_path, 'annotation3Dfinal', 'index.json')

    def read_3d_annotation_file( self, annotation_file ) :
        annotation_data = self.read_json_file(annotation_file)
        numberOfAnnot = self.get_number_of_3d_annotations(annotation_data)
        return self.read3dAnnotationData(annotation_data, numberOfAnnot)

    @staticmethod
    def read_json_file( annotation_file ) :
        with open(annotation_file) as json_data :
            annotation_data = json.load(json_data)
        return annotation_data

    # def read3dAnnotationData(self, annotation_data, numberOfAnnot):
    #     annotation3D = [];
    #     labels3D = [];
    #     for i in range(0, numberOfAnnot):
    #         idxObj, x, y, z = self.get3dBBData(annotation_data, i)
    #         pts3 = numpy.array([x, y, z], numpy.int32)
    #         pts3 = numpy.transpose(pts3);
    #         annotation3D.append(pts3);
    #         labels3D.append(annotation_data['objects'][idxObj]["name"])
    #     return annotation3D, labels3D
    #
    # def get3dBBData(self, annotation_data, i):
    #     box = self.getBBData(annotation_data, "polygon", i)
    #     # idxObj = self.getBBData(annotation_data, "object", i);
    #     return idxObj, x, y, zmin, zmax


    @staticmethod
    def get_number_of_3d_annotations( annotation_data ) :
        return len(annotation_data[ "objects" ])

    @staticmethod
    def get_annotated_data( annotation_data, param, i ) :
        return annotation_data[ "objects" ][ i ][ "polygon" ][ 0 ][ param ]

    @staticmethod
    def annotated_data_exists( annotation_data, i ) :
        if annotation_data[ "objects" ][ i ] :
            return True
        else :
            return False

    def read_bounding_box( self, annotation_data, i ) :
        gt_box = GroundTruth()
        gt_box.x = self.get_annotated_data(annotation_data, "X", i)
        gt_box.y = self.get_annotated_data(annotation_data, "Z", i)
        vector1 = [ gt_box.x[ 1 ] - gt_box.x[ 0 ], gt_box.y[ 1 ] - gt_box.y[ 0 ], 0 ]
        coeff1 = numpy.linalg.norm(vector1)
        vector1 = vector1 / coeff1

        vector2 = [ gt_box.x[ 2 ] - gt_box.x[ 1 ], gt_box.y[ 2 ] - gt_box.y[ 1 ], 0 ]
        coeff2 = numpy.linalg.norm(vector2)
        vector2 = vector2 / coeff2
        up = numpy.cross(vector1, vector2)
        vector1 = (vector1 * up[ 2 ]) / up[ 2 ]
        vector2 = (vector2 * up[ 2 ]) / up[ 2 ]
        centroid2D = [ 0.5 * (gt_box.x[ 0 ] + gt_box.x[ 2 ]),
                       0.5 * (gt_box.y[ 0 ] + gt_box.y[ 2 ]) ]

        gt_box.basis = [ [ vector1 ], [ vector2 ], [ 0, 0, 1 ] ]  # one row is one basis
        gt_box.zmin = -self.get_annotated_data(annotation_data, "Ymin", i)
        gt_box.zmax = -self.get_annotated_data(annotation_data, "Ymax", i)

        gt_box.coeffs = numpy.abs([ coeff1, coeff2, gt_box.zmax - gt_box.zmin ]) / 2
        gt_box.centroid = [ centroid2D[ 0 ], centroid2D[ 1 ], 0.5 * (gt_box.zmin + gt_box.zmax) ]
        orientation = [ [ 0.5 * (gt_box.x[ 1 ] + gt_box.x[ 0 ]),
                          0.5 * (gt_box.y[ 1 ] + gt_box.y[ 0 ]) ] - numpy.transpose(centroid2D), 0 ]
        print(orientation)

        # orientation_magnitude  = scipy.linalg.norm(orientation)
        # if orientation_magnitude == 0:
        #     gt_box.orientation = orientation / orientation_magnitude
        # print(gt_box)

        pass
