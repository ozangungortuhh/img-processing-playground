# import the necessary packages
import imutils
import numpy as np
import cv2

class DistanceToCamera:
    def __init__(self):
        self.KNOWN_DISTANCE = 122
        self.KNOWN_WIDTH = 26
        self.KNOWN_PIXEL_WIDTH=131
        
        image = cv2.imread("frame_0.png")
        marker = self.find_marker(image)
        focalLength = self.get_focal_length()
        distance = self.distance_to_camera(self.KNOWN_WIDTH, focalLength, marker[1][0])

        box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        cv2.putText(image, str(distance), (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
        cv2.imshow("image", image)
        cv2.waitKey(0)

    def find_marker(self, image):
        # convert the image to grayscale, blur it, and detect edges
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)
        cv2.imshow("image", edged)
        cv2.waitKey(0)
        # find the contours in the edged image and keep the largest one;
        # we'll assume that this is our piece of paper in the image
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key = cv2.contourArea)
       
        # compute the bounding box of the of the paper region and return it
        return cv2.minAreaRect(c)
    
    def distance_to_camera(self,knownWidth, focalLength, perWidth):
        # compute and return the distance from the maker to the camera
	    return (knownWidth * focalLength) / perWidth
    def get_focal_length(self):
        return (self.KNOWN_PIXEL_WIDTH * self.KNOWN_DISTANCE) / self.KNOWN_WIDTH
if __name__ == "__main__":
    distance = DistanceToCamera()