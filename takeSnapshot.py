import cv2

def take_snapshot():
        #Initialing cv2 to start the webcam
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
                #Read the frames while the camera is on
                ret,frame = videoCaptureObject.read()
                #cv2.imwrite is a method used to save an image to any storage device
                cv2.imwrite("newPicture1.jpg",frame)
                result = False
        #release Camera
        videoCaptureObject.release()
        #closes all the windows
        cv2.destroyAllWindows()

take_snapshot()

