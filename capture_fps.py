import cv2
import time

class Capture:
    def __init__(self):
        self.video_source = 0
        self.cam = cv2.VideoCapture(self.video_source)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.counter = 0
        cv2.namedWindow("test")

        self.capture()


    def capture(self):
        start = time.time()
        tick = 0
        frame_counter = 0

        
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 30.0, (1280,720))
        
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("failed to grab frame")
                break
            # cv2.imshow("test", frame)
            # cv2.waitKey(1)

            self.out.write(frame)
            
            # Print FPS
            frame_counter += 1
            time_now = time.time() - start
            if(time_now - tick >= 1):
                tick += 1
                print(frame.shape)
                print("FPS:", frame_counter)
                frame_counter = 0

if __name__ == "__main__":
    capture = Capture()
