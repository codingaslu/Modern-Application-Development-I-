from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_om.sqlite3"

class Category(db.Model):
    cat_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    cat_name = db.Column(db.String(50), nullable = False)
    items = db.relationship('Item', backref = "category")

    def __repr__(self):
        return f"<Category name {self.cat_name}>"


class Item(db.Model):
    item_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    item_name = db.Column(db.String(50), nullable = False)
    cat = db.Column(db.Integer(), db.ForeignKey('category.cat_id'), nullable = False)
    # category = db.relationship('Category', backref = "items")


# c1 = (<Item 1>,<Item 2)
# c1.items

# i1.category
# <Category 1>

# Category 1 <-----> Item 1
# Category 1 <-----> Item 2

# Item 1 <-----> category 1