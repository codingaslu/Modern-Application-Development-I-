from flask import Flask, render_template, request, redirect 
from models import *

app = Flask(__name__)
db.init_app(app)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_mm.sqlite3"

@app.route("/")
def home():
    cat = Category.query.all()
    return render_template("all_cat.html", cat = cat)

@app.route("/create_cat", methods = ["GET", "POST"])
def create_c():
    if request.method == "POST":
        cat = request.form['c_name']
        new_cat = Category(cat_name = cat)
        db.session.add(new_cat)
        db.session.commit()
        return redirect('/')

    return render_template('create_cat.html')

@app.route("/items/<int:cat_id>")
def items_cat(cat_id):
    this_cat = Category.query.get(cat_id)
    items = this_cat.items 
    return render_template("items.html", items = items)


if __name__ == "__main__":
    app.run(debug = True)

# (1,1) (1,2) (2,1)