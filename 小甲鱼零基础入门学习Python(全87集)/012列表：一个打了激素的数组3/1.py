Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [123]
>>> list 2= [234]
SyntaxError: invalid syntax
>>> list2 = [234]
>>> lsit1>list2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lsit1>list2
NameError: name 'lsit1' is not defined
>>> list1>list2
False
>>> list1=[123,456]
>>> list2=[234,123]
>>> list1>list2
False
>>> list3=[123,456]
>>> (list1<list2)and(list1==list2)
False
>>> (list1<list2)and(list1==list3)
True
>>> list4=[4,2,5,1,9,23,32,0]
>>> list4
[4, 2, 5, 1, 9, 23, 32, 0]
>>> list4.sort()
>>> list4
[0, 1, 2, 4, 5, 9, 23, 32]
>>> list4.sort(reverse=True)
>>> lsit4
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    lsit4
NameError: name 'lsit4' is not defined
>>> list4
[32, 23, 9, 5, 4, 2, 1, 0]
>>> 
