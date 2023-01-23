import numpy as np
import cv2
import matplotlib.pyplot as plt
image=np.zeros((500,500,3),np.uint8)
a=[10,50]
ta=a
b=[50,90]
tb=b
c=[90,50]
tc=c
d=[50,10]
td=d
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
    a=np.add(a,np.array(i*(np.array(np.subtract(tb,a))))/dist1)
    a=a.astype(int)
    cv2.putText(image,".", (a[0]-rad,a[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    b=np.add(b,np.array((i)*(np.array(np.subtract(tc,b))))/dist2)
    b=b.astype(int)
    cv2.putText(image,".", (b[0]-rad,b[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (155,0,1))
    c=np.add(c,np.array((i)*(np.array(np.subtract(td,c))))/dist3)
    c=c.astype(int)
    cv2.putText(image,".", (c[0]-rad,c[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,1,255))
    d=np.add(d,np.array((i)*(np.array(np.subtract(ta,d))))/dist3)
    d=d.astype(int)
    cv2.putText(image,".", (d[0]-rad,d[1]-rad), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,145,25))
    i=i+1
    if(np.sqrt(sum(np.subtract(a,tb)**2))==0):
        a=ta
        b=tb
        c=tc
        d=td
        i=0
    cv2.imshow("Image",image)
    cv2.waitKey(1)
    #cv2.waitKey(0)
