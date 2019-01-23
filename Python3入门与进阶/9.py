#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
_date_ = '2018/12/9 18:58'
_author_ = 'YouChao'

# 循环
# 循环语句

# while for
#
# condition=True
#
# while condition:
#     print('I am While')

# counter=1
#
# while counter<=10:
#     counter+=1
#     print(counter)
# else:
#     print('EOF')

# 主要是用来遍历/循环  序列或者集合、字典
# a=[['apple','orange','banana','grape'],(1,2,3)]
# for x in a:
#     for y in x:
#       print(y,end=' ')

# a=[['apple','orange','banana','grape'],(1,2,3)]
# for x in a:
#     for y in x:
#       print(y)
# else:
#     print('fruit is gone')

# a=[1,2,3]
#
# for x in a:
#     if x==2:
#         break
#     print(x)

# a=[1,2,3]
#
# for x in a:
#     if x==2:
#         continue
#     print(x)

# a=[1,2,3]
#
# for x in a:
#     if x==2:
#         break
#     print(x)
#
# else:
#     print('EOF')
# for循环不是正常结束，不会执行 else


# a=[['apple','orange','banana','grape'],(1,2,3)]
# for x in a:
#     for y in x:
#         if y=='orange':
#             break  #break跳出的是内部循环
#         print(y)
# else:
#     print('fruit is gone')


# for target_list in expression_list:
#   pass
# for x in range(0,10):
#     print(x)

# for x in range(0,10,2):
#     print(x,end='|')

# for x in range(10,0,-2):
#     print(x,end='|')

a=[1,2,3,4,5,6,7,8]

# for i in range(0,len(a),2):
#     print(a[i],end=' | ')

b=a[0:len(a):2]
print(b)

# 会写代码，非常容易
# 高性能、封装性（可复用）、抽象
# 直白
# 美与不美

