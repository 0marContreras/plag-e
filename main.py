import motorController
from laneDetectionModule import getLaneCurve
import webCamModule
import time
import cv2
 

def main():
    img = webCamModule.getImg()
    curveVal = getLaneCurve(img, 1)
    #motorController.foward()

    # Parte izquierda - Control de la variable curveVal
    if curveVal > 0:
        motorController.right()
        if curveVal < 0.05:  
            motorController.left()
       	      
       	    curveVal = 0
    # Fin de la parte izquierda

    # Parte derecha - Control de la variable curveVal
    else:
        if curveVal > -0.08:
     
            motorController.foward()
             
            curveVal = 0
    # Fin de la parte derecha




    # Parte común - Visualización de la imagen
    #cv2.imshow('debug', img)
    #cv2.waitKey(1)
    # Fin de la parte común

if __name__ == '__main__':
    while True:
        main()
