from tkinter import CASCADE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import os

app = Flask(__name__) # instantiate the application.Here __name__ is equal to "app"(file name).app.py is the module.

db = SQLAlchemy(app) # Creating/Instantiate db Object of SQLAlchemy & Pass app as arguement

#current_dir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///"+ os.path.join(current_dir,"mydatabom.sqlite3")  # This is how we configure our database with our application.When it run,it will create database in the local directory.

app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///mydatabom.sqlite3"
# Every table in the database refers to every class in our python program
# How to map that as tables and their records will be done by sql-alchemy

class Section(db.Model): #db.Model class,which is inherited by the class Section.db.Model Column(),Integer etc.
    section_id = db.Column(db.Integer(), primary_key=True) # Setting primary key to true will take care of not nullable and auto increamented.you can explicitly also set to true auto incremented as well 
    section_name =db.Column(db.String(50),nullable=False) # Setting nullable false then my table set in a way that cannot kept it empty.
    books = db.relationship("Book", backref="section",cascade="all, delete")#cascade will take care if the parent deleted then the child also get deleted #backref act as suodo column section and also do the job of #back_populates = "section") #It establishiing the relationship so that you can directly accesss all the books that belong to the section
    #whenever i create this books what it will do is it will make use of the foreign key attribute created in the table Book section.section_id.It will map the section.section id with section.books and create a collection for all the books whose section is some particular single value.It is happening in the background.we donot have to explicitly add some value to the book attribue whenever i create section. 
    def __repr__(self): #if any object return then it will be in this format only
        return "< Section %r>" % self.section_name

class Book(db.Model):
    book_id = db.Column(db.Integer(), primary_key=True) # Setting primary key to  will take care of not nullable and auto increamented.you can explicitly true auto incremented as well 
    book_name =db.Column(db.String(50),nullable=False)# Setting nullable false then my table set in a way that cannot kept it empty.
    sect = db.Column(db.Integer(),db.ForeignKey("section.section_id"),nullable = False) #we are setting foreign key and passing (tablename.columnname).Here we are passing tablename not the class name.Eventhough Class name is same as tablename,table name is saved as small letters.Thats why use section instead of Section
    #section =db.relationship("Section", back_populates = "books") #overlaps = "books" for suppress the waring but back_populates solve the problem
    def __repr__(self):
        return "< Book %r>" % self.book_name
    
    
    
#if we do some changes on the schema then it will require to create database form the scratch.


    

