from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"


@app.route("/")
def home():
    s1 = Student.query.all()
    length = len(s1)
    return render_template("Home.html", length=length, s1=s1)


@app.route("/student/create", methods=["GET", "POST"])
def addStudent():
    if request.method == "GET":
        return render_template("addstudent.html")
    if request.method == "POST":
        try:
            roll_no = request.form['roll']
            f_name = request.form['f_name']
            l_name = request.form['l_name']
            course = request.form['courses']
            stu = Student(roll_number=roll_no,first_name=f_name, last_name=l_name)
            db.session.add(stu)
            db.session.commit()
            courses = request.form.getlist('courses')
            for course in courses:
                enroll = Enrollments(estudent_id=stu.student_id, ecourse_id=int(course[-1]))
                db.session.add(enroll)
        except:
            db.session.rollback()
            return render_template("error.html")
        else:
            db.session.commit()
            return redirect('/')

@app.route('/student/<int:student_id>/update',methods=['GET', 'POST'] )
def update(student_id):
    if request.method == "GET":
        s=Student.query.get(student_id)
        return render_template("update.html",s=s)
    if request.method == "POST":
            f_name = request.form['f_name']
            l_name = request.form['l_name']
            course = request.form['courses']
            stu=Student.query.get(student_id)
            stu.first_name=f_name
            stu.last_name=l_name
            db.session.add(stu)

            Enrollments.query.filter_by(estudent_id=student_id).delete()
            courses = request.form.getlist('courses')
            for course in courses:
                enroll = Enrollments(estudent_id=student_id,ecourse_id=int(course[-1]))
                db.session.add(enroll)
            db.session.commit()
            return redirect('/')

@app.route('/student/<student_id>/delete', methods=['GET', 'POST'])
def delete(student_id):
        Stu = Student.query.filter_by(student_id=student_id).delete()
        Enrollments.query.filter_by(estudent_id=student_id).delete()
        db.session.flush()
        db.session.commit()
        return redirect('/')

@app.route('/student/<student_id>', methods=['GET', 'POST'])
def student_details(student_id):
    Stu_list = Student.query.get(student_id)
    enroll_list = Enrollments.query.filter_by(estudent_id=student_id).with_entities(Enrollments.ecourse_id)
    lst = []
    for num in enroll_list:
        lst.append(num['ecourse_id'])
    
    c_list = Course.query.join(Enrollments, Enrollments.ecourse_id == Course.course_id).filter_by(estudent_id=student_id).with_entities(Course.course_code, Course.course_name,Course.course_description)
   
    return render_template('studentdetails.html', student=Stu_list,courses=c_list)

            


class Student(db.Model):
    student_id = db.Column(db.Integer(), primary_key=True)
    roll_number = db.Column(db.Integer(), unique=True, nullable=False)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10))


class Course(db.Model):
    course_id = db.Column(db.Integer(), primary_key=True)
    course_code = db.Column(db.String(10), unique=True, nullable=False)
    course_name = db.Column(db.String(10), nullable=False)
    course_description = db.Column(db.String())


class Enrollments(db.Model):
    enrollment_id = db.Column(db.Integer(), primary_key=True)
    estudent_id = db.Column(db.Integer(), db.ForeignKey(
        'student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer(), db.ForeignKey(
        'course.course_id'), nullable=False)


if __name__ == "__main__":
    app.run(debug=True)
