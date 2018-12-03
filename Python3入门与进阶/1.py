Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
hello world
hello world
hello world
'''
'\nhello world\nhello world\nhello world\n'
>>> """
hello world
hello world
hello world
"""
'\nhello world\nhello world\nhello world\n'
>>> """hello world\nhello world\nhello world"""
'hello world\nhello world\nhello world'
>>> print("""hello world\nhello world\nhello world""")
hello world
hello world
hello world
>>> """hello world
hello world"""
'hello world\nhello world'
>>> 'hello\
world'
'helloworld'
>>> print('hello \n world')
hello 
 world
>>> print('hello \\n world')
hello \n world
>>> 'let \'s go'
"let 's go"
>>> print('c:\northwind\northwest')
c:
orthwind
orthwest
>>> print('c:\\northwind\\northwest')
c:\northwind\northwest
>>> print(r'c:\northwind\northwest')
c:\northwind\northwest
>>> "hello"
'hello'
>>> "world"
'world'
>>> "hello world"
'hello world'
>>> "hello"+"world"
'helloworld'
>>> "hello"*3
'hellohellohello'
>>> "hello world"[0]
'h'
>>> "hello world"[3]
'l'
>>> "hello world"[4]
'o'
>>> "hello world"[1]
'e'
>>> "hello world"[-1]
'd'
>>> "hello world"[-3]
'r'
>>> "hello world"[6]
'w'
>>> "hello world"[-5]
'w'
>>> "hello world"[0:4]
'hell'
>>> "hello world"[0:5]
'hello'
>>> "hello world"[0:-1]
'hello worl'
>>> "hello world"[0:-3]
'hello wo'
>>> "hello world"[6:11]
'world'
>>> "hello world"[6:20]
'world'
>>> "hello world"[6:]
'world'
>>> "hello  python java C# javascript php ruby"[6:]
' python java C# javascript php ruby'
>>> "hello  python java C# javascript php ruby"[-4:]
'ruby'
>>> r'C:\Windows'
'C:\\Windows'
>>> 
