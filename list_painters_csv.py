import random

narr=[]
fo = open('.\\csv\\all-images.csv','r')
ofile = ".\\csv\\all-painters.csv"
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
pl = list(set(painterarr))
pl = sorted(pl)
#random.shuffle(pl)
for pai in pl :
    pailist = pailist +pai+'\n'
#print pailist

 
fout.write(pailist)
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
