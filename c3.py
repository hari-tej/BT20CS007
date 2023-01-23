import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
image=np.zeros((500,500,3),np.uint8)
radius=201
p=int(2*3.14*radius)
c=[250,250]
a=c[0]
b=c[1]
for i in range(0,p):
    #print(i)
    x=int(a+(math.cos(-i/10)*radius))
    y=int(b+(math.sin(-i/10)*radius))
    cv2.putText(image,".", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("Image",image)
    cv2.waitKey(1)
