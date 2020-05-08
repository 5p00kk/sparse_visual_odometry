from frame_loader import FrameLoader
from odometry import FeatureExtractor
from visualizator import Visualizator

# Declarations
frame_loader = FrameLoader("data/video.mp4")
extractor = FeatureExtractor()
visualizator = Visualizator()
frame_read = True

while frame_read:
    # Load and display the frame
    frame_read, frame = frame_loader.get_frame()
    visualizator.show_image(frame)

    # Printouts
    print("Captured frame: %d" % frame_loader.frame_num)
    print("Frame shape: %s" % (frame.shape,))

frame_loader.close()
