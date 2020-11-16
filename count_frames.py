"""
Created on Sat Sep 19 18:06:48 2020
@author: ISH KAPOOR
"""
# import the necessary packages
from imutils.video import count_frames
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
ap.add_argument("-o", "--override", type=int, default=-1,
	help="whether to force manual frame count")
args = vars(ap.parse_args())

# count the total number of frames in the video file
override = False if args["override"] < 0 else True
total = count_frames(args["video"], override=override)

# display the frame count to the terminal
print("[INFO] {:,} total frames read from {}".format(total,
	args["video"][args["video"].rfind(os.path.sep) + 1:]))

'''
python count_frames.py --video Babbar.mov
'''