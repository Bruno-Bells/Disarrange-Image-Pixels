######################################################################
#                                                                    #
#              Flip Image Pixels Using Opencv 3                      #
#                to generate a different image                       #
#                                                                    #
#    This code is brought to you by Bruno C, Odinukweze              #
#     as an early research in my journey in computer Vision.         #
#        Email me: brunofreelancing@gmail.com                        #
#                                                                    #
######################################################################

######################################################################
#                                                                    #
#    This version of this code will convert every image to gray.     #
#                                                                    #
######################################################################


# Import the necessary packages 
import numpy as np
import cv2

# load the camera(webcam) and assign it to the variable   cap
cap = cv2.VideoCapture(0) # webcam

# check if the camera is opened
if cap.isOpened():
    ret, frame = cap.read()
# if the camera is not opened stop the cap
else:
    cap = False

# The path we will save the image to be captures | So that we can access it
img = 'c:\\users\\sabinus o ofoleta\\desktop\\summer1.jpg' # path to save the image

# # the image to be read and displayed | you can see that it's the same image that we saved earlier | img
img1 = 'c:\\users\\sabinus o ofoleta\\desktop\\summer1.jpg' # path to the image

Fliped = 'c:\\users\\sabinus o ofoleta\\desktop\\fliped.jpg' # path to the image

# save the image to the disk | img =  | You can 
cv2.imwrite(img, frame)

# read the saved image from the disk and convert the image to gray a scale image
image = cv2.imread(img1, 0)
np.shape(image)
# print(image.shape)
# we define a function called main(). It will contain all our code that will do the trick 
def main():
	# we get the number of rows in the image| so that we can flip it
    width = image.max(axis=1).shape
	# we get the number of columns in the image 
    height = image.max(axis=0).shape
	# we do for loop to convert the width from tuple to string
    for i in width:
        w = ("%s" % i)
		# we convert the string(w) to integer. 
        w = int(w)
        # print('w',w)
	# we do for loop to convert the height from tuple to string
    for r in height:
       h = ("%s" % r)
	   # we convert the string(h) to integer. 
       h = int(h)
    #    print('h',h)
    # we reshape the image to h,w instead of w,h
    im = image.reshape(h,w)
	
    cv2.imwrite(Fliped, im)
	# we display the image to the screen
    cv2.imshow("Fliped image",im)
    cv2.waitKey(0)

if __name__=="__main__":
    main()
