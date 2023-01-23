import numpy as np
import cv2
import matplotlib.pyplot as plt
image=np.zeros((500,500,3),np.uint8)
a=[10,10]
b=[200,200]
c=[400,50]
dist1=np.sqrt(sum(np.subtract(a,b)**2))
dist2=np.sqrt(sum(np.subtract(b,c)**2))
dist3=np.sqrt(sum(np.subtract(c,a)**2))
d=int((dist1+dist2+dist3)/3)
#print(d)
rad=2
v=0.01
for i in range(0,d):
    image=np.zeros((500,500,3),np.uint8)
    #print(i)
    a=np.add(a,np.array(v*i*(np.array(np.subtract(b,a))))/dist1)
    b=np.add(b,np.array(v*i*(np.array(np.subtract(c,b))))/dist2)
    c=np.add(c,np.array(v*i*(np.array(np.subtract(a,c))))/dist3)
    a=a.astype(int)
    b=b.astype(int)
    c=c.astype(int)
    cv2.circle(image,(a[0]-rad,a[1]-rad), rad, (0,0,255), -1)
    cv2.circle(image,(b[0]-rad,b[1]-rad), rad, (0,255,255), -1)
    cv2.circle(image,(c[0]-rad,c[1]-rad), rad, (255,0,255), -1)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
