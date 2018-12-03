Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type([1,2,3,4,5,6])
<class 'list'>
>>> ["hello","world",1,9,True,False]
['hello', 'world', 1, 9, True, False]
>>> type(["hello","world",1,9,True,False])
<class 'list'>
>>> [[1,2],[3,4],[True,False]]
[[1, 2], [3, 4], [True, False]]
>>> type([[1, 2], [3, 4], [True, False]])
<class 'list'>
>>> 嵌套列表
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    嵌套列表
NameError: name '嵌套列表' is not defined
>>> ["新月打击","苍白之瀑","月之降临","月神冲刺"][0]
'新月打击'
>>> ["新月打击","苍白之瀑","月之降临","月神冲刺"][3]
'月神冲刺'
>>> ["新月打击","苍白之瀑","月之降临","月神冲刺"][0:2]
['新月打击', '苍白之瀑']
>>> ["新月打击","苍白之瀑","月之降临","月神冲刺"][-1:]
['月神冲刺']
>>> ["新月打击","苍白之瀑","月之降临","月神冲刺"]+["点燃","虚弱"]
['新月打击', '苍白之瀑', '月之降临', '月神冲刺', '点燃', '虚弱']
>>> ['点燃','虚弱']*3
['点燃', '虚弱', '点燃', '虚弱', '点燃', '虚弱']
>>> ['点燃','虚弱']-['点燃']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ['点燃','虚弱']-['点燃']
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> [['巴西','克罗地亚','墨西哥','喀麦隆'],[],[],[],[],[],[],[]]
[['巴西', '克罗地亚', '墨西哥', '喀麦隆'], [], [], [], [], [], [], []]
>>> (1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> (1,'-1',True)
(1, '-1', True)
>>> tpye((1, '-1', True))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tpye((1, '-1', True))
NameError: name 'tpye' is not defined
>>> (1, 2, 3, 4, 5)[0]
1
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> type((1, '-1', True))
<class 'tuple'>
>>> type((1))
<class 'int'>
>>> type(('hello'))
<class 'str'>
>>> (1+1)*2
4
>>> type((1,))
<class 'tuple'>
>>> type(())
<class 'tuple'>
>>> type([1])
<class 'list'>
>>> int,float,bool,str,list,tuple
(<class 'int'>, <class 'float'>, <class 'bool'>, <class 'str'>, <class 'list'>, <class 'tuple'>)
>>> str list tuple 序列
SyntaxError: invalid syntax
>>> 切片
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    切片
NameError: name '切片' is not defined
>>> [1,2,3][2]
3
>>> "hello world"[0:8:2]
'hlow'
>>> 3 in [1,2,3,4,5,6]
True
>>> 3 not in [1,2,3,4,5,6]
False
>>> len([1,2,3,4,5,6])
6
>>> len("hello world")
11
>>> max([1,2,3,4,5,6])
6
>>> min([1,2,3,4,5,6])
1
>>> max('hello world')
'w'
>>> min('hello world')
' '
>>> min('helloworld')
'd'
>>> ord('w')
119
>>> ord('d')
100
>>> ord(' ')
32
>>> type({1,2,3,4,5,6})
<class 'set'>
>>> {1,2,3,4,5,6}[0]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    {1,2,3,4,5,6}[0]
TypeError: 'set' object does not support indexing
>>> [1,2,3,4,5,6][0:2]切片
SyntaxError: invalid syntax
>>> {1,1,2,3,4,4,5}
{1, 2, 3, 4, 5}
>>> len({1,2,3})
3
>>> 1 in {1,2,3}
True
>>> {1,2,3,4,5,6}{3,4}
SyntaxError: invalid syntax
>>> {1,2,3,4,5,6}-{3,4}
{1, 2, 5, 6}
>>> {1,2,3,4,5,6}&{3,4}
{3, 4}
>>> {1,2,3,4,5,6}^{3,4}
{1, 2, 5, 6}
>>> {1,2,3,4,5,6}|{3,4}
{1, 2, 3, 4, 5, 6}
>>> type({})
<class 'dict'>
>>> set()
set()
>>> type(set())
<class 'set'>
>>> len(set())
0
>>> {'Q':"新月打击",'W':"苍白之瀑",'E':"月之降临",'R':"月神冲刺"}
{'Q': '新月打击', 'W': '苍白之瀑', 'E': '月之降临', 'R': '月神冲刺'}
>>> Q
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    Q
NameError: name 'Q' is not defined
>>> {'Q':"新月打击",'W':"苍白之瀑",'E':"月之降临",'R':"月神冲刺"}['R']
'月神冲刺'
>>> {'Q':"新月打击",'Q':"苍白之瀑",'E':"月之降临",'R':"月神冲刺"}['Q']
'苍白之瀑'
>>> {1:"新月打击",'1':"苍白之瀑",'E':"月之降临",'R':"月神冲刺"}[1]
'新月打击'
>>> {1:"新月打击",'1':"苍白之瀑",'E':"月之降临",'R':"月神冲刺"}['1']
'苍白之瀑'
>>> 
