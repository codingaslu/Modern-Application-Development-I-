from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello,World!"

@app.route("/route1",methods=["POST"])
def function1():
    return "This is my second function"

@app.route("/route2",methods=["GET"])
def function2():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()