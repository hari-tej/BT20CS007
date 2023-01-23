import numpy as np
import cv2
import matplotlib.pyplot as plt
image=np.zeros((500,500,3),np.uint8)
a=[10,10]
ta=a
b=[10,90]
c=[90,90]
d=[90,10]
dist1=np.sqrt(sum(np.subtract(a,b)**2))
dist2=np.sqrt(sum(np.subtract(b,c)**2))
dist3=np.sqrt(sum(np.subtract(c,d)**2))
dist4=np.sqrt(sum(np.subtract(d,a)**2))
#d=int((dist1+dist2+dist3)/3)
#print(d)
f=1
i=0
rad=2
while f==1:
    image=np.zeros((500,500,3),np.uint8)
    #print(i)
    #cv2.putText(image,"j", (a[0]-rad,a[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    if(i<dist1):
        a=np.add(a,np.array(i*(np.array(np.subtract(b,a))))/dist1)
        a=a.astype(int)
        cv2.putText(image,".", (a[0]-rad,a[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    elif(i<dist1+dist2):
        b=np.add(b,np.array((i-dist1)*(np.array(np.subtract(c,b))))/dist2)
        b=b.astype(int)
        cv2.putText(image,".", (b[0]-rad,b[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (155,0,1))
    elif(i<dist1+dist2+dist3):
        c=np.add(c,np.array((i-dist1-dist2)*(np.array(np.subtract(d,c))))/dist3)
        c=c.astype(int)
        cv2.putText(image,".", (c[0]-rad,c[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,1,255))
    elif(i<dist1+dist2+dist3+dist4):
        d=np.add(d,np.array((i-dist1-dist2-dist3)*(np.array(np.subtract(ta,d))))/dist3)
        d=d.astype(int)
        cv2.putText(image,".", (d[0]-rad,d[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,145,25))
    else:
        f=0
    #cv2.circle(image,(a[0]-rad,a[1]-rad), rad, (0,0,255), -1)
    #cv2.circle(image,(b[0]-rad,b[1]-rad), rad, (0,255,255), -1)
    #cv2.circle(image,(c[0]-rad,c[1]-rad), rad, (255,0,255), -1)
    i=i+1
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    #cv2.waitKey(0)
