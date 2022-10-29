from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Category(db.Model):
    cat_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    cat_name = db.Column(db.String(50), nullable = False)
    items = db.relationship('Item', backref = "category", secondary = 'associate')

    def __repr__(self):
        return f"<Category name {self.cat_name}>"


class Item(db.Model):
    item_id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    item_name = db.Column(db.String(50), nullable = False)
   

class Associate(db.Model):
    id_cat = db.Column(db.Integer(), db.ForeignKey('category.cat_id'), primary_key = True)
    id_item = db.Column(db.Integer(), db.ForeignKey('item.item_id'), primary_key = True)