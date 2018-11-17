#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
_date_ = '2018/10/28 21:06'
_author_ = 'YouChao'

import random
secret=random.randint(1,10)
print('----------YouChao嘤嘤嘤')
temp=input("猜猜我心中想的数字:")
guess=int(temp)
while guess!=secret:
    temp=input("哈哈哈猜错了重新猜吧:")
    guess=int(temp)
    if guess==secret:
         print("woc")
         print("你怎么知道的")
    else:
         if guess>secret:
            print("猜大了")
         else:
             print("猜小了")
print("游戏结束!")
