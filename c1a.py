import numpy as np
'''
def dist(A,B):
    d=np.sqrt(np.sum(A-B)**2)
    print("d:  ",d)
    return d
'''
import cv2
import matplotlib.pyplot as plt
image=np.zeros((242,512,3),np.uint8)
#pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=np.array([[10,10],[201,201]],np.int32)
print(pts[0][1])
print(pts[1])
radius=4
#cv2.circle(image,(pts[0][0]-radius,pts[0][1]-radius), radius, (0,0,255), -1)
i=3
x=1
a=pts[0]
b=pts[1]
c=a[0]
d=a[1]
#print(str(a)+' '+str(type(a)))
while True:
    x=x+1
    image=np.zeros((242,512,3),np.uint8)
    #cv2.imshow("Image",image)
    if (np.sqrt(np.sum(a-b)**2))<2:
        break
    cv2.circle(image,(c-radius,d-radius), radius, (0,0,255), -1)
    cv2.circle(image,(b[0]-radius,b[1]-radius), radius, (0,255,255), -1)
    a=a+(i*(b-a)/np.sqrt(np.sum(a-b)**2))
    #a.astype(int)
    c=int(a[0])
    d=int(a[1])
    #h=input()
    #plt.imshow(image, cmap=plt.cm.gray)
    #cv2.putText(image,"Hello World!!!", (c,d), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("Image",image);
    cv2.circle(image,(c-radius,d-radius), 0, (0,0,255), -1)
    cv2.waitKey(1)
    #print("a:  ",a)
    #print(type(a))

#cv2.destroyAllWindows()
#cv2.polylines(image,[pts],True,(0,255,255))
#cv2.imshow("Image",image)
