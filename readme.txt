auto twit setup

1.check last update, using painter name in dynamodb imglist, upload image files to S3, images?
2.SSH to EC2, twipro\list_images1.py  param: [dir:images?, file:images?.txt]
3. backup dynamoDB, export imglist items to csv file
4. run list_dyn2.py, param: [images?.txt,]
5. twit: local
    lambda: lamb_img.py

auto twit setup axu:
1. upload images to S3 photo?
2. SSH to EC2, run list_photo.py
3. backup dynamoDB photo
4. run list_photo.py


retwit:
local: retwi-01.py

axu twit:
img_down_gre.py download from twit acc
img_mongo_gre.py  inser
lt to mongo DB
img_list_axu.py  twit
lamb_img_list_axu.py  lambda twit


list file names in directory:
dir-tree-02.py   param: [rootdir: .\images, output file: flist?.txt]

 
download images from twit:
pic_list.py  get image url   param:[input twit accs: xxx_list.txt, output: xxx_url.txt]
pic_down.py  download image  param:[input: xxx_url.txt,  download dir: \pics, \videos]


build web site:
img-tree-02.py   list image files    param: [dir, output file: img-?.csv]
img-tree-03.py   list image files    param: [dir, output file: allimages?.csv]
img-tree-dup-01.py  check and delete duplicated images files 
                       params:[duplicate to del: all-del-images.csv]

img-html-100.py      write unitegallery html files  
                     param:[input file: img-?.csv, output file: img-html-?.html template:img-html-100-?.html]
img-html-gg-05.py   write gammagallery htmls
                  param:[input file: img-?.csv, output file:img-html-gg-?.html
                   template gg-?.html]
dir-img.py       param: [rootdir: .\images, output file: flist?.txt]
list_painter_html.py   list painters params:[input:flist?.csv, ouput: painterlist?.html]
list_painter_csv.py    list painters params:[input:flist?.csv, ouput: painterlist?.csv]
dir-painting.py        writer painter's painting list 
                       params:[input painterlist?.csv, output painter-name.csv]
img-html-painter-list-00.py    write gammagallery htmls for painters
                        params:[input: painterlist?.csv, output: paintername-?.html]

img-html-random-01.py   listing random pics 
                     param:[input file: img-?.csv, output file:img-html-gg-?.html
                                template gg-?.html]

img-html-load.py       listing random pics  in img html with infinite load
                       param:[input file: allimages?.csv, output file:img-html-gg-?.html
                                template gg-?.html]


aws
deploy.py              upload files to s3  
                       params:[dir: dist, bucketname:artlisastage for zip:out]

// web server
python -m SimpleHTTPServer 2000

//links
http://www.lambdatwist.com/s3-hosting-guide/   upload to s3
https://linuxacademy.com/howtoguides/posts/show/topic/14209-automating-aws-with-python-and-boto3   aws python boto3






