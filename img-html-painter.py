incsv = "img-01.csv"
fin = open(incsv,'r')
outhtml = "img-html-gg-06.html"
fout = open(outhtml,'w')
thtml = "gg-01.html"
fhtml = open(thtml,'r')
htmlstr = fhtml.read()
sgg = '<ul class="gamma-gallery">'
tlen = len(sgg)
mark = htmlstr.find(sgg)+tlen
instr = ""
outstr = ""
#read  template file
painterarr=[]
i = 0
for line in fin:
  if i < 20:
     i = i+1
	  #print line
     narr = line.split('\\')
	#print len(narr)
     if  len(narr)>3:
         painter = narr[2]
         name = painter.split('-')
         painterarr.append(painter)
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
         status = status
         desc = painter+' '+pic
         desc = desc.title()
         imgsrc = narr[2]+'/'+narr[3]
         imgsrc = "images/"+imgsrc.replace('\n','')
         
         #items = [<li><div data-alt="img03" 
         #       data-description="<h3>Sky high</h3>" 
         #       data-max-width="1800" 
         #       data-max-height="1350">
         #       <div data-src="images/xxxlarge/3.jpg" data-min-width="1300"></div>
         #       <div data-src="images/xxlarge/3.jpg" data-min-width="1000"></div>
         #       <div data-src="images/xlarge/3.jpg" data-min-width="700"></div>
         #       <div data-src="images/large/3.jpg" data-min-width="300"></div>
         #       <div data-src="images/medium/3.jpg" data-min-width="200"></div>
         #       <div data-src="images/small/3.jpg" data-min-width="140">
         #       </div><div data-src="images/xsmall/3.jpg"></div>
         #       <noscript><img src="images/xsmall/3.jpg" alt="img03"/></noscript>
         #       </div></li>

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
               
         print imgstr
         instr = instr+imgstr

#outstr = '"<div id="gallery" style="display:none;">'+instr+'</div>'
#print mark
outstr = htmlstr[:mark]+instr+htmlstr[mark:]
sgg2 = "items = ['"
tlen2 =len(sgg2)
mark2 = outstr.find(sgg2)+tlen2
outstr = outstr[:mark2]+instr+outstr[mark2:]

sgg3 = "</header>"
tlen3 =len(sgg3)
mark3 = outstr.find(sgg3)+tlen3
pailist =""
for pai in list(set(painterarr)):
    pailist = pailist + ' ' +pai 
outstr = outstr[:mark3]+pailist+outstr[mark3:]
fout.write(outstr)

#print(list(set(painterarr)))


         #<img alt="Image 2 Title" 
	     #     src="thumbs/greece.jpg"
		 #     data-image="images/greece.jpg"
	     #     data-description="Image 2 Description">
	     #print status