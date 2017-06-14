# -*- coding: utf-8 -*-
#from book import Book

class AlreadyRentError:
	def __init__(self,book):
		self.msg="貸りています"
		self.books=book

	def getMessage(self):
		return self.book.getName() + " を " + self.msg


class OverRentError:
	def __init__(self,books):
		self.msg="すでに3冊貸りています"
		self.books=books

	def getMessage(self):
		return self.msg

class Student:
	"""A simple student class"""
	def __init__(self,name):
		self.name = name
		self.books = []

	def getName(self):
		return self.name

	def rent(self, book):
		if book not in self.books:
			if len(self.books) < 3 :
				self.books.append(book)
			else:
				raise OverRentError(self.books)
		else:
			raise AlreadyRentError(self.book)

	def listBooks(self):
		return self.books
