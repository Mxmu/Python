Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,3,4,5,6]*3+[1,2,3]+[1,2,3,4,5,6]
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4, 5, 6]
>>> A=[1,2,3,4,5,6]
>>> print(A)
[1, 2, 3, 4, 5, 6]
>>> B=[1,2,3]
>>> A*3+B+A
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 4, 5, 6]
>>> skill=['新月打击','苍白之瀑']
>>> type=3
>>> print(type)
3
>>> a=1
>>> b=a
>>> a=3
>>> print(b)
1
>>> a=[1,2,3,4,5]
>>> b=a
>>> a[0]='1'
>>> print(a)
['1', 2, 3, 4, 5]
>>> print(b)
['1', 2, 3, 4, 5]
>>> type=1
>>> type(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(1)
TypeError: 'int' object is not callable
>>> 1(1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    1(1)
TypeError: 'int' object is not callable
>>> int str tuple(不可改变)  值类型   list set dict(可变)  引用类型
SyntaxError: invalid syntax
>>> a='hello'
>>> a=a+'python'
>>> print(a)
hellopython
>>> b='hello'
>>> id(b)
2821054961624
>>> b=b+'python'
>>> id(b)
2821055842160
>>> 'python'[0]
'p'
>>> 'python'[0]='o'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'python'[0]='o'
TypeError: 'str' object does not support item assignment
>>> 字符串是不可改变的类型
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    字符串是不可改变的类型
NameError: name '字符串是不可改变的类型' is not defined
>>> a=[1,2,3]
>>> id(a)
2821055841096
>>> hex(id(a))
'0x290d4080348'
>>> a[0]='1'
>>> id(a)
2821055841096
>>> a=(1,2,3)
>>> a[0]='1'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[0]='1'
TypeError: 'tuple' object does not support item assignment
>>> b=[1,2,3]
>>> b.append(4)
>>> print(b)
[1, 2, 3, 4]
>>> c=(1,2,3)
>>> c.append(4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.append(4)
AttributeError: 'tuple' object has no attribute 'append'
>>> a=(1,2,3,[1,2,4])
>>> a[2]
3
>>> a[3][2]
4
>>> a=(1,2,3,[1,2,['a','b','c']])
>>> a[3][2][1]
'b'
>>> a=(1,2,3,[1,2,4])
>>> a[2]='3'
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a[2]='3'
TypeError: 'tuple' object does not support item assignment
>>> a[3][2]='4'
>>> print(a)
(1, 2, 3, [1, 2, '4'])
>>> 元组不可改变，上面改变的是列表
SyntaxError: invalid character in identifier
>>> 'hello'+'world'
'helloworld'
>>> [1,2,3]*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 3-1
2
>>> 3/2
1.5
>>> 3//2
1
>>> 5%2
1
>>> 余数
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    余数
NameError: name '余数' is not defined
>>> 2**2
4
>>> 2**5
32
>>> 平方
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    平方
NameError: name '平方' is not defined
>>> 算数运算符
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    算数运算符
NameError: name '算数运算符' is not defined
>>> c=1
>>> c=c+1
>>> print(c)
2
>>> c+=1
>>> print(c)
3
>>> c++
SyntaxError: invalid syntax
>>> c--
SyntaxError: invalid syntax
>>> b=2
>>> a=3
>>> b+=a
>>> print(b)
5
>>> b-=a
>>> print(b)
2
>>> b=b-a
>>> print(b)
-1
>>> b*=a
>>> print(b)
-3
>>> b=2
>>> a=1
>>> a+b
3
>>> print(a)
1
>>> print(b)
2
>>> b=b+a
>>> print(b)
3
>>> 1==1
True
>>> 1>1
False
>>> 1>=1
True
>>> a>=b
False
>>> a=1
>>> b=2
>>> a!=b
True
>>> b=1
>>> b+=b>=1
>>> print(b)
2
>>> print(b>=1)
True
>>> int(True)
1
>>> 2>3
False
>>> 'a'>'b'
False
>>> ord('a')
97
>>> ord('b')
98
>>> 'abc'<'abd"
SyntaxError: EOL while scanning string literal
>>> 'abc'<'abd'
True
>>> [1,2,3]<[2,3,4]
True
>>> (1,2,3)<(1,3,2)
True
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> not False
True
>>> not True
False
>>> not not True
True
>>> 1 and 1
1
>>> 'a' and 'b'
'b'
>>> 'a' or 'b'
'a'
>>> not 'a'
False
>>> not '0'
False
>>> not ''
True
>>> [1] or []
[1]
>>> [] or [1]
[1]
>>> 'a' and 'b'
'b'
>>> '' and 'b'
''
>>> not 0
True
>>> not 1
False
>>> 1 and 0
0
>>> 0 and 1
0
>>> 0 and 0
0
>>> 1 and 1
1
>>> 1 and 2
2
>>> 2 and 1
1
>>> 0 or 1
1
>>> 1 or 0
1
>>> 1 or 0
1
>>> 1 or 2
1
>>> a=1
>>> a in [1,2,3,4,5]
True
>>> b=6
>>> b in [1,2,3,4,5]
False
>>> b='h'
>>> b in 'hello'
True
>>> b='a'
>>> b in {'c':1}
False
>>> b=1
>>> b in {'c':1}
False
>>> b='c'
>>> b in {'c':1}
True
>>> a=1
>>> b=2
>>> a is b
False
>>> a=1
>>> b=1
>>> a is b
True
>>> a='heelo'
>>> a=1
>>> b=1.0
>>> a is b
False
>>> id(a)
140737124086608
>>> id(b)
2821016632368
>>> a==b
True
>>> a={1,2,3}
>>> b={2,1,3}
>>> a==b
True
>>> a is b
False
>>> id(a)
2821055821192
>>> id(b)
2821055820968
>>> c=(1,2,3)
>>> d=(2,1,3)
>>> c==d
False
>>> c is d
False
>>> a='hello'
>>> type(a)==int
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    type(a)==int
TypeError: 'int' object is not callable
>>> type(a)==str
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    type(a)==str
TypeError: 'int' object is not callable
>>> print(type)
1
>>> isinstance(a,str)
True
>>> isinstance(a,int)
False
>>> isinstance(a,(int,str,float))
True
>>> isinstance(a,(int,float))
False
>>> 按位与&
SyntaxError: invalid syntax
>>> a=2
>>> b=3
>>> a&b
2
>>> 按位或|
SyntaxError: invalid syntax
>>> a=2
>>> b=3
>>> a|b
3
>>> 
