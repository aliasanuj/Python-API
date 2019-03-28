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

























