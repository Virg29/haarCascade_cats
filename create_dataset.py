import sys
if __name__ == "__main__":
    argv=sys.argv[1:]
    args=dict()
    for param in argv:
    	if(param!=None):
    		try:
    			args[param.split('=')[0]]=param.split('=')[1]
    		except IndexError as e:
    			raise Exception('Args parsing error')
if(len(args)!=4):
	print('#count=последняя цифра файла в папке')
	print('#file=название файла с датасетом')
	print('#type=neg/pos')
	print('#path=путь до папки с фото ./asd/aaa/')
else:
	counter=int(args['count'])+1
	file=open(args['file'],'w')
	for i in range(counter):
		if(args['type']=="neg"):
			file.write(args['path']+str(i)+'.jpg\n')
		elif(args['type']=="pos"):
			file.write(args['path']+str(i)+'.jpg 1 100 100 0 0\n')