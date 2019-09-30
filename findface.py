import cv2
import time
FACE_NO = 0
def faceDetect():
    capture = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    playing = 1
    while True:

        ret,frame = capture.read()
        grayOfFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(grayOfFrame,scaleFactor =1.5,minNeighbors =5)
        FACE_NO = len(faces)

        colour = (0,0,255)
        stroke = 2

        for (x,y,w,h) in faces:
            if FACE_NO >0:
                width,height = x+w,y+h
                cv2.rectangle(frame,(x,y),(width,height),colour,stroke)
                cv2.putText(frame,'Found Face',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
            #playing = 1
            else:
            #    playing = 0
                pass
        if playing ==1 and FACE_NO>0:
                   playing = 1
                   state = "playing"
                   pass
        if playing ==1 and FACE_NO<1:
                playing = 0
                state = "pausing..."
                pause()
        if playing == 0 and FACE_NO>0:
                playing = 1
                state = "playing"
                pause()
        if playing == 0 and FACE_NO<1:
                playing = 0
                state = "pausing"
                pass
        print(FACE_NO,state)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

def pause():
    import pyautogui as p
    #p.click(p.size()[0]/2,p.size()[1]/2)
    p.hotkey('space')





faceDetect()
