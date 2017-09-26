#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import random 
# Set the directory you want to start from

#print('first check')
#rootDir = '.\images'



# writing csv
 
pfile = ".\\csv\\all-painters.csv"
outf = ".\\csv\\all-img-random.csv"
fo = open(outf,'w')
fp = open(pfile,'r')
choose = ''
for painter in fp:
    painter = painter.replace('\n','')
    listf = ".\\csv-plist\\"+painter+'.csv'
    plistcsv = open(listf,'r')
    parr = []
    for pimg in plistcsv:
           if len(pimg) > 5:
              parr.append(pimg)
    random.shuffle(parr)
    choose = choose+parr[0]
fo.write(choose)
print outf
    #print choose  

    


 