# -*- coding: utf-8 -*-

from student import Student
from student import AlreadyRentError as student_AlreadyRentError 
from student import OverRentError
from book import Book
from book import AlreadyRentError as book_AlreadyRentError 
from book import NotRentError

b1=Book("SQL")
print b1.getName()
b2=Book("XML")
print b2.getName()
b3=Book("Java")
print b3.getName()
b4=Book("JSP")
print b4.getName()

aStudent=Student("小林")
print aStudent.getName()

bStudent=Student("大林")
print bStudent.getName()

try:
	b1.rent(aStudent)
	b2.rent(aStudent)
	b3.rent(aStudent)
	for b in aStudent.listBooks():
		print b.getName()

	b4.rent(aStudent)
except OverRentError as err:
    print err.getMessage()

try:
	b1.rent(aStudent)
	b2.rent(aStudent)
	b3.rent(aStudent)
	for b in aStudent.listBooks():
		print b.getName()

	b3.rent(aStudent)
except book_AlreadyRentError as err:
    print err.getMessage()

