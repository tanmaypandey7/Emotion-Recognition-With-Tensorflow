from PIL import Image
import face_recognition
import cv2
import os 
def face_crop(path):
	# Load the jpg file into a numpy array
	image = face_recognition.load_image_file(path)

	# Find all the faces in the image using the default HOG-based model.
	# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
	# See also: find_faces_in_picture_cnn.py
	face_locations = face_recognition.face_locations(image)

	print("I found {} face(s) in this photograph.".format(len(face_locations)))
	f_directory=r"D:\PYTHON\Scripts\emotion recognition\processed dataset\sad_person_face"
	i='a'
	for face_location in face_locations:
	    
	    # Print the location of each face in this image
	    top, right, bottom, left = face_location
	    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
	    sub_face = image[top:bottom, left:right]	

	    drive, path_and_file = os.path.splitdrive(path)
	    _, file = os.path.split(path_and_file)
	    
	    to_paste_path=f_directory+file
	    image_to_write = cv2.cvtColor(sub_face, cv2.COLOR_RGB2BGR)
	    ## Change here the Desired directory.
	    # print ("Writing: " + path + "   to {}".format(f_directory +"\\"+file[:-4]+i))
	    cv2.imwrite(f_directory +"\\"+file[:-4]+i+".jpg", image_to_write)	    
	    i=chr(ord(i) + 1)

	    # You can access the actual face itself like this:
	    # face_image = image[top:bottom, left:right]
	    # pil_image = Image.fromarray(face_image)
	    # pil_image.show()



for i in os.listdir(r"D:\PYTHON\Scripts\emotion recognition\dataset\sad_person_face"):
	face_crop(r"D:\PYTHON\Scripts\emotion recognition\dataset\sad_person_face"+"\\"+i)