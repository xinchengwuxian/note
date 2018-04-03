from PIL import Image,ImageDraw,ImageFont
import os

def resize(img,img_name):
    (width,height) = img.size
    if width > height:
        times = width/500
    else:
        times = height/500
    img = img.resize((int(width/times),int(height/times)))
    img.save(img_name,'jpeg')



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
    resize(img_src,img_name)
    print(img) 