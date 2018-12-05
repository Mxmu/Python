Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> a=[1,2,3]
>>> a>b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a>b
NameError: name 'b' is not defined
>>> 表达式
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    表达式
NameError: name '表达式' is not defined
>>> c=int('1')+2
>>> print(c)
3
>>> a or b and c 从左向右 左结合
SyntaxError: invalid syntax
>>> a=1
>>> b=2
>>> c=a+b  右结合
SyntaxError: invalid syntax
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/4.py ==================
go to left
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/4.py ==================
go to left
back away
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/4.py ==================
go to right
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/5.py ==================
go to right
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/5.py ==================
go to left
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/5.py ==================
go to right
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/6.py ==================
please input account
1
please input password
3
success
fail
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/6.py ==================
please input account
123
please input password
213
fail
>>> 
================== RESTART: D:/git/Python/Python3入门与进阶/6.py ==================
please input account

================== RESTART: D:/git/Python/Python3入门与进阶/6.py ==================
please input account
YouChao
please input password
123456
success
>>> 
