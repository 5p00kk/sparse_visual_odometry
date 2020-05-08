import cv2

class FrameLoader():
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.frame_num = 0
    
    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.frame_num += 1
        
        return ret, frame

    def close(self):
        self.cap.release()