Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> getwd()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    getwd()
NameError: name 'getwd' is not defined
>>> getpwd
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    getpwd
NameError: name 'getpwd' is not defined
>>> getpwd()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    getpwd()
NameError: name 'getpwd' is not defined
>>> import os
>>> os.getwd()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.getwd()
AttributeError: module 'os' has no attribute 'getwd'
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Python39'
>>> os.mkdir(C:\\Users\Admin\\Python Diptarko 08_06_21)
SyntaxError: invalid syntax
>>> os.mkdir(C:/Users/Admin/Python Diptarko 08_06_21)
SyntaxError: invalid syntax
>>> os.mkdir C:/Users/Admin/Python Diptarko 08_06_21
SyntaxError: invalid syntax
>>> os.chdir("C:\Users\Admin\Python Diptarko 08_06_21")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir("C:/Users/Admin/Python Diptarko 08_06_21")
>>> os.getcwd()
'C:\\Users\\Admin\\Python Diptarko 08_06_21'
>>> 'C:\\Users\\Admin\\Python Diptarko 08_06_21'
'C:\\Users\\Admin\\Python Diptarko 08_06_21'
>>> print('Hello Word')
Hello Word
>>> print("Hello Word")
Hello Word
>>> print('''Hello Word''')
Hello Word
>>> pirnt('Hello'"\n"'''world''')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    pirnt('Hello'"\n"'''world''')
NameError: name 'pirnt' is not defined
>>> print('Hello'"\n"'''world''')
Hello
world
>>> print('Hello' "\n" '''world''')
Hello
world
>>> iCanProgram = 1
>>> icannnnnnnnnnnnnnnn = 10
>>> AnIdentifier = 'Hello World'
>>> 0AnIdentifier = 'Hello World'
SyntaxError: invalid syntax
>>> _AnIdentifier = 'Hello World'
>>> AnIdentifier = 2
>>> @AnIdentifier = 10
SyntaxError: invalid syntax
>>> AnIden$tifier = 'Hello World'
SyntaxError: invalid syntax
>>> _An_Identi_fier= 20
>>> _An_Identi _fier= 20
SyntaxError: invalid syntax
>>> _An_Identi,fier= 20,10
>>> _An_Identi_fier = 30,10
>>> _AnIdentifier = 30,10
>>> _AnIdentifier
(30, 10)
>>> aName = 10
>>> type(aName)
<class 'int'>
>>> id(aName)
1992008690256
>>> Name = '10'
>>> type(Name)
<class 'str'>
>>> id(Name)
1992015085360
>>> NAME = 20
>>> 10, 20, 10000000001
(10, 20, 10000000001)
>>> class Name():
	pass
-AnIden  = 10
SyntaxError: invalid syntax
>>> _AnIden  = 10
>>> __AnIden  = 20
>>> __name__ = 20
>>> __name__
20
>>> __NAME__
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    __NAME__
NameError: name '__NAME__' is not defined
>>> __last__
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    __last__
NameError: name '__last__' is not defined
>>> True
True
>>> and
SyntaxError: invalid syntax
>>> str = 10
>>> a = 'r'
>>> type(a)
<class 'str'>
>>> globle = 1
>>> globel = 1
>>> Globel = 2
>>> Globle = 2
>>> if True:
	print('True')
else:
	print("False")

True
>>> 