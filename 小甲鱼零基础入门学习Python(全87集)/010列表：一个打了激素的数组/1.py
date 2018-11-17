Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> menber=['小布丁','小叮当','小豆豆','静香']
>>> member
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    member
NameError: name 'member' is not defined
>>> menber
['小布丁', '小叮当', '小豆豆', '静香']
>>> number=[1,2,3,4,5]
>>> number
[1, 2, 3, 4, 5]
>>> mix=[1,'小豆豆',3.14,[1,2,3]]
>>> mix
[1, '小豆豆', 3.14, [1, 2, 3]]
>>> empty=[]
>>> empty
[]
>>> menber
['小布丁', '小叮当', '小豆豆', '静香']
>>> menber.append('葫芦娃')
>>> menber
['小布丁', '小叮当', '小豆豆', '静香', '葫芦娃']
>>> len(menber)
5
>>> menber.append('嘤嘤嘤','呜呜呜')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    menber.append('嘤嘤嘤','呜呜呜')
TypeError: append() takes exactly one argument (2 given)
>>> menber.extend('嘤嘤嘤','呜呜呜')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    menber.extend('嘤嘤嘤','呜呜呜')
TypeError: extend() takes exactly one argument (2 given)
>>> menber.extend(['嘤嘤嘤','呜呜呜'])
>>> menber
['小布丁', '小叮当', '小豆豆', '静香', '葫芦娃', '嘤嘤嘤', '呜呜呜']
>>> menber.insert(1,'菲菲')
>>> menber
['小布丁', '菲菲', '小叮当', '小豆豆', '静香', '葫芦娃', '嘤嘤嘤', '呜呜呜']
>>> menber.insert(0,'游超敏')
>>> menber
['游超敏', '小布丁', '菲菲', '小叮当', '小豆豆', '静香', '葫芦娃', '嘤嘤嘤', '呜呜呜']
>>> 
