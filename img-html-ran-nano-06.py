#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import datetime
import random 
# Set the directory you want to start from

#print('first check')
#rootDir = '.\images'
def getItem(painter):
    imgitem  = ''
    fi = ".\\csv-plist\\"+painter+".csv"
    fimg = open(fi,'r')
    #i = albumid*100
    for item in fimg:
      #i = i + 1
      iarr = item.split('\\')
      iname = iarr[3].replace('\n','')
      #print item
      if len(item) > 5:
         item = item.replace('\n','')
         item = item.replace('.\\images\\','')
         item = item.replace('\\','/')
         #print item
         imark = iname.find('.')
         iname = iname[:imark]
         desc = iname+'    '+painter
         desc = desc.replace('-',' ').title()

         imgitem = imgitem+'<a href="'+item+'" data-ngid="'+iname+'" data-ngalbumid="'\
                   +painter+'" data-ngthumb="'+item+'">'\
                   +desc+'</a>\n'
    
    return imgitem
def getInstr(inum,iend,parr):
    i = inum
    instr = ""
    for i in range(inum,iend):
        narr = parr[i].split('\\')
        i = i + 1
        #print i
        #print parr[i]
        if  len(narr)>3:
              painter = narr[2]
              name = painter.split('-')
              #painterarr.append(painter)
              lastname = name[-1]
              fullname = painter.replace('-','')
              pic = narr[3]
              pic=  pic.split('.')[0]
              painter = painter.replace('-',' ').title()
              pic = pic.replace('-',' ').title()
              #print (painter)
              #print (pic)
              status =  painter+'\n'+pic
              status = status.title()
              #hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
              #status = status
              desc = pic+' '+painter
              desc = desc.title()
              imgsrc = narr[2]+'/'+narr[3]
              imgsrc = "images/"+imgsrc.replace('\n','')
              lstr = narr[2]+'/'+narr[3]
              lstr = lstr.replace('\n','')
         #print imgsrc
              
              imgstr = '\n<a href=""  data-ngkind="album" data-ngid="'+narr[2]+'" data-ngthumb="'\
                 + lstr +'">'+painter+'</a>\n'
              #print imgstr
              instr = instr+imgstr
              imgitem = getItem(narr[2])
              instr = instr+imgitem
    return instr


def ranfile(parr,outhtml,thtml):
    
    fout = open(outhtml,'w')
    
    fhtml = open(thtml,'r')
    htmlstr = fhtml.read()
    sgg = '<!-- first album -->'
    tlen = len(sgg)
    mark = htmlstr.find(sgg)+tlen
    instr = ""
    outstr = ""
    #read  template file
    i = 0
    plen = len(parr)
    instr = getInstr(0,plen,parr)
    

    

#outstr = '"<div id="gallery" style="display:none;">'+instr+'</div>'
#print mark
    outstr = htmlstr[:mark]+instr+htmlstr[mark:]
     

    fout.write(outstr)


def getLine(csvfile):
    larr = []
    fcsv = open(csvfile,'r')
    for line in fcsv:
        larr.appen(line)
    return larr
  
pfile = ".\\csv\\all-painters.csv"
parr = getLine(pfile)
random.shuffle(parr)
ranfile(parr,listf,thtml)
#parr = sorted(parr)
#print parr
#now =  datetime.datetime.now()
#timestr = str(now).replace(' ','-').replace(':','-')
#print now
listf = "al-06.html"
#print timestr[0:19]
thtml = "nano-06.html"
print thtml,listf






 