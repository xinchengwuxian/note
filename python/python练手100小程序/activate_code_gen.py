#coding=utf-8  

# 很多收费软件都需要用激活码来注册，
# 限时促销活动也需要填写激活码来进行。
# 激活码应用非常广泛，本文主要讲解如何用Python
# 语言生成我们常见的激活码。激活码一般是由26
# 个大写字母和10个数字任意组合而成，长度为12
# 位或者16位的居多。一个激活码里的字符是可以重
# 复的，而且必须要保证激活码是不能重复的。可以
# 分别随机生成16个字符，然后组成一个字符串，放
# 在字典中，通过字典来判断是否有重复的激活码。
# 以下代码是用Python生成10个16位的激活码。

import random  
import string  
  
def gene_activation_code(number,length):  

    ''''' 
    @number:生成激活码的个数 
    @length:生成激活码的长度 
    '''  
    result = {}  
    source = list(string.ascii_uppercase)  
    for index in range(0,10):  
        source.append(str(index))  
    while len(result) < number:  
        key= ''  
        for index in range(length):  
            if (index % 4 == 0) & (index != 0):
                key += "-"
            key += random.choice(source)  
        if key in result:  
            pass  
        else:  
            result[key] = 1  
    for key in result:  
        print(key)
  
if __name__ == "__main__":  
    number = 10  
    length = 16  
    gene_activation_code(number,length)  