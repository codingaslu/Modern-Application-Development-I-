from jinja2 import Template
import matplotlib.pyplot as plt
import sys
import csv

with open("data.csv", 'r') as f:
    csv_reader = csv.DictReader(f)
    data = list(csv_reader)

sid=[]
cid=[]
for d in data:
    sid.append(int(d["Student id"]))
    cid.append(int(d[" Course id"])) 
     
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
</head>
<body>
   {% if Decision == "-s" %}
    <h1>Student Details</h1>
    <table border="1" cellsapcing="0"  style="text-align:center">
        <thead>
            <tr>
                <th>Student id</th>
                <th>Course id</th>
                <th>Mark</th>
            </tr>
        </thead>
        <tbody>
            {% for d in data %}
                    <tr>
                        <td>{{d["Student id"]}}</td>
                        <td>{{d[" Course id"]}}</td>
                        <td>{{d[" Marks"]}}</td>
                    </tr>
            {% endfor %}
        </tbody>
        <tfoot>
            <tr>
                <td colspan="2" >Total</td>
                <td>{{Sum}}</td>
            </tr>
        </tfoot>
    </table>
   {% elif Decision == "-c" %}
      <h1>Course Details</h1>
    <table border="1" cellsapcing="0"  style="text-align:center">
        <thead>
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{{avg}}</td>
                <td>{{max}}</td>
            </tr>
        </tbody>
    </table>
    <img src="histo.PNG">
   {% else %}
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
    {% endif %}
</body>
</html> 
"""


def main():
    if len(sys.argv) > 2:
        Decision = sys.argv[1]
        ID = sys.argv[2]
        filter_data = []    
        if Decision == '-s' and int(ID) in sid:
            Sum = 0
            for d in data:
                if (d["Student id"] == ID):
                    filter_data.append(d)
                    Sum = Sum+int(d[" Marks"])
            template = Template(TEMPLATE)
            output = open('output.html', 'w')
            output.write(template.render(data=filter_data, Sum=Sum,title = "Student Details",Decision=Decision))
            output.close()
        elif Decision == "-c" and int(ID) in cid:
            Count = 0
            max = 0
            Total = 0
            for d in data:
                if (int(d[" Course id"]) == int(ID)):
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
            plt.savefig('histo.PNG')
            avg = Total/Count   
            template = Template(TEMPLATE)
            output = open('output.html', 'w')
            output.write(template.render(avg=avg, max=max,title = "Course Data",Decision=Decision))
            output.close()
        else:
            template = Template(TEMPLATE)
            output = open('output.html', 'w')
            output.write(template.render(title = "Something Went Wrong"))
            output.close()
    else:
        template = Template(TEMPLATE)
        output = open('output.html', 'w')
        output.write(template.render(title = "Something Went Wrong"))
        output.close()
    
        
if __name__ == "__main__":
    main()
