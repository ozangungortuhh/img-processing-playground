import glob
import cv2

frame_counter = success_counter = 0

for frame in glob.glob('/home/o.guengoer/itl/data/distance-17-06-2020/14-29/*.jpg'):
    cv_img = cv2.imread(frame)
    height, width, _ = cv_img.shape
    frame_counter += 1
    if width == 1920 and height == 1080:
        success_counter += 1
    else:
        print("image failed size check", frame, width, height)
if frame_counter == success_counter:
    print(f"All {frame_counter} frames passed the size check")        
