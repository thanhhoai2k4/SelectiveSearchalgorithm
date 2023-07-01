# add libary package
import argparse
import random
import time 
import cv2



# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
ap.add_argument("-m", "--method", type=str, default="fast",
                choices=["fast", "quality"],
                help="seletive search method")

args = vars(ap.parse_args())

"""
    run file : python main.py --image E:\github_thanhhoai2k4\SelectiveSearchalgorithm\dog.jpg 
    python filename --image path
"""


# load image 
image = cv2.imread(args["image"])

#initalize OPENVC's selective search 

selectiveSearch = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
selectiveSearch.setBaseImage(image)


if args["method"] == "fast":
    print("[INFO] Using *fast* selective search")
    selectiveSearch.switchToSelectiveSearchFast()
else:
    print("[INFO] Using *quality* selective search")
    selectiveSearch.switchToSelectiveSearchQuality()


# time run on selective search on the image
start = time.time()
rects = selectiveSearch.process()
end = time.time()

# Show time
print("[INFO] selective: {}".format(end-start))
print("[INFO] total region proposals {}".format(len(rects)))


for  i in range(0,len(rects),100):
    output = image.copy()
    for (x,y,w,h) in rects[i:i+100]:
        color = [random.randint(0,255) for j in range(0,3)]
        cv2.rectangle(output,(x,y), (x+w,y+h), color, 2)
    
    cv2.imshow("Output", output)
    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        break
