import cv2
import mediapipe as mp
import HandTrackingModule as htm
from pynput.keyboard import Controller,Key
cap=cv2.VideoCapture(0)
detector=htm.HandDetector()
keyboard=Controller()

while True:
    success,img=cap.read()
    img = cv2 .resize(img, (640, 480))
    img=cv2.flip(img,1)
    hands, _  = detector.findHands(img)
    if hands:
        # keyboard.press(Key.up)
        lmList = []
        lmListLe = []
        if len(hands) > 1:
            if hands[0]['type'] == 'Right':
                lmList = hands[0]['lmList']
                lmListLe = hands[1]['lmList']
            else:
                lmListLe = hands[0]['lmList']
                lmList = hands[1]['lmList']
        else:
            if hands[0]['type'] == 'Right':
                lmList = hands[0]['lmList']
            if hands[0]['type'] == 'Left':
                lmListLe = hands[0]['lmList']
        if lmListLe:
            l, _, _ = detector.findDistance(lmListLe[8][:2], lmListLe[12][:2], img)
            l1,_,_=detector.findDistance(lmListLe[4][:2],lmListLe[8][:2],img)
            if l1<50:
                keyboard.press(Key.space)
            else:
                keyboard.release(Key.space)
            if l < 50:
                if l1<50:
                    keyboard.press('s')
                keyboard.press(Key.left)
            else:
                keyboard.release(Key.left)
                keyboard.release('s')
        if lmList:
            l, _, _ = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
            l1,_,_=detector.findDistance(lmList[4][:2],lmList[8][:2],img)
            if l1<50:
                keyboard.press(Key.enter)
                keyboard.press('w')
            if l < 50:
                # if l1<50:
                #     keyboard.press(Key.space)
                keyboard.press(Key.right)
                delayCounter = 1
            else:

                keyboard.release(Key.right)
                keyboard.release(Key.space)
                keyboard.release(Key.enter)
        else:
            keyboard.press('s')
            # cv2.putText(img,str(total),(20,70),cv2.FONT_HERSHEY_PLAIN,8,(255,0,255),3)
    cv2.imshow("Asphalt",img)
    cv2.waitKey(1)