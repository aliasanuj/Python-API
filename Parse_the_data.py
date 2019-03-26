To parse the data in Python :
================================
https://in.pycon.org/2010/talks/57-text-parsing-in-python/
https://www.vipinajayakumar.com/parsing-text-with-python/
https://realpython.com/python-csv/


Text parsing is a common programming task that splits the given sequence of characters or values (text) 
into smaller parts based on some rules. It has been used in a wide variety of applications ranging from
simple file parsing to large scale natural language processing.
Based on the context, different methodologies can be used such as parsing line by line using python's 
native string methods, using specialized pattern recognition language like regular expressions, using lex 
and yacc where the given sequence is analyzed, tokenized and the grammar is determined

What is parsing?
Why parsing?
Parsing in python
Simple string functions
Regular expressions
Lex and yacc
Efficient and appropriate use of different techniques


Parse : Convert data in a certain format into a more usable format.

The big picture:
==================
1. With that definition in mind, we can imagine that our input may be in any format. So, the first step
, when faced with any parsing problem, is to understand the input data format. If you are lucky, there 
will be documentation that describes the data format. If not, you may have to decipher the data format 
for yourselves. That is always fun.

2. Once you understand the input data, the next step is to determine what would be a more usable format
. Well, this depends entirely on how you plan on using the data. If the program that you want to feed 
the data into expects a CSV format, then that’s your end product. For further data analysis, I highly 
recommend reading the data into a pandas DataFrame.

Raw Text File ==> Primitive data structure (List\Dict) ==> complex Data structure (Database\DataFrame)

Parsing text in standard format :
================================
If your data is in a standard format or close enough, then there is probably an existing package that you can use to read your data with minimal effort.
For example, let’s say we have a CSV file, data.txt:
a,b,c
1,2,3
4,5,6
7,8,9

You can handle this easily with pandas.
import pandas as pd
df = pd.read_csv('data.txt')
df


   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

Parsing text using string methods :
=======================================

my_string = 'Names: Romeo, Juliet'
# split the string at ':'
step_0 = my_string.split(':')
# get the first slice of the list
step_1 = step_0[1]
# split the string at ','
step_2 = step_1.split(',')
# strip leading and trailing edge spaces of each item of the list
step_3 = [name.strip() for name in step_2]
# do all the above operations in one go
one_go = [name.strip() for name in my_string.split(':')[1].split(',')]
for idx, item in enumerate([step_0, step_1, step_2, step_3]):
    print("Step {}: {}".format(idx, item))
print("Final result in one go: {}".format(one_go))

Step 0: ['Names', ' Romeo, Juliet']
Step 1:  Romeo, Juliet
Step 2: [' Romeo', ' Juliet']
Step 3: ['Romeo', 'Juliet']
Final result in one go: ['Romeo', 'Juliet']
