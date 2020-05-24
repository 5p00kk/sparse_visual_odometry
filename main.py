from frame_loader import FrameLoader
from odometry import FeatureExtractor
from visualizator import Visualizator

# Declarations
frame_loader = FrameLoader("data/video.mp4")
extractor = FeatureExtractor("orb")
visualizator = Visualizator()
frame_read = True

while frame_read:
    # Load and display the frame
    frame_read, frame = frame_loader.get_frame()

    # Extract features and descriptors
    kp, des = extractor.extract_features(frame)

    # Visualize results
    visualizator.show_image(frame)
    visualizator.show_keypoints(frame, kp)

    # Printouts
    print("Captured frame: %d" % frame_loader.frame_num)
    print("Frame shape: %s" % (frame.shape,))
    print("Extracted keypoints: %d" % len(kp))

frame_loader.close()
