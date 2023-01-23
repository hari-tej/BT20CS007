import numpy as np
import cv2
import matplotlib.pyplot as plt
image=np.zeros((500,500,3),np.uint8)
a=[50,90]
b=[90,50]
tb=b
dist1=np.sqrt(sum(np.subtract(a,b)**2))
i=-1
j=-1
t=0
rad=2
while True:
    a=np.add(a,np.array(t*(np.array(np.subtract(b,a))))/dist1)
    a=a.astype(int)
    cv2.circle(image,(a[0]-rad,a[1]-rad), rad, (0,255,255), -1)
    cv2.imshow("Image",image)
    t=t+1
    if(np.sqrt(sum(np.subtract(a,b)**2))==0):
        a=tb
        b[0]=tb[0]+40*i
        b[1]=tb[1]+40*j
        tb=b
        t=0
        if(i==-1 and j==-1):
            j=1
        elif(i==-1):
            i=1
        elif(j==1):
            j=-1
        else:
            i=-1
    cv2.waitKey(1)

