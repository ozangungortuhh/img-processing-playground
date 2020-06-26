import glob
import cv2

label_counter = failed_counter = 0

for file in glob.glob('*.txt'):
    label = open(file, "r")
    label_counter += 1    
    line = label.read()
    split = line.split(' ')
    for coord in split[1:]:
        if float(coord) == 0:
            print("Corrupted label in file", file)
            failed_counter += 1
        
if failed_counter == 0:
    print(f"All {label_counter} labels are correct")
