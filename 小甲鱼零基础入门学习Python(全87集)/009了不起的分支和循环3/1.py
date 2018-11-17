Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> love='YCM'
>>> for i in love:
	print(i,end=' ')

	
Y C M 
>>> member=['小豆豆','小布丁','小叮当','静香']
>>> for each in member:
	print(each,len(member))

	
小豆豆 4
小布丁 4
小叮当 4
静香 4
>>>  for each in member:
	print(each,len(each))
	
SyntaxError: unexpected indent
>>> for each in member:
	print(each,len(each))

	
小豆豆 3
小布丁 3
小叮当 3
静香 2
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(2,9):
	print(i)

	
2
3
4
5
6
7
8
>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9
>>> 
