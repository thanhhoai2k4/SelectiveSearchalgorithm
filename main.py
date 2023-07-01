# add libary package
import argparse
import random
import time 
import cv2



# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("--i", "--image", required=True,
                help="path to the input image")
ap.add_argument("-m", "--method", type=str, default="fast",
                choices=["fast", "quality"],
                help="seletive search method")

args = vars(ap.parse_args())

# run file : python main.py --image E:\github_thanhhoai2k4\SelectiveSearchalgorithm\dog.jpg 

