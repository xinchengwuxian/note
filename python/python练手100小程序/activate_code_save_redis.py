from activate_code_gen_2 import generate
import redis 
import random

r = redis.Redis(host='10.190.23.206',port=6379,db=0)

r.flushdb()


code_dict = dict(map(lambda x,y:[x,y], range(200),generate(200)))

for code_index in code_dict:
    r.set(code_index,code_dict[code_index])


