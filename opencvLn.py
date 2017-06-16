import numpy as np
import cv2
#print(cv2.useOptimized())
#img=cv2.imread("logo.png",cv2.IMREAD_COLOR)
#cv2.imshow("image",img)
#cv2.waitKey(0)

img=cv2.imread("test.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("re.jpg",gray)
edges=cv2.Canny(gray,50,150,apertureSize=3)
cv2.imwrite("re1.jpg",edges)
minLineLength=500
maxLineGap=10
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
linenum=len(lines)
print(linenum)
i=0
while i<linenum:
	for x1, y1, x2, y2 in lines[i]:
		cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
	i=i+1


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.imwrite("houghlines2.jpg",img)
