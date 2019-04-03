What Is a CSV File? :
==========================
A CSV file (Comma Separated Values file) is a type of plain text file that uses specific structuring to 
arrange tabular data. Because it’s a plain text file, it can contain only actual text data—in other 
words, printable ASCII or Unicode characters.

The structure of a CSV file is given away by its name. Normally, CSV files use a comma to separate each 
specific data value. Here’s what that structure looks like:
column 1 name,column 2 name, column 3 name
first row data 1,first row data 2,first row data 3
second row data 1,second row data 2,second row data 3

Notice how each piece of data is separated by a comma. Normally, the first line identifies each piece of 
data—in other words, the name of a data column. Every subsequent line after that is actual data and is 
limited only by file size constraints.In general, the separator character is called a delimiter, and the 
comma is not the only one used. Other popular delimiters include the tab (\t), colon (:) and semi-colon 
(;) characters. Properly parsing a CSV file requires us to know which delimiter is being used.


Where Do CSV Files Come From? :
=====================================
CSV files are normally created by programs that handle large amounts of data. They are a convenient way 
to export data from spreadsheets and databases as well as import or use it in other programs. For 
example, you might export the results of a data mining program to a CSV file and then import that into a 
spreadsheet to analyze the data, generate graphs for a presentation, or prepare a report for publication.
CSV files are very easy to work with programmatically. Any language that supports text file input and 
string manipulation (like Python) can work with CSV files directly.


Parsing CSV Files With Python’s Built-in CSV  :
===================================================
The csv library provides functionality to both read from and write to CSV files. Designed to work out of 
the box with Excel-generated CSV files, it is easily adapted to work with a variety of CSV formats. The 
csv library contains objects and other code to read, write, and process data from and to CSV files.

1. Reading CSV Files With csv
2. Reading CSV Files Into a Dictionary With csv
3. Writing CSV Files With csv
4. Writing CSV File From a Dictionary With csv


Parsing CSV Files With the pandas Library :
=============================================
Of course, the Python CSV library isn’t the only game in town. Reading CSV files is possible in pandas 
as well. It is highly recommended if you have a lot of data to analyze. Pandas is an open-source Python 
library that provides high performance data analysis tools and easy to  use data structures. pandas is 
available for all Python installations, but it is a key part of the Anaconda distribution and works 
extremely well in Jupyter notebooks to share data, code, analysis results, visualizations, and narrative 
text.

1. Reading CSV Files With pandas
2. Writing CSV Files With pandas


==================================
1. Reading CSV Files With csv :
==================================
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March

import csv
with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=',')
    print(list(reader))
csvFile.close()

[['name', 'department', 'birthday month'], ['John Smith', 'Accounting', 'November'], ['Erica Meyers', 'IT', 'March'], []]
====================================
import csv
with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=',')
    for row in reader:
        print(row)
csvFile.close()

['name', 'department', 'birthday month']
['John Smith', 'Accounting', 'November']
['Erica Meyers', 'IT', 'March']
[]
======================================
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March

import csv
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


Column names are name, department, birthday month
    John Smith works in the Accounting department, and was born in November.
    Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.


===================================================
2. Reading CSV Files Into a Dictionary With csv :
====================================================
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March

import csv
with open('data.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
Column names are name, department, birthday month
	John Smith works in the Accounting department, and was born in November.
	Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.

============================================================
3. Writing CSV Files With csv :
============================================================
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March

import csv
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

John Smith,Accounting,November
Erica Meyers,IT,March

===================================================
4. Writing CSV File From a Dictionary With csv :
===================================================
John Smith,Accounting,November
Erica Meyers,IT,March

import csv
with open('data.txt', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name': 'kumar anuj', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

emp_name,dept,birth_month
kumar anuj,Accounting,November
Erica Meyers,IT,March

======================================
1. Reading CSV Files With pandas :
=======================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt')
print(df)


             Name Hire Date   Salary  Sick Days remaining
0  Graham Chapman  03/15/14  50000.0                   10
1     John Cleese  06/01/15  65000.0                    8
2       Eric Idle  05/12/14  45000.0                   10
3     Terry Jones  11/01/13  70000.0                    3
4   Terry Gilliam  08/12/14  48000.0                    7
5   Michael Palin  05/23/13  66000.0                    8
=================================================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt', index_col='Name')
print(df)

               Hire Date   Salary  Sick Days remaining
Name                                                  
Graham Chapman  03/15/14  50000.0                   10
John Cleese     06/01/15  65000.0                    8
Eric Idle       05/12/14  45000.0                   10
Terry Jones     11/01/13  70000.0                    3
Terry Gilliam   08/12/14  48000.0                    7
Michael Palin   05/23/13  66000.0                    8
======================================================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt', index_col='Name', parse_dates=['Hire Date'])
print(df)

                Hire Date   Salary  Sick Days remaining
Name                                                   
Graham Chapman 2014-03-15  50000.0                   10
John Cleese    2015-06-01  65000.0                    8
Eric Idle      2014-05-12  45000.0                   10
Terry Jones    2013-11-01  70000.0                    3
Terry Gilliam  2014-08-12  48000.0                    7
Michael Palin  2013-05-23  66000.0                    8
===========================================================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)

                    Hired   Salary  Sick Days
Employee                                     
Graham Chapman 2014-03-15  50000.0         10
John Cleese    2015-06-01  65000.0          8
Eric Idle      2014-05-12  45000.0         10
Terry Jones    2013-11-01  70000.0          3
Terry Gilliam  2014-08-12  48000.0          7
Michael Palin  2013-05-23  66000.0          8
==============================================================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt',
            index_col='Employee',
            parse_dates=['Hired'],
            header=3,
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)

                   Hired   Salary  Sick Days
Employee                                    
Terry Jones   2013-11-01  70000.0          3
Terry Gilliam 2014-08-12  48000.0          7
Michael Palin 2013-05-23  66000.0          8

======================================================================
2. Writing CSV Files With pandas :
=========================================================
Name,Hire Date,Salary,Sick Days remaining
Graham Chapman,03/15/14,50000.00,10
John Cleese,06/01/15,65000.00,8
Eric Idle,05/12/14,45000.00,10
Terry Jones,11/01/13,70000.00,3
Terry Gilliam,08/12/14,48000.00,7
Michael Palin,05/23/13,66000.00,8

import pandas
df = pandas.read_csv('data.txt',
            index_col='Employee',
            parse_dates=['Hired'],
            header=0,
            names=['Employee', 'Hired', 'Salary', 'Sick Dayz'])
df.to_csv('data_modified.txt')
print(df.to_csv)


<bound method NDFrame.to_csv of                     Hired   Salary  Sick Dayz
Employee                                     
Graham Chapman 2014-03-15  50000.0         10
John Cleese    2015-06-01  65000.0          8
Eric Idle      2014-05-12  45000.0         10
Terry Jones    2013-11-01  70000.0          3
Terry Gilliam  2014-08-12  48000.0          7
Michael Palin  2013-05-23  66000.0          8
================================================================
