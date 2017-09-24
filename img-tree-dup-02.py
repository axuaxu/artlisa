#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import re
 
# Set the directory you want to start from

print('first check')
rootDir = '.\images'


def flist():
#  t="dir,name,twi,extra\n"
  t = ""
  d = ""
  for dirName, subdirList, fileList in os.walk(rootDir):
   # print('Found directory: %s' % dirName)
     
    for fname in fileList:
    	if ('(' in fname):
           #print('\t%s' % fname)
           d = d+dirName+'\\'+fname+'\n'
        t = t+dirName+'\\'+fname+'\n'
  return t,d

# writing csv

 
ft,fd = flist()  
with open('.\\csv\\allimages.csv', 'wb') as f:
      f.write(ft)
with open('.\\csv\\all-dup-images.csv', 'wb') as f:
      f.write(fd)


fin = open('.\\csv\\all-dup-images.csv', 'r')
fall = open('.\\csv\\allimages.csv', 'r')
allarr=[]
fo = ''
ft = ''
for aim in fall:
    allarr.append(aim)
for images in  fin :
	#print images
	if  'untitled' not in images:

	     sm = images.find('(')
	     images1 = images[:sm-1]+images[sm+3:].replace(' ','')
	     #print images
	     #fo = fo + images
	     if images1 in allarr:
	     	 #print images
	     	 fo = fo + images1
	     	 ft = ft + images
	     #print images
	     #fo = fo + images
		 #images = images.replace('(1)','')
		 #bool(re.search('ba[rzd]', 'foobarrrr'))
         #if (images in ft):
with open('.\\csv\\all-org-images.csv', 'wb') as f:
      f.write(fo)
with open('.\\csv\\all-del-images.csv', 'wb') as f:
      f.write(ft)

fdel = open('.\\csv\\all-del-images.csv','r') 
for idel in fdel:
   idel = idel.replace('\n','')
   os.remove(idel)
   print  "deleted" , idel, 
