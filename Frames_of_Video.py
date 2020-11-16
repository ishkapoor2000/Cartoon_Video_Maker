"""
Created on Sat Sep 19 19:04:06 2020
@author: ISH KAPOOR
"""
import cv2
import os

def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)

    cap = cv2.VideoCapture(pathIn)
    count = 0

    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.png".format(count)),
                        frame)
            # save frame as PNG file
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    PathInName = str(input("Enter full name:\n"))
    PathOutName = str(input("Enter folder name:\n"))
    extractFrames(PathInName, 'Babbar_Frame')

if __name__=="__main__":
    main()