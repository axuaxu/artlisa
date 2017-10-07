//auto twit setup

1.check last update, using painter name in dynamodb imglist, upload image files to S3, images?
2.SSH to EC2, twipro\list_images1.py, edit file change dir
                   param: [dir:images?, file:images?.txt]
3. backup dynamoDB, export imglist items to csv file
4. edit file, change input file name, run list_dyn2.py, param: [images?.txt,]
5. twit: local
    lambda: lamb_img.py

//auto twit setup axu:
1. upload images to S3 photo?
2. SSH to EC2, list files in photo?, edit and run list_photo.py, 
                                     param[output: photo?.txt]
3. backup dynamoDB photo
4. insert files to dbtable photo,  edit and run list_dyn_photo.py
                                    param[input: photo?.txt]
 
//retwit:
local: retwi-01.py

//axu twit:
pic_list.py    build url list for twi pics 
               param:[input: twi_list.txt acc list, count: 200, maxid:  output: twi_url.txt url list]
pic_down.py    download pic in twi_url.txt
               params:[input: twi_url.txt, pic dir, video dir]

img_down_gre.py download from url links  params:[input: twidown_?.txt]
img_mongo_gre.py  inser
lt to mongo DB
img_list_axu.py  twit
lamb_img_list_axu.py  lambda twit


//list file names in directory:
dir-tree-02.py   param: [rootdir: .\images, output file: flist?.txt]

 
//download images from twit:
pic_list.py  get image url   param:[input twit accs: xxx_list.txt, output: xxx_url.txt]
pic_down.py  download image  param:[input: xxx_url.txt,  download dir: \pics, \videos]


//build web site:
img-tree-02.py   list image files    param: [dir, output file: img-?.csv]
img-tree-03.py   list image files    param: [dir, output file: all-images?.csv]
img-tree-dup-02.py  check and delete duplicated images files 
                       params:[duplicate to del: all-del-images.csv]
list-img-random.py list random painting of a painter
                        params:[input all-painters.csv, csv-plist\painter-name.csv
                                output: all-img-random.csv]

img-html-100.py      write unitegallery html files  
                     param:[input file: img-?.csv, output file: img-html-?.html template:img-html-100-?.html]
img-html-gg-05.py   write gammagallery htmls
                  param:[input file: img-?.csv, output file:img-html-gg-?.html
                   template gg-?.html]
dir-img.py       param: [rootdir: .\images, output file: flist?.txt]
list_painter_html.py   list painters params:[input:flist?.csv, ouput: all-painters.html]
list_painter_csv.py    sorted list painters params:[input:flist?.csv, ouput: all-painters.csv]

dir-painting.py        write painter's painting list 
                       params:[input all-painters.csv, output csv-plist\painter-name.csv]

img-html-painter-list-00.py    write gammagallery htmls for painters
                        params:[input: painterlist?.csv, output: paintername-?.html]

img-html-random-01.py   listing random pics 
                         param:[input file: img-?.csv, output file:img-html-gg-?.html
                                template gg-?.html]

img-html-load.py       listing random pics  in img html with infinite load
                       param:[input file: allimages?.csv, output file:img-html-gg-?.html
                                template gg-?.html]
img-html-load-fluid.py  listing random pics  in img html with infinite load
                        bootstrap fluid layout
                        param:[input file: allimages?.csv, output file:img-html-gg-?.html
                                template b-?.html]

img-html-load-sal.py  listing random pics  in img html with salvattore
                        bootstrap fluid layout
                        param:[input file: allimages?.csv, output file:img-html-gg-?.html
                                template sv-?.html]

img-html-load-nano-01.py  listing random pics  in img html with nano gallery
                        param:[input file: all-img-random.csv, output file:al-?.html
                                template nano-?.html] 
//aws
deploy.py              upload files to s3  
                       params:[dir: dist, bucketname:artlisastage for zip:out]

//steps

img-tree-dup-02.py     check and delete duplicated images files 
                        params:[duplicate to del: all-del-images.csv]
list_painter_csv.py    sorted list painters 
                       params:[input:flist?.csv, ouput: all-painters.csv]
dir-painting.py        write painter's painting list 
                        params:[input all-painters.csv, output csv-plist\painter-name.csv]
list-img-random.py list random painting of a painter
                        params:[input all-painters.csv, csv-plist\painter-name.csv
                                output: all-img-random.csv]
img-html-load-nano-03.py SEO page name, load images to albums in nano gallery
                          params:[input:all-img-random.csv, template: nano-01.html
                                 output al-?.html]
img-html-load-nano-05.py id page name, load images to albums in nano gallery
                          params:[input:all-img-random.csv, template: nano-01.html
                                 output al-?.html]
img-html-load-nano-06.py id random painting from painter page name, l
                           oad images to albums in nano gallery
                          params:[input:all-img-random.csv, template: nano-01.html
                                 output al-?.html]

test-mnry-scrl-1.html  https://infinite-scroll.com/demo/masonry/
test-mnry-scrl-1...-6.html     view source, copy paste html, serial pages

//lambda
  handler name: filename.function name
  advanced : 1 min

//layout
z1.html               gamma gallery
oa1.html              bootstrap fluid.html
sa1.html              salvattore masonry
testjscroll.html      jscroll
testnano-02.html        nano gallery album
artnano2.html          artlisa.org

//jquery
https://nanogallery2.nanostudio.org   nano gallery
//layout
http://jscroll.com/
http://www.developphp.com/video/JavaScript/Scroll-Load-Dynamic-Content-When-User-Reach-Bottom-Ajax
https://connekthq.com/infinite-scroll-masonry/
https://codepen.io/drawby/pen/Adjkt
http://salvattore.com/
http://savvior.org/
https://connekthq.com/plugins/ajax-load-more/examples/salvattore-js/#code
fluid                 bootstrap 

//css masonry
http://w3bits.com/css-masonry/
https://medium.com/@_jh3y/how-to-the-masonry-layout-56f0fe0b19df
https://masonry.desandro.com/
https://tympanus.net/Development/GridLoadingEffects/index5.html
https://tympanus.net/codrops/2013/07/02/loading-effects-for-grid-items-with-css-animations/

https://css-tricks.com/snippets/css/using-font-face/

// web server
python -m SimpleHTTPServer 2000


//bootstrap //layout
https://startbootstrap.com/template-overviews/clean-blog/
https://tutorialzine.com/2017/02/freebie-4-bootstrap-galleries

//links
aws  https://cyberduck.io/?l=en
http://www.lambdatwist.com/s3-hosting-guide/   upload to s3
https://linuxacademy.com/howtoguides/posts/show/topic/14209-automating-aws-with-python-and-boto3   aws python boto3









