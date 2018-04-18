#coding:utf-8
from PIL import Image,ImageDraw,ImageFont
import os

#http://font.chinaz.com/zhongwenziti.html 字体下载网站



def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('cambriab.ttf',size=80)
    fillcolor = 'red'
    (width, height) = img.size
    print("width = %d " %width)
    print("height = %d" %height)
    #第一个参数是加入字体的坐标
    #第二个参数是文字内容
    #第三个参数是字体格式
    #第四个参数是字体颜色
    draw.text((800,100),u'44',font=myfont,fill=fillcolor)
    img.save('modfiy_pdd01.jpg','jpeg')
    return 0


def cut_img(img,img_new):
    (width, height) = img.size

    '''
    裁剪：传入一个元组作为参数
    元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
    '''

    if width*3/4 > height:
        x = (width - height*4/3)/2
        y = 0
        w = height*4/3
        h = height
    else:
        x = 0
        y = (height - width*3/4)/2
        w = width
        h = width*3/4

    region = img.crop((x, y, x+w, y+h))
    region.save(img_new,'jpeg')

#img = Image.open('F:/Github/note/python/python练手100小程序/images.jpg')
#add_num(img)
#cut_img(img)

path=r'd:/my_note/python练手100小程序/images'

for i in os.walk(path):
    file_list = i
    
# print(file_list)

imgs = file_list[2]
# print(imgs)
# print(os.walk(path))
for img in imgs:
    img_path = path + "/" + img
    img_src = Image.open(img_path)  
    img_name = path + "/1" + img
    cut_img(img_src,img_name)
    print(img) 