#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
 
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
           print('\t%s' % fname)
           d = d+dirName+'\\'+fname+'\n'
        t = t+dirName+'\\'+fname+'\n'
  return t,d

# writing csv
 
ft,fd = flist()  
with open('.\\csv\\allimages.csv', 'wb') as f:
      f.write(ft)
with open('.\\csv\\all-dup-images.csv', 'wb') as f:
      f.write(fd)
 