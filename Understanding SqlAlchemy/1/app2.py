from tkinter import CASCADE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import os

app = Flask(__name__) # instantiate the application.Here __name__ is equal to "app"(file name).app.py is the module.

db = SQLAlchemy(app) # Creating/Instantiate db Object of SQLAlchemy & Pass app as arguement

app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///mydatabmm.sqlite3"
# Every table in the database refers to every class in our python program
# How to map that as tables and their records will be done by sql-alchemy

class Section(db.Model): #db.Model class,which is inherited by the class Section.db.Model Column(),Integer etc.
    section_id = db.Column(db.Integer(),primary_key=True) 
    section_name =db.Column(db.String(50),nullable=False) # Setting nullable false then my table set in a way that cannot kept it empty.
    books = db.relationship("Book", backref="section",secondary='association')#secondary attribute take value of tabel assocaition
    #whenever i create this books what it will do is it will make use of the foreign key attribute created in the table Book section.section_id.It will map the section.section id with section.books and create a collection for all the books whose section is some particular single value.It is happening in the background.we donot have to explicitly add some value to the book attribue whenever i create section. 
    def __repr__(self): #if any object return then it will be in this format only
        return "< Section %r>" % self.section_name

class Book(db.Model):
    book_id=db.Column(db.Integer(),primary_key=True)     
    book_name=db.Column(db.String(50),nullable=False)# Setting nullable false then my table set in a way that cannot kept it empty.
    #section =db.relationship("Section", back_populates = "books") #overlaps = "books" for suppress the waring but back_populates solve the problem
    def __repr__(self):
        return "< Book %r>" % self.book_name
    
    class Association(db.Model):#
        #we are not setting individually primary key here we are setting combination of section_id and book_id is primary key 
        section_id = db.Column(db.Integer(),db.ForeignKey('section.section_id'),primary_key=True) 
        book_id = db.Column(db.Integer(), db.ForeignKey('book.book_id'),primary_key=True) 

    
#if we do some changes on the schema then it will require to create database form the scratch.


    

