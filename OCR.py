#encoding: utf8
from aip import AipOcr
import os
import sys
import json

""" 你的 APPID AK SK """
APP_ID = '14827525'
API_KEY = 'mxZcVdC3Hy8YulMPDgGmLjLk'
SECRET_KEY = 'BOxcAq41wr2xsG7DF9hLybtXLCea8ctL'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
n =0
while n <=26:
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    n = n + 1
    str(n)
    print(n)
    image = get_file_content(str(n) + '.png')
    res =client.basicAccurate(image);
    f1=open(str(n) + '.txt','w')
    for item in res['words_result']:
        """写到文本文件"""

        f1.write(item['words']+'\n')
    f1.close()
print('END')



