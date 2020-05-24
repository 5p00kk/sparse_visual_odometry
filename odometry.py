import cv2
import numpy as np

class FeatureExtractor():
    def __init__(self, extractor_type, nfeatures_per_cell=100, patch_size=32):
        if extractor_type == "orb":
            self.patch_size = patch_size
            self.extractor = cv2.ORB_create(nfeatures=nfeatures_per_cell,
                                            edgeThreshold=patch_size,
                                            patchSize=patch_size,
                                            scoreType=cv2.ORB_FAST_SCORE)
        else:
            self.extractor = None
    
    def extract_from_cell(self, cell):
        # Extract keypoints
        kp = self.extractor.detect(cell, None)
        # Compute descriptors
        kp, des = self.extractor.compute(cell, kp)

        return kp, des

    def extract_features(self, frame, height_div=1, width_div=1):
        assert self.extractor is not None

        # Bucketing - divide image into cells
        
        # TODO, implement more advanced method from:
        # Efficient_adaptive_non-maximal_suppression_algorithms_for_homogeneous_spatial_keypoint_distribution

        # TODO Add some checks for this division
        # If not divideable not all pixels of the input iamge will be used
        height_step = int(frame.shape[0]/height_div)
        width_step = int(frame.shape[1]/width_div)

        full_image_kps = []
        full_image_des = []

        # Divide image into cells
        for width_cell_idx in range(width_div):
            for height_cell_idx in range(height_div):
                # Get cell coordinates
                # Add patch size overlap to avoid extractor boarders inside of the image
                start_x = width_step*width_cell_idx
                end_x = width_step*(width_cell_idx+1)+self.patch_size
                start_y = height_step*height_cell_idx
                end_y = height_step*(height_cell_idx+1)+self.patch_size

                # Make sure that the last cell is not out of bounds
                end_x = min(end_x, frame.shape[1])
                end_y = min(end_y, frame.shape[0])

                # Extract a cell
                image_cell = frame[start_y:end_y, start_x:end_x, :].copy()

                # Extract features from the cell                
                kps, des = self.extract_from_cell(image_cell)
                
                # Translate cell keypoint into global image frame
                for idx, kp in enumerate(kps):
                    full_image_kps.append(cv2.KeyPoint(kp.pt[0] + start_x, kp.pt[1] + start_y, kp.size))
                    full_image_des.append(des[idx])

        return full_image_kps, full_image_des

    def filter_features(self, features):
        pass

class Odometry():
    def __init__(self):
        pass

    def do_odometry(self, kp_pairs):
        pass