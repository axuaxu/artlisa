#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import datetime
import random 
# Set the directory you want to start from

#print('first check')
#rootDir = '.\images'

 
def ranfile(parr,outhtml,thtml):
    
    fout = open(outhtml,'w')
    
    fhtml = open(thtml,'r')
    htmlstr = fhtml.read()
    sgg = '<ul class="gamma-gallery">'
    tlen = len(sgg)
    mark = htmlstr.find(sgg)+tlen
    instr = ""
    outstr = ""
    #read  template file
    i = 0
    plen = len(parr)
    for i in range(0,plen):
   
       print i,parr[i]
       pstr = parr[i].replace('\n','')
       pcsv = ".\\csv\\"+pstr+".csv"
       fpcsv = open(pcsv,'r')
       imgarr = []
       i = i + 1
       for painting in fpcsv:
           imgarr.append(painting)
       random.shuffle(imgarr)
       #paintinglist = paintinglist.append(imgarr[0])
	      #print line
       narr = imgarr[0].split('\\')
	      #print len(narr)
       if  len(narr)>3:
              painter = narr[2]
              name = painter.split('-')
              #painterarr.append(painter)
              lastname = name[-1]
              fullname = painter.replace('-','')
              pic = narr[3]
              pic=  pic.split('.')[0]
              painter = painter.replace('-',' ')
              pic = pic.replace('-',' ')
              #print (painter)
              #print (pic)
              status =  painter+'\n'+pic
              status = status.title()
              #hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
              #status = status
              desc = painter+' '+pic
              desc = desc.title()
              imgsrc = narr[2]+'/'+narr[3]
              imgsrc = "images/"+imgsrc.replace('\n','')
        
         #print imgsrc
              imgstr = '<li><div  data-alt="'+imgsrc+'" data-description="<h3>'+desc \
                + '</h3>" data-max-width="1800" data-max-height="1350"><div data-src="' \
                +imgsrc+'" data-min-width="1300"></div><div data-src="' \
                +imgsrc+'" data-min-width="1000"></div><div data-src="' \
                +imgsrc+'" data-min-width="700"></div><div data-src="'  \
                +imgsrc+'" data-min-width="300"></div><div data-src="'  \
                +imgsrc+'" data-min-width="200"></div><div data-src="'  \
                +imgsrc+'" data-min-width="140"></div><div data-src="'  \
                +imgsrc+'"></div><div data-src="'+imgsrc+'"></div><noscript><img src="' \
                +imgsrc+'" alt="img03"/></noscript></div></li>'
               
              #print imgstr
              instr = instr+imgstr

#outstr = '"<div id="gallery" style="display:none;">'+instr+'</div>'
#print mark
    outstr = htmlstr[:mark]+instr+htmlstr[mark:]
    sgg2 = "items = ['"
    tlen2 =len(sgg2)
    mark2 = outstr.find(sgg2)+tlen2
    outstr = outstr[:mark2]+instr+outstr[mark2:]

    #sgg3 = "</header>"
    #tlen3 =len(sgg3)
    #mark3 = outstr.find(sgg3)+tlen3
    #pailist =""
    #for pai in list(set(painterarr)):
    #    pailist = pailist + ' ' +pai
    #outstr = outstr[:mark3]+pailist+outstr[mark3:]
    fout.write(outstr)




pfile = ".\csv\painterlist-01.csv"
fp = open(pfile,'r')
parr = []
for painter in fp:
    parr.append(painter)
random.shuffle(parr)
#print parr
now =  datetime.datetime.now()
timestr = str(now).replace(' ','-').replace(':','-')
#print now
print timestr[0:16]
listf = ".\index-00"+'.html'
thtml = "gg-01.html"
ranfile(parr,listf,thtml)





 