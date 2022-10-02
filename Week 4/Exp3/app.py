
from flask import Flask
from flask import request
from flask import render_template
import csv
import matplotlib.pyplot as plt

with open("data.csv",'r') as f:
    csv_reader = csv.DictReader(f)
    data=list(csv_reader)
filter_data=[]
sid=[]
cid=[]
for d in data:
    sid.append(int(d["Student id"]))
    cid.append(int(d[" Course id"])) 


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def Web():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        if len(request.form.keys()) < 2 or request.form["id_value"] == "":
            return render_template("details.html",title = "Something Went Wrong")
        filter_data.clear()
        id_name = request.form["ID"]
        id_value = int(request.form["id_value"])
        if id_name=="student_id" and int(id_value) in sid:
            Total_Mark=0
            for d in data:
                if int(d["Student id"]) == int(id_value):
                    filter_data.append(d) 
                    Total_Mark= Total_Mark + int(d[" Marks"])    
            return render_template("details.html",title="Student Details",ID =id_name,data=filter_data,Total_Mark=Total_Mark)
        elif id_name=="course_id" and int(id_value) in cid:
            max=0
            Total=0
            Count=0
            for d in data:
                if int(d[" Course id"]) == int(id_value):
                    Count = Count + 1
                    Total = Total+int(d[" Marks"])
                    filter_data.append(d[" Marks"])
                    if (int(d[" Marks"]) > max):
                        max = int(d[" Marks"])
            marks = sorted(filter_data)
            avg=0
            plt.hist(marks)
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('static\histo.PNG')
            avg = Total/Count    
            return render_template("details.html",title="Course Details",ID = "course_id",avg=avg, max=max)
        else:
            return render_template("details.html",title = "Something Went Wrong")
    
    else:
        return render_template("details.html",title = "Something Went Wrong")
    
if __name__ == "__main__":
    app.debug = False
    app.run()
