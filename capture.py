import cv2

class Capture:
    def __init__(self):
        self.video_source = 0
        self.cam = cv2.VideoCapture(self.video_source)
        self.counter = 0
        cv2.namedWindow("test")
        self.capture()

    def capture(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = f"frame_{self.counter}.png"
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                self.counter += 1
        self.cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture = Capture()