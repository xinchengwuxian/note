#coding:utf-8
from PIL import Image,ImageDraw,ImageFont

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


img = Image.open('d:/my_note/python练手100小程序/images.jpg')
add_num(img)
