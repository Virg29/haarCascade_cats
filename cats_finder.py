from requests import get
from time import sleep
import cv2
filename='./stream.jpg'
if __name__ == '__main__':
	one=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
	two=cv2.imread(filename)
	cascade = cv2.CascadeClassifier('E:\\python\\haarCascade_cats\\haarcascade\\1.xml')
	face = cascade.detectMultiScale(one,1.05,5)
	for (x,y,w,h) in face:
		cv2.rectangle(two,(x,y),(x+w,y+h),(255,0,0),2)
	#cv2.imwrite(filename,two)
	cv2.imshow('Frame',two)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	#file = open('./stream.jpg','wb')
	#a = get(info)
	#print(a)
	#file.write(a.content)
	#file.close()







	#cv2.imshow('frame',gray)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()