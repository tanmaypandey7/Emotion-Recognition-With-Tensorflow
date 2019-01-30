import cv2


im= cv2.imread(r"C:\Users\Vision\Downloads\00100sPORTRAIT_00100_BURST20180809203353818_COVER.jpg") #Using custom image path.
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)