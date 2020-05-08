import cv2

class Visualizator():
    def __init__(self):
        pass

    def show_image(self, image, wait=1):
        cv2.imshow("Image", image)
        cv2.waitKey(wait)
