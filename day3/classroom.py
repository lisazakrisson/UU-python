#!/usr/bin/env python3

class Person(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def printName(self):
        print('Name: ' + self.firstName + ' ' + self.lastName)

class Student(Person):
    def __init__(self, firstName, lastName, subject):
        Person.__init__(self, firstName, lastName)
        self.subject = subject
    
    def printStudent(self):
        print('Name: ' + self.firstName + ' ' + self.lastName + '. Subject: ' + self.subject)

class Teacher(Person):
    def __init__(self, firstName, lastName, course):
        Person.__init__(self, firstName, lastName)
        self.course = course
    
    def printCourse(self):
        print('Name: ' + self.firstName + ' ' + self.lastName + '. Course: ' + self.course)    
        
