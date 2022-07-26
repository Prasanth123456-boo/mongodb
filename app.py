from flask import Flask, render_template,request
import pymongo

connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["employeeDb"]
myemployee=mydb["employees"]

app = Flask(__name__)

@app.route("/read",methods=["POST"])
def read():
    if(request.method=="POST"):
        empCode=request.form.get("ecode")
        empName=request.form.get("ename")
        empDesignation=request.form.get("edesig")
        data={"EmployeeCode":empCode,"EmployeeName":empName,"EmployeeDesignation":empDesignation}
        print(data)
        myemployee.insert_one(data)
        print("Data added successfully")
        return render_template("display.html")
    else:
        return "Invalid"

@app.route("/view")
def view():
    result=myemployee.find({},{"_id":0}).sort("EmployeeName")
    datalist=[]
    for i in result:
        datalist.append(i)
    return render_template("display.html",data=datalist)

@app.route("/")
def hello_world():
    return render_template("index.html")
app.run()