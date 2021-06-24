Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
except:
	print('You cant divide a number by zero. Please try again')

	
>10
|0
You cant divide a number by zero. Please try again
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
except:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
	except:
		print('Again you are trying division by zero. You are locked out')

		
>9
|0
You cant divide a number by zero. Please try again
#10
||0
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
except:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2
	except:
		print('You cant divide a number by zero. You are locked out')

		
>10
|0
You cant divide a number by zero. Please try again
#10
||0
You cant divide a number by zero. You are locked out
>>> fp = open('hithere.txt','r')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    fp = open('hithere.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'hithere.txt'
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2
		fp = open(r'Hello_Class.txt','r')
	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except:
	print('Please debug properly')

	
>10
|2
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'Hello_Class.txt','r')
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2
		
	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except:
	print('Please debug properly')

	
>10
|2
Oops, the file doesnt exist, please check its path
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'D:\Trainings\Programs\Hello_Class.txt','r')
	import hell0_hello_hello
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2

	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except:
	print('Please debug properly')

	
>10
|2
Please debug properly
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'D:\Trainings\Programs\Hello_Class.txt','r')
	#import hell0_hello_hello
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2

	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except:
	print('Please debug properly')
else:
	print('Good, no errors')
finally:
	print('Ok, Bye')

	
>10
|2
Good, no errors
Ok, Bye
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'D:\Trainings\Programs\Hello_Class.txt','r')
	#import hell0_hello_hello
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2

	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except:
	print('Please debug properly')
else:
	print('Good, no errors')
finally:
	print('Ok, Bye')

	
>10
|0
You cant divide a number by zero. Please try again
#10
||0
You cant divide a number by zero. You are locked out
Ok, Bye
>>> import hell0_hello_hello
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    import hell0_hello_hello
ModuleNotFoundError: No module named 'hell0_hello_hello'
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'D:\Trainings\Programs\Hello_Class.txt','r')
	import hell0_hello_hello
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2

	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except ImportError:
	print('Please check the module properly.')
else:
	print('Good, no errors')
finally:
	print('Ok, Bye')

	
>10
|2
Please check the module properly.
Ok, Bye
>>> try:
	n1 = int(input('>'))#Get divisor
	n2 = int(input('|')) #Get dividor

	n3 = n1/n2
	fp = open(r'D:\Trainings\Programs\Hello_Class.txt','r')
	import hell0_hello_hello
except ZeroDivisionError:
	print('You cant divide a number by zero. Please try again')
	try:
		n1 = int(input('#'))#Get divisor
		n2 = int(input('||')) #Get dividor
		n1/n2

	except ZeroDivisionError:
		print('You cant divide a number by zero. You are locked out')
except FileNotFoundError:
	print('Oops, the file doesnt exist, please check its path')
except ModuleNotFoundError:
	print('Please check the module properly.')
else:
	print('Good, no errors')
finally:
	print('Ok, Bye')

	
>10
|2
Please check the module properly.
Ok, Bye
>>> try:
	sal = float(input('>'))
	assert sal >=0 ,'Salary cant be less than zero'
except AssertionError:
	print('Please enter your salary properly')

	
>100
>>> try:
	sal = float(input('>'))
	assert sal >=0 ,'Salary cant be less than zero'
except AssertionError:
	print('Please enter your salary properly')

	
>-100
Please enter your salary properly
>>> try:
	sal = float(input('>'))
	assert sal >=0 
except AssertionError:
	print('Please enter your salary properly')

	
>-100
Please enter your salary properly
>>> try:
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    sal = float(input('>'))
ValueError: could not convert string to float: 'try:'
>>> try:
	sal = float(input('>'))
	assert sal >=0 ,'Salary cant be less than zero'


	
KeyboardInterrupt
>>> def sal(salary):
	assert salary >=0, 'Salary cant be less than zero'
	print('Salary')

	
>>> sal(100)
Salary
>>> def sal(salary):
	assert salary >=0, 'Salary cant be less than zero'
	print(salary)

	
>>> sal(100)
100
>>> sal(-100)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    sal(-100)
  File "<pyshell#68>", line 2, in sal
    assert salary >=0, 'Salary cant be less than zero'
AssertionError: Salary cant be less than zero
>>> sal(0)
0
>>> 
>>> try:
	sal = float(input('>'))
	assert sal >=0
except AssertionError:
	print('Please enter your salary properly')

	
>0
>>> try:
	sal = float(input('>'))
	assert sal >=1
except AssertionError:
	print('Please enter your salary properly')

	
>1
>>> try:
	sal = float(input('>'))
	assert sal >=1
	print(sal)
except AssertionError:
	print('Please enter your salary properly')

	
>1
1.0
>>> try:
	sal = float(input('>'))
	assert sal >=100
	print(sal)
except AssertionError:
	print('Please enter your salary properly')

	
>100
100.0
>>> try:
	sal = float(input('>'))
	assert sal >=100
	print(sal)
except AssertionError:
	print('Please enter your salary properly')

	
>99.9
Please enter your salary properly
>>> try:
	sal = float(input('>'))
	assert sal >=0
	print(sal)
except AssertionError:
	print('Please enter your salary properly')

	
>0
0.0
>>> 1 == 1.0
True
>>> 1.0 == 1.00
True
>>> 6 == 6.0
True
>>> 