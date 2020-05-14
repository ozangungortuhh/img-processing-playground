import cv2

class DisplayImage:
    def __init__(self):
        frame = cv2.imread("frame_0.png")
        cv2.namedWindow("display")
        cv2.imshow("display", frame)
        cv2.waitKey(0)


if __name__ == "__main__":
    display = DisplayImage()