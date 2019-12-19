import requests as r
import cv2
counter=1077
with open('./listFlickr.txt','r') as f:
    for line in f:
    	
    	print(line)
    	try:
    		a=r.get("http://"+line,timeout=(2, 3))
    	except Exception as e:
    		if(e==r.exceptions.ConnectTimeout):
    			print('timeout has been reach')
    		else:
    			print('some different error')
    		continue
    	try:
    		a.headers['content-type']
    	except KeyError as e:
    		print('not-allowed headers')
    		continue
    	if(a.headers['content-type']=="image/jpeg"):
    		filename="./cats/"+str(counter)+"."+line.split('.')[-1:][0].rstrip('\n')
    		new = open(filename,"wb")
    		new.write(a.content)
    		new.close()
    		img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    		img = cv2.resize(img, (100,100), interpolation = cv2.INTER_AREA)
    		cv2.imwrite(filename,img)

    		counter+=1
    		print('success')
    	else:
    		print('failure')
    		continue
        