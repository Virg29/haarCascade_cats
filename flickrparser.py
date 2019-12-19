from bs4 import BeautifulSoup as bs
a = open('./lickr.html','rb')
info=a.read().decode('utf-8')
a.close()
soup=bs(info)
divs=soup.findAll('div',{'class':'photo-list-photo-view'})
listFlickr = open('./listFlickr.txt','w')

for i in divs:
	listFlickr.write(str(i['style'].split(';')[:-1][-1:][0][26:-2])+'\n')
listFlickr.close()

#print(soup.prettify())