from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin,login_required,login_user,logout_user,current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite3'
app.config['SECRET_KEY'] = 'thisismysecretkeyiitm@1234' #A secret key that will be used for securely signing the session cookie.
db = SQLAlchemy(app)
login_manager =LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model): #UserMixing will implement four properties of this login manager[is active,is authenticated,is anonymous and get id].
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    def __init__(self,id, name):
        self.id = id
        self.name = name
@login_manager.user_loader #it load the user information from the user id stored in the session.#login_user automatically invoke that login manager.user_login
def firstuser(id):
    return User.query.get(int(id))
@app.route('/')
def index():
    u1 = User.query.filter_by(name ='Rose').first()
    login_user(u1)
    return 'logged in'
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logged out'

@app.route('/home')
@login_required
def home():
    return "current_user is " + current_user.name

def init_db():
    db.create_all()
    new_user = User(112,'Rose')
    db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    #init_db()
    app.run(host = '0.0.0.0', debug = True)
    
    