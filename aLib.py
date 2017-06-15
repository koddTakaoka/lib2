# -*- coding: utf-8 -*-

from student import Student
from student import AlreadyRentError as student_AlreadyRentError 
from student import OverRentError
from student import NotRentError as student_NotRentError 
from book import Book
from book import AlreadyRentError as book_AlreadyRentError 
from book import NotRentError as book_NotRentError 

b1=Book("SQL")
print b1.getName()
b2=Book("XML")
print b2.getName()
b3=Book("Java")
print b3.getName()
b4=Book("JSP")
print b4.getName()
b5=Book("CSS")
print b5.getName()

aStudent=Student("小林")
print aStudent.getName()

bStudent=Student("大林")
print bStudent.getName()

try:
	b1.rent(aStudent,"2017-6-15")
	b2.rent(aStudent,"2017-6-15")
	b3.rent(aStudent,"2017-6-15")
	for b in aStudent.listBooks():
		print b.getName()+ b.getRentDate().strftime("%Y-%m-%d") + b.getStudent().getName()

   	b5.rent(aStudent,"2017-6-15")
	b4.rent(aStudent,"2017-6-15")
except (OverRentError,book_AlreadyRentError) as err:
    print err.getMessage()

try:
	b1.back("2017-6-15")
	b2.back("2017-6-15")
	b3.back("2017-6-15")
	print "after all books were returned as below list is empty"
	for b in aStudent.listBooks():
		print b.getName()+ b.getRentDate().strftime("%Y-%m-%d") + b.getStudent().getName()
	print "all books were returned"
except (book_NotRentError,student_NotRentError) as err:
    print err.getMessage()

try:
	b1.rent(bStudent,"2017-6-15")
	b2.rent(bStudent,"2017-6-15")
	b3.rent(bStudent,"2017-6-15")
	for b in bStudent.listBooks():
		print b.getName()+ b.getRentDate().strftime("%Y-%m-%d") + b.getStudent().getName()

  	b5.rent(bStudent,"2017-6-15")
#  	b3.rent(aStudent,"2017-6-15")
except (book_AlreadyRentError,OverRentError) as err:
    print err.getMessage()

try:
	b4.back("2017-6-15")

except book_NotRentError as err:
    print err.getMessage()
