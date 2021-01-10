# Not Working yet didn't finish the
# threading yet but if you put the
# keys() and streams() into while
# True loop it will work again only
# pauses because the picture and the
# command can not be sent at the same time

from djitellopy import Tello
from threading import Thread
import cv2,math,time



tello = Tello()
tello.connect()
tello.get_battery()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.get_battery()

def keys():
 while True:
    key = cv2.waitKey(1) & 0xff
    if key == 27:  # ESC
        break
    elif key == ord('w'):
        tello.move_forward(20)
    elif key == ord('s'):
        tello.move_back(20)
    elif key == ord('a'):
        tello.move_left(20)
    elif key == ord('d'):
        tello.move_right(20)
    elif key == ord('e'):
        tello.rotate_clockwise(20)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(20)
    elif key == ord('z'):
        tello.move_up(20)
    elif key == ord('c'):
        tello.move_down(20)


tello.land()

def streams():
    while True:
        key = cv2.waitKey(1) & 0xff
        if key == 27:  # ESC
            break
    img = frame_read.frame
    cv2.imshow("StreamFromTheDroneWindow", img)
    thread1 = streams()
    thread2 = keys()
    thread1.start()
    thread2.start()



