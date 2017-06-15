# -*- coding: utf-8 -*-
#from student import Student
from datetime import datetime 


class AlreadyRentError:
	def __init__(self,student):
		self.msg="貸出中です"
		self.student=student

	def getMessage(self):
		return self.student.getName() + " に " + self.msg


class NotRentError:
	def __init__(self,book):
		self.msg="貸出されていません"
		self.book=book

	def getMessage(self):
		return self.book.getName() + " は " + self.msg

class Book:
	"""A simple book class"""
	def __init__(self,name):
		self.name = name
		self.student = None
		self.rentDate = None

	def getName(self):
		return self.name

	def back(self,str_date):
		if self.student is not None:
			self.student.back(self,str_date)
			self.student=None
			self.rentDate = None
		else:
			raise NotRentError(self)

	def rent(self, student,str_date):
		if self.student is None:
			self.student = student
			self.rentDate=datetime.strptime(str_date, "%Y-%m-%d").date()
			self.student.rent(self)
		else:
			raise AlreadyRentError(self.student)

	def getStudent(self):
		return self.student

	def getRentDate(self):
		return self.rentDate
