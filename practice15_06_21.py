Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DICTIONARY
>>> d = {'stud_a':100,'stud_b':200,'stud_c':300}
>>> d
{'stud_a': 100, 'stud_b': 200, 'stud_c': 300}
>>> type(d)
<class 'dict'>
>>> d.items
<built-in method items of dict object at 0x0000027B223E6540>
>>> d.items()
dict_items([('stud_a', 100), ('stud_b', 200), ('stud_c', 300)])
>>> d.keys()
dict_keys(['stud_a', 'stud_b', 'stud_c'])
>>> d.values()
dict_values([100, 200, 300])
>>> d.pop('stud_b')
200
>>> d
{'stud_a': 100, 'stud_c': 300}
>>> d.popitem()
('stud_c', 300)
>>> d
{'stud_a': 100}
>>> d['stud_c'] = 200
>>> d
{'stud_a': 100, 'stud_c': 200}
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
>>> d.get('stud_a')
100
>>> d
{'stud_a': 100, 'stud_c': 200}
>>> d.update()
>>> d
{'stud_a': 100, 'stud_c': 200}
>>> d1 = {'stud_b':60,'stud_d':70}
>>> d1
{'stud_b': 60, 'stud_d': 70}
>>> d2 = d | d1
>>> d2
{'stud_a': 100, 'stud_c': 200, 'stud_b': 60, 'stud_d': 70}
>>> d['stud_a'] = 70
>>> d
{'stud_a': 70, 'stud_c': 200}
>>> d1['stud_a'] =  100
>>> d1
{'stud_b': 60, 'stud_d': 70, 'stud_a': 100}
>>> d3 = d | d1
>>> d3
{'stud_a': 100, 'stud_c': 200, 'stud_b': 60, 'stud_d': 70}
>>> {**d,**d1}
{'stud_a': 100, 'stud_c': 200, 'stud_b': 60, 'stud_d': 70}
>>> # above command is for merge dictionary
>>> #Create a dictionary , which stores the salary of three different people.
>>> #Now, read out from the dictionary each key, value pair, corresponding to the salary, calculate the Income tax of the person(You can consider a 10% Flat rate), and create a new dictionary, with the Name of the person, and the income tax

>>> print('Hi %s, my nave is %s'%('sir','navnath'))
Hi sir, my nave is navnath
>>> print('Hi {}, my name is {}'.formate('sir','navnath'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print('Hi {}, my name is {}'.formate('sir','navnath'))
AttributeError: 'str' object has no attribute 'formate'
>>> print('Hi {}, my name is {}.formate('sir','navnath')')
SyntaxError: invalid syntax
>>> print('Hi {}, my name is {}'.formate(sir,navnath))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('Hi {}, my name is {}'.formate(sir,navnath))
AttributeError: 'str' object has no attribute 'formate'
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> print('Hi {}, my name is {}'.format('sir','navnath'))
Hi sir, my name is navnath
>>> tuple_dishes = ('Pulao','Shahi paneer', 'palak paneer' ,'Gobi Manhcurian')
>>> tuple_dishes
('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
>>> my_plate = []
>>> for itr in tuple_dishes :
	if itr == 'Shahi _paneer' or itr == 'palak paneer' :
		my_plate.append(itr)
	else:
		pass

	
>>> my_plate
['palak paneer']
>>> for itr in tuple_dishes :
	if itr == 'Shahi paneer' or itr == 'palak paneer' :
		my_plate.append(itr)
	else:
		pass

	
>>> my_plate
['palak paneer', 'Shahi paneer', 'palak paneer']
>>> my_plate.clear()
>>> my_plate
[]
>>> for itr in tuple_dishes :
	if itr == 'Shahi paneer' or itr == 'palak paneer' :
		my_plate.append(itr)
	else:
		pass

	
>>> my_plate
['Shahi paneer', 'palak paneer']
>>> my_plate.clear()
>>> for itr in tuple_dishes :
	if itr == 'Shahi paneer' or itr == 'palak paneer' :
		my_plate.append(itr)
	elif itr == 'Pulao':
		my_plate.append(itr=' salt')
	else:
		pass

	
Traceback (most recent call last):
  File "<pyshell#58>", line 5, in <module>
    my_plate.append(itr=' salt')
TypeError: list.append() takes no keyword arguments
>>> for itr in tuple_dishes :
	if itr == 'Shahi paneer' or itr == 'palak paneer' :
		my_plate.append(itr)
	elif itr == 'Pulao':
		my_plate.append(itr+' salt')
	else:
		pass

	
>>> my_plate
['Pulao salt', 'Shahi paneer', 'palak paneer']
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> range(0,10,2)
range(0, 10, 2)
>>> for itr in range(1,10,2):
	print(itr)

	
1
3
5
7
9
>>> tuple_dishes
('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
>>> len(tuple_dishes)
4
>>> for itr in range(len(tuple_dishes)):
	print(itr, tuple_dishes)

	
0 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
1 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
2 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
3 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
>>> for itr in range(len(tuple_dishes)):
	print(itr, tuple_dishes[itr])

	
0 Pulao
1 Shahi paneer
2 palak paneer
3 Gobi Manhcurian
>>> for itr in range(4):
	print(itr, tuple_dishes)

	
0 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
1 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
2 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
3 ('Pulao', 'Shahi paneer', 'palak paneer', 'Gobi Manhcurian')
>>>  for itr in range(4):
	print(itr, tuple_dishes[itr])

SyntaxError: unexpected indent
>>>  for itr in range(4):
	print(itr, tuple_dishes[itr])
	
SyntaxError: unexpected indent
>>>  for itr in range(4):
	print(itr, tuple_dishes[itr])
	
SyntaxError: unexpected indent
>>> for itr in range(4):
        print(itr, tuple_dishes[itr])

        
0 Pulao
1 Shahi paneer
2 palak paneer
3 Gobi Manhcurian
>>> tuple_dishes[0]
'Pulao'
>>> tuple_dishes[1]
'Shahi paneer'
>>> 
>>> 
>>> 
>>> itr = 0
>>> while itr < 10:
	print(itr)
	itr = itr + 1

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(20):
	if i % 2 != 0:
		continue
	else:
		print(i)

		
0
2
4
6
8
10
12
14
16
18
>>> for i in range(20):
	if i % 2!= 0:
		break
	else:
		print(i)

		
0
>>> for i in range(20):
	if i % 2 !=0:
		continue
	print('Hi, number is {}'.format(i))

	
Hi, number is 0
Hi, number is 2
Hi, number is 4
Hi, number is 6
Hi, number is 8
Hi, number is 10
Hi, number is 12
Hi, number is 14
Hi, number is 16
Hi, number is 18
>>> 