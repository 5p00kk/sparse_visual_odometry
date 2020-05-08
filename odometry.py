import cv2 

class FeatureExtractor():
    def __init__(self, type):
        if type == "orb":
            self.extractor = cv2.ORB_create()
        else:
            self.extractor = None
    
    def extract_features(self, frame):
        assert self.extractor is not None
        
        # Extract keypoints
        kp = self.extractor.detect(frame, None)
        # Compute descriptors
        kp, des = self.extractor.compute(frame, kp)

        return kp, des

    def filter_features(self, features):
        pass

class Odometry():
    def __init__(self):
        pass

    def do_odometry(self, kp_pairs):
        pass