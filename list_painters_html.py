
narr=[]
fo = open('flist-01.csv','r')
ofile = "painterlist-01.html"
fout = open(ofile,'w')
painterarr=[]
for line in fo:
  #nstr =  line['name'].encode('utf-8').replace('\n','')
  narr = line.split('\\')
  #print(len(narr))
  if  len(narr)==4:
    painter = narr[2]
    painterarr.append(painter)
    pic = narr[3]
    pic=  pic.split('.')[0]
    painter = painter.replace('-',' ')
    pic = pic.replace('-',' ')
    #print (painter)
    #print (pic)
    status =  painter+'\n'+pic
    status = status.title()

pailist =""
pl = sorted(list(set(painterarr)))
for pai in pl :
    paistr = '<li><a = href="'+pai+'.html">'+pai.replace('-',' ')+'</a></li>'
    pailist = pailist + ' ' +paistr
#print pailist

headstr = "<html><body><ul>"
footerstr = "</ul></body></html>"
outstr = headstr+pailist+footerstr
fout.write(outstr)
print ofile
print len(pl)
#     print(myb,nstr,tmpf)
    #boto3.client('s3').download_file(myb,nstr,tmpf)
    #file = open(tmpf,'rb')
    #api.update_with_media(tmpf, status=status)
    #table.delete_item(
    #     Key={
     #      'name': item['name'],
     #  })
