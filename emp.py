from unittest import result
import pymongo

connection=pymongo.MongoClient("mongodb://localhost:27017")
mydb=connection["employeeDb"]
myemployee=mydb["employees"]


while True:
    print("   Menu   \n")
    print("1.Add an employee \n")
    print("2.View all employees \n")
    print("3.Search an employee \n")
    print("4.Delete an employee \n")
    print("5.Update an employee \n")
    print("6.Employee name starts upto")
    print("7.Exit \n")
    option=int(input("Select an option: "))
    if option==1:
        print("Add an employee option selected")
        empCode=input("Enter an employee code: ")
        empName=input("Enter an employee name: ")
        empDesignation=input("Enter designation: ")
        data={"EmployeeCode":empCode,"EmployeeName":empName,"EmployeeDesignation":empDesignation}
        print(data)
        myemployee.insert_one(data)
        print("Data added successfully")
    elif option==2:
        print("View all employees option selected")
        result=myemployee.find({},{"_id":0,"EmployeeDesignation":0}).sort("EmployeeName",-1)
        for i in result:
            print(i)
    elif option==3:
        print("Search an employee option selected")
        empCode=input("Enter an employee code")
        data={"EmployeeCode":empCode}
        result=myemployee.find_one(data,{"_id":0})
        print(result)
    elif option==4:
        print("Delete an employee option selected")
        empCode=input("Enter an employee code to be deleted")
        data={"EmployeeCode":empCode}
        result=myemployee.delete_one(data)
        print("Data deleted successfully")

    elif option==5:
        print("Update an employee option selected")
        empCode=input("Enter an employee code to be updated: ")
        empName=input("Enter employee name: ")
        empDesignation=input("Enter designation: ")
        setData={"EmployeeCode":empCode}
        newData={"$set":{"EmployeeName":empName,"EmployeeDesignation":empDesignation}}
        myemployee.update_one(setData,newData)
        print("Data updated successfully")
    elif option==6:
        ip=input("Enter starting name of employee: ")
        condition={"EmployeeName":{"$gte":ip}}
        result=myemployee.find(condition)
        
        for i in result:
            print(i)
    
    
    else:
        break

