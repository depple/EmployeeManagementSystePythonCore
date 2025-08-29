class Employee:
    
    # Default Constructor
    def __init__(self):
        self.EmployeeDict = {
            1: {'name': 'Jay Prajapati', 'age': 22, 'department': 'Technical', 'salary': 20000},
            2: {'name': 'Deep Patel', 'age': 24, 'department': 'Development', 'salary': 15000},
            3: {'name': 'Ravi Sharma', 'age': 28, 'department': 'HR', 'salary': 18000},
            4: {'name': 'Sneha Mehta', 'age': 26, 'department': 'Technical', 'salary': 22000},
            5: {'name': 'Amit Singh', 'age': 30, 'department': 'Finance', 'salary': 25000},
            6: {'name': 'Priya Nair', 'age': 27, 'department': 'Development', 'salary': 21000},
            7: {'name': 'Kunal Desai', 'age': 25, 'department': 'Support', 'salary': 16000},
            8: {'name': 'Neha Gupta', 'age': 29, 'department': 'HR', 'salary': 19000},
            9: {'name': 'Manish Yadav', 'age': 32, 'department': 'Technical', 'salary': 28000},
            10: {'name': 'Anjali Verma', 'age': 24, 'department': 'Development', 'salary': 17000},
            11: {'name': 'Rohit Malhotra', 'age': 31, 'department': 'Finance', 'salary': 26000},
            12: {'name': 'Kavya Iyer', 'age': 23, 'department': 'Support', 'salary': 15000},
            13: {'name': 'Siddharth Chauhan', 'age': 29, 'department': 'Technical', 'salary': 23000},
            14: {'name': 'Pooja Kulkarni', 'age': 27, 'department': 'Development', 'salary': 20000},
            15: {'name': 'Aditya Joshi', 'age': 28, 'department': 'HR', 'salary': 18500},
            16: {'name': 'Ritu Bansal', 'age': 26, 'department': 'Finance', 'salary': 24000},
            17: {'name': 'Harsh Vora', 'age': 25, 'department': 'Support', 'salary': 15500},
            18: {'name': 'Divya Reddy', 'age': 30, 'department': 'Technical', 'salary': 27000},
            19: {'name': 'Vivek Choudhary', 'age': 33, 'department': 'Development', 'salary': 30000},
            20: {'name': 'Meera Das', 'age': 24, 'department': 'HR', 'salary': 17500}
        }
       
    # Get List of Employee
    def GetList(self):
        return self.EmployeeDict
    
    # Add Employee Data
    def AddEmployee(self, EmployeeData: dict):
        empId = list(EmployeeData.keys())[0]
        if empId in self.EmployeeDict:
            return "This Employee Id is Already Exist."
        else:      
            self.EmployeeDict.update(EmployeeData)
            return "Successfully Add Data"
    
    # Search Employee By Id 
    def GetEmployeeById(self,EmployeeId):
        if EmployeeId in self.EmployeeDict:
            return self.EmployeeDict[EmployeeId]
        else:
            return "This Employee Id is Not Exist."