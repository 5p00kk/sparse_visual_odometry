from frame_loader import FrameLoader
from odometry import FeatureExtractor

# Declarations
frame_loader = FrameLoader("data/video.mp4")
extractor = FeatureExtractor()
frame_read = True


while frame_read:
    frame_read, frame = frame_loader.get_frame()
    print("Captured frame %d" % frame_loader.frame_num)

frame_loader.close()
