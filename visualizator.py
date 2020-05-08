import cv2

class Visualizator():
    def __init__(self):
        pass

    def show_image(self, image, wait=1):
        cv2.imshow("Image", image)
        cv2.waitKey(wait)

    def show_keypoints(self, image, kp, wait=1):
        kp_image = cv2.drawKeypoints(image, kp, None, color=(0,255,0), flags=0)
        cv2.imshow("Keypoints", kp_image)
        cv2.waitKey(wait)
