Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10 = 2j
SyntaxError: cannot assign to literal
>>> a = 10+ 2j
>>> type(a)
<class 'complex'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> min (1,100,+0.5)
0.5
>>> abs(-11.5)
11.5
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> math.log10(3)
0.47712125471966244
>>> math.pow(2,3)
8.0
>>> math.ceil(5.5)
6
>>> math.floor(5.5)
5
>>> math.exp(3)
20.085536923187668
>>> math.sqrt(2)
1.4142135623730951
>>> int(math.sqrt(5))
2
>>> float(math.sqrt(9))
3.0
>>> complex(3)
(3+0j)
>>> complex(3,4)
(3+4j)
>>> math.fabs(-9.587)
9.587
>>> (10+2)>15
False
>>> 10 % 2
0
>>> 9%2
1
>>> 8 **2
64
>>> math.pow(8,2)
64.0
>>> 9//2
4
>>> 10 // 5
2
>>> 10 // -5
-2
>>> -10 // 5
-2
>>>  -10 // -5
 
SyntaxError: unexpected indent
>>> -10 // -5
2
>>> if (10 + 6)> 55 and 10%2 ==0:
	print('My condition is met')

>>> if false:
	print('my condition is met')

	
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    if false:
NameError: name 'false' is not defined
>>> a += 2
>>> a
12.5
>>> 'BODMAS'
'BODMAS'
>>> 10+25-5  #LEFT TO RIGHT
30
>>> 2**3**4 # RIGHT TI LEFT
2417851639229258349412352
>>> float(‘inf’)

SyntaxError: invalid character '‘' (U+2018)
>>> float('inf’)
      
SyntaxError: EOL while scanning string literal
>>> float('inf')
inf
>>> float('nan)'
      float('56'+'65')
      
SyntaxError: invalid syntax
>>> float('56'+'65')
5665.0
>>> float('12+34')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float('12+34')
ValueError: could not convert string to float: '12+34'
>>> eval('1586')
1586
>>> eval('10>2')
True
>>> #6. What does (1>3)-(1<3) evaluate to?a) -1b) 1c) 0d) Unknown

>>> eval('(1>3)-(1<3)')
-1
>>> name = 'Freddy'
>>> type(name)
<class 'str'>
>>> name[0]
'F'
>>> name[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> name[1]
'r'
>>> name[-1]
'y'
>>> name[-3]
'd'
>>> name[0:4]
'Fred'
>>> name[0:3]
'Fre'
>>> name[-3,-1]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    name[-3,-1]
TypeError: string indices must be integers
>>> name[-3:-1]
'dd'
>>> name[-1:-4:-1]
'ydd'
>>> name[-1::-2]
'ydr'
>>> name[-1::-1]
'ydderF'
>>> name[0:]
'Freddy'
>>> name[:]
'Freddy'
>>> name[-1:-4]
''
>>> 'dd'+'yy'
'ddyy'
>>> 'dd'*2
'dddd'
>>> name[-1:4]
''
>>> 