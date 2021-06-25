'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)


    High Level Design

    1. One function, which will capture the entire alphabet set and create
    a dictionary out of it.

    2. Read the input string one alphabet at a time.
    3. Convert the alphabet to Upper case.
    4. If the alphabet is in the Alphabet dictionary, then find its position.
    5. Else ignore
'''

def create_alphabet_dict():
    '''Map the entire alphabet set to their corresponding positions'''
    
    alphabet_str = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    return  dict((value,key) for key,value in enumerate(alphabet_str.split(','),start = 1))

''' 1. Loop through every alphabet in the passed string.
    2. Map to its position in Dict
'''

my_alphabet_dict = create_alphabet_dict()

def replace_alphabet_posn(input_str):
    return ' '. join([str(my_alphabet_dict[itr.upper()]) for itr in input_str  if itr.upper()  in my_alphabet_dict])
    

     
		 
