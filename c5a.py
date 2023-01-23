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
for i in range(0,d):
    #print(i)
    image=np.zeros((500,500,3),np.uint8)
    a=np.add(a,np.array(i*(np.array(np.subtract(b,a))))/dist1)
    b=np.add(b,np.array(i*(np.array(np.subtract(c,b))))/dist2)
    c=np.add(c,np.array(i*(np.array(np.subtract(a,c))))/dist3)
    a=a.astype(int)
    b=b.astype(int)
    c=c.astype(int)
    #cv2.putText(image,'OpenCV',(10,500), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(image,".", (a[0]-rad,a[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    cv2.putText(image,".", (b[0]-rad,b[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (155,0,1))
    cv2.putText(image,".", (c[0]-rad,c[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,1,255))
    #cv2.circle(image,(a[0]-rad,a[1]-rad), rad, (0,0,255), -1)
    #cv2.circle(image,(b[0]-rad,b[1]-rad), rad, (0,255,255), -1)
    #cv2.circle(image,(c[0]-rad,c[1]-rad), rad, (255,0,255), -1)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    #cv2.waitKey(0)
