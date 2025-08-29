from EmployeeClass import Employee
def main_menu():
    Run = True
    emp = Employee()
    while(Run):
        print("============================= Welcome to Employee Management System =========================")
        print("Please Select Menu From Below:-")
        print("1. Add Employee")
        print("2. View All Employee")
        print("3. SearchEmployee By Id")
        print("4. Exit")
        choice = int(input("Please Enter No From 1 to 4 :-"))
        if choice == 1:
            add_employee(emp)
        elif choice == 2:
            view_employees(emp)
        elif choice == 3:
            search_employee(emp)
        elif choice == 4:
            print("Your Application is Exist. Thanks for Using Employee Management Application.")
            Run = False

def add_employee(emp: Employee):
    print("===================================================")
    EmployeeId = max(emp.EmployeeDict.keys()) + 1
    print("Employee Id = ",EmployeeId)
    Name = input("Please Enter Name:-")
    Age = int(input("Please Enter Age:-"))
    Department = input("Please Enter Department:-")
    Salary = int(input("Please Enter Salary:-"))
    EmployeeData = {
        EmployeeId:{
            'name':Name,
            'age':Age,
            'department':Department,
            'salary':Salary
        }
    }
    msg = emp.AddEmployee(EmployeeData)
    print(msg)
    print("===================================================")

# GetList By Employee
def view_employees(emp: Employee):
    print("===================================================")
    print("Id\tName\t\tAge\tDepartment\tSalary")
    list = emp.GetList()
    # print(list)
    for key in list:
        data = list[key]
        print(key,'\t', data['name'],'\t',data['age'],'\t',data['department'],'\t',data['salary'])
    print("===================================================")
    
# GetEmployee By Id
def search_employee(emp: Employee):
    EmpId = int(input("Please Enter Employee Id :-"))
    data = emp.GetEmployeeById(EmpId)
    print("===================================================")
    print("Id\tName\t\tAge\tDepartment\tSalary")
    print(EmpId,end="\t")
    for key in data:
        print(data[key],end="\t")
    print("")
    print("===================================================")    
    
    
    

main_menu()