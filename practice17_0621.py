Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

'''
l1 = list(range(1,27))
l1
'\nIn this kata you are required to, given a string, replace every letter with its position in the alphabet.\nIf anything in the text isn\'t a letter, ignore it and don\'t return it.\n"a" = 1, "b" = 2, etc.\n\nExample\nalphabet_position("The sunset sets at twelve o\' clock.")\nShould return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)\n\n'
>>> l1 = list(range(1,27))
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
>>> str = "The sunset sets at twelve o' clock."
>>> str
"The sunset sets at twelve o' clock."
>>> def create_alphabet_dict():
	alphabet_str="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
	return dict((value,key) for key,value in enumerate(alphabet_str.split(','), start=1))
my_alphabet_dict = create_alphabet_dict()
SyntaxError: invalid syntax
>>> def create_alphabet_dict():
	alphabet_str="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
	return dict((value,key) for key,value in enumerate(alphabet_str.split(','), start=1))
    my_alphabet_dict = create_alphabet_dict()
    
SyntaxError: unindent does not match any outer indentation level
>>> def create_alphabet_dict():
    '''Map the entire alphabet set to their corresponding positions'''
    
    alphabet_str = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    return  dict((value,key) for key,value in enumerate(alphabet_str.split(','),start = 1))

''' 1. Loop through every alphabet in the passed string.
    2. Map to its position in Dict
'''

my_alphabet_dict = create_alphabet_dict()
SyntaxError: invalid syntax
>>> def create_alphabet_dict():
    '''Map the entire alphabet set to their corresponding positions'''
    
    alphabet_str = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    return  dict((value,key) for key,value in enumerate(alphabet_str.split(','),start = 1))

''' 1. Loop through every alphabet in the passed string.
    2. Map to its position in Dict
'''

my_alphabet_dict = create_alphabet_dict()

SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 