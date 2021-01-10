from djitellopy import tello
import pygame
import KeyboardModule as km
from time import sleep
import cv2

white = (255,255,255);
green = (0, 255, 0)
blue = (0, 0, 128)
win = pygame.display.set_mode((1280,768))
pygame.display.set_caption('DroneMetrics')
pygame.font.init()
myfont = pygame.font.SysFont('Helvetica', 20)
batterysurface = myfont.render('Battery:' + '' + '%', False, (0, 0, 0))
wifisurface = myfont.render('Wifi:' + '' + '%', False, (0, 0, 0))
attitudesurface = myfont.render('Attitude:' + '' + '%', False, (0, 0, 0))
barometersurface = myfont.render('Barometer:' + '' + '%', False, (0, 0, 0))
flighttimesurface = myfont.render('Flighttime:' + '' + '%', False, (0, 0, 0))

km.init()
drone = tello.Tello()
drone.connect()
drone.streamon()

def getKeyboardInput():
    lr,fb,ud,yv = 0,0,0,0
    speed = 50

    if km.getKey("a"): lr = -speed
    elif km.getKey("d"): lr = speed

    if km.getKey("w"): fb = speed
    elif km.getKey("s"): fb = -speed

    if km.getKey("z"): ud = speed
    elif km.getKey("c"): ud = -speed

    if km.getKey("q"): yv = -speed
    elif km.getKey("e"): yv = speed

    if km.getKey("l"): yv = drone.land()
    if km.getKey("t"): yv = drone.takeoff()

    return [lr,fb,ud,yv]

while True:
    batterystr = str(drone.get_battery())
    wifistr = str(drone.get_wifi())
    attitudestr = str(drone.get_attitude())
    barometerstr = str(drone.get_barometer())
    flighttimestr = str(drone.get_flight_time())
    batterysurface = myfont.render('Battery:' + batterystr + '%', False, (0, 0, 0))
    wifisurface = myfont.render('Wifi:' + wifistr + '%', False, (0, 0, 0))
    attitudesurface = myfont.render('Attitude:' + attitudestr + 'cm', False, (0, 0, 0))
    barometersurface = myfont.render('Barometer:' + barometerstr + 'cm', False, (0, 0, 0))
    flighttimesurface = myfont.render('Flighttime:' + flighttimestr, False, (0, 0, 0))
    win.fill(white)
    win.blit(batterysurface, (0, 0))
    win.blit(wifisurface, (0, 20))
    win.blit(attitudesurface, (0, 40))
    win.blit(barometersurface, (0, 60))
    win.blit(flighttimesurface, (0, 80))
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    cam = drone.get_frame_read().frame
    cam = cv2.resize(cam,(800,600))
    cv2.imshow("Drone Cam",cam)
    cv2.waitKey(1)
    pygame.display.update()
