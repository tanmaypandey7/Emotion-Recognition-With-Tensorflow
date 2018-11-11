import cv2
import label_image

size = 4


# We load the xml file
classifier = cv2.CascadeClassifier(r"D:\PYTHON\Scripts\emotion recognition\Emotion-Recognition-With-Tensorflow\haarcascade_frontalface_default.xml")

# webcam=cv2.VideoCapture(r"C:\Users\Vision\Videos\VID_20181105_132135.mp4") #Using custom video path.

# while True:
#     (rval, im) = webcam.read()
#     # im=cv2.flip(im,1,0) #Flip to act as a mirror

#     # Resize the image to speed up detection
#     mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

#     # detect MultiScale / faces 
#     faces = classifier.detectMultiScale(mini)

#     # Draw rectangles around each face
#     for f in faces:
#         (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
#         cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        
#         #Save just the rectangle faces in SubRecFaces
#         sub_face = im[y:y+h, x:x+w]

#         FaceFileName = "test.jpg" #Saving the current image from the webcam for testing.
#         cv2.imwrite(FaceFileName, sub_face)
        
#         text = label_image.main(FaceFileName)# Getting the Result from the label_image file, i.e., Classification Result.
#         text = text.title()# Title Case looks Stunning.
#         font = cv2.FONT_HERSHEY_TRIPLEX
#         cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)

#     # Show the image
#     cv2.imshow('Capture',   im)
#     key = cv2.waitKey(10)
#     # if Esc key is press then break out of the loop 
#     if key == 27: #The Esc key
#         break
# cap.release()
# cv2.destroyAllWindows()    


#For image emotion recognition

im= cv2.imread(r"C:\Users\Vision\Downloads\00100sPORTRAIT_00100_BURST20180809203353818_COVER.jpg") #Using custom image path.
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
while True:
    # (rval, im) = webcam.read()
    # # im=cv2.flip(im,1,0) #Flip to act as a mirror

    # # Resize the image to speed up detection
    mini = cv2.resize(gray, (int(gray.shape[1]/size), int(gray.shape[0]/size)))

    # # detect MultiScale / faces 
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        
        #Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y+h, x:x+w]

        FaceFileName = "test.jpg" #Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        
        text = label_image.main(FaceFileName)# Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()# Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)

    # Show the image
    cv2.imshow('Capture',   im)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop 
    if key == 27: #The Esc key
        break
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows() 