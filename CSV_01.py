CSV files | CSV Operations :
=============================

https://www.programiz.com/python-programming/working-csv-files
https://pythonspot.com/files-spreadsheets-csv/
https://realpython.com/python-csv/
https://stackabuse.com/reading-and-writing-csv-files-in-python/
https://docs.python.org/2/library/csv.html


Writing data into different types of CSV files
Writing on Existing File
Normal CSV File
CSV File with Quotes
CSV files with Custom Delimiters
CSV file with Lineterminator
CSV file with quotechars
Writing CSV file into a Dictionary

====================================================
1. Writing data into different types of CSV files :
===================================================

We have a people.csv file with following data.

SN, Name, City
1, John, Washington
2, Eric, Los Angeles
3, Brad, Texas
Now, we are going to modify people.csv file.

Example 1: Modifying existing rows of people.csv
import csv

row = ['2', ' Marie', ' California']

with open('people.csv', 'r') as readFile:
reader = csv.reader(readFile)
lines = list(reader)
lines[2] = row #lines[0] means 1st line

with open('people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
When we open the people.csv file with text editor, then it will show:

SN, Name, City
1, John, Washington
2, Marie, California
3, Brad, Texas

========================================================
2. Example 2: Appending new rows to people.csv file :
========================================================
import csv

row = ['4', ' Danny', ' New York']

with open('people1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()
When we open people.csv file with text editor, then it will show :

SN, Name, City
1, John, Washington
2, Marie, California
3, Brad, Texas
4, Danny, New York

In the above program, we append a new row into people.csv. For this, we opened the csv file in 'a' append mode. Then, we 
write the value of row after the last line of the people.csv file.

==========================================================
3. Normal CSV File
==========================================================
We create a normal csv file using writer() method of csv module having default delimiter comma(,).

Example 3: Write a python list into person.csv file :
=======================================================
import csv
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()
When we open the person.csv file with text editor, then it will show :

Person,Age
Peter,22
Jasmine,21
Sam,24
In the above program, we use csv.writer() function to write data from a list csvData into a csv file person.csv.
Note: The writerow() method writes one row at a time. If you need to write all the data at once you can use writerows() 
method.

========================================
CSV Files with quotes :
=======================================
We can write the csv file with quotes, by registering new dialects using csv.register_dialect() class of csv module.

Example 4 : Write into person1.csv file :
============================================
import csv

person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]
csv.register_dialect('myDialect',delimiter = '|', quoting=csv.QUOTE_ALL, skipinitialspace=True)
with open('person1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
f.close()

When we open person1.csv file, we get following output :
"SN","Person","DOB"
"1","John","18/1/1997"
"2","Marie","19/2/1998"
"3","Simon","20/3/1999"
"4","Erik","21/4/2000"
"5","Ana","22/5/2001"

In above program, we register a dialect named myDialect. Inside myDialect we use quoting=csv.QUOTE_ALL to write the 
double quote on all the values.
========================================================
Example 5 : Writing with custom delimiter as pipe(|) :
==================================================
import csv
person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]
csv.register_dialect('myDialect', delimiter = '|', quoting=csv.QUOTE_NONE, skipinitialspace=True)
with open('dob.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
f.close()

When we open dob.csv file, we get following output:
SN|Person|DOB
1|John|18/1/1997
2|Marie|19/2/1998
3|Simon|20/3/1999
4|Erik|21/4/2000
5|Ana|22/5/2001
In the above program, we register a dialect with delimiter as pipe(|). Then we write a list into a csv file dob.csv.

CSV File with a Lineterminator
A lineterminator is a string used to terminate lines produced by writer. The default value is \r\n.

We can write csv file with a lineterminator in Python by registering new dialects using csv.register_dialect() class of csv module

========================================================
Example 6 : Writing csv file using a lineterminator  :
========================================================
import csv
csvData = [['Fruit', 'Quantity'], ['Apple', '5'], ['Orange', '7'], ['Mango', '8']]
csv.register_dialect('myDialect', delimiter = '|', lineterminator = '\r\n\r\n')
with open('lineterminator.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerows(csvData)
f.close()

When we open the lineterminator.csv file, we get following output:
Fruit|Quantity
Apple|5
Orange|7
Mango|8

In above code, we register a new dialects as myDialect. Then, we use delimiter='|' where a | is considered as column 
separator. After that, we use lineterminator='\r\n\r\n' where each row separates after every two lines.
Note : Python's CSV module only accepts \r\n, \n or \r as lineterminator.

=============================================
CSV File with quotechars :
==============================================
We can write the csv file with custom quote characters, by registering new dialects using csv.register_dialect() class of
csv module.

Example 7: Writing CSV FIle with quotechars :
==============================================
import csv
csvData = [['SN', 'Items'], ['1', 'Pen'], ['2', 'Book'], ['3', 'Copy']]
csv.register_dialect('myDialect', delimiter = '|', quotechar = '"', quoting=csv.QUOTE_ALL, skipinitialspace=True)

with open('quotechars.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, dialect='myDialect')
    writer.writerows(csvData)
print("writing completed")
csvFile.close()
Output:

"SN"|"Items"
"1"|"Pen"
"2"|"Book"
"3"|"Copy"

In the above program, we register a dialect called myDialect. Then we use delimiter as pipe(|) and quotechar as 
doublequote '"'.

========================================
Writing CSV file into a Dictionary :
=========================================
Using DictWriter() class of csv module, we can write a csv file into a dictionary. It works similar to the writer() 
function but creates an object which maps data into a dictionary. The keys are given by the fieldnames parameter.

Example 8: Writing dictionary into peak.csv file :
===================================================
import csv
data = [{'mountain' : 'Everest', 'height': '8848'},
      {'mountain' : 'K2 ', 'height': '8611'},
      {'mountain' : 'Kanchenjunga', 'height': '8586'}]
with open('data.csv', 'w') as csvFile:
    fields = ['mountain', 'height']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
    writer.writeheader()
print("writing completed")
csvFile.close()

When we open peak.csv file, it will contain following output :
mountain,height
Everest,8848
K2 ,8611
Kanchenjunga,8586
mountain,height

In the above program, we use fieldnames as headings of each column in csv file. Then, we use a DictWriter() to write dictionary 
data into peak.csv file.
============================================================================ 
Example 9: Writing dictionary into grade.csv file with custom dialects :
==============================================================================
import csv
csv.register_dialect('myDialect', delimiter = '|', quoting=csv.QUOTE_ALL)
with open('grade.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'Name': 'Alex'},
                 {'Grade': 'A', 'Name': 'Bin'},
                 {'Grade': 'C', 'Name': 'Tom'}])
print("writing completed")

When we open grade.csv file, it will contain following output:
"Name"|"Grade"
"Alex"|"B"
"Bin"|"A"
"Tom"|"C"

In the above program, we create a custom dialect called myDialect with pipe(|) as delimiter. Then, use fieldnames as 
headings of each column in csv file. Finally, we use a DictWriter() to write dictionary data into grade.csv file.
