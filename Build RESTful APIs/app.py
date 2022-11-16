from flask import Flask
from resources import api
from models import db

app = Flask(__name__)
db.init_app(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
api.init_app(app) #instatiate api

@app.route('/')
def index():
    return "hello"
  
if __name__ == '__main__':
    app.run()