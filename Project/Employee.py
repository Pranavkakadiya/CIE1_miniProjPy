from PermanentEmployee import Per_Emp
from Validation import validation
from connect import myconnect


class Employee:
    _empname = ""
    _emptype = ""
    _empemail = ""
    _empsalary = ""

    def __init__(self):
        self._empname = input("enter name : ")
        self._empemail = input("enter email : ")
        self._empmob = input("enter mobile no : ")
        self._emptype = input("enter type : ")
        self._empexp = int(input("enter experience :"))
        self._empsalary = self.getsalary()

    def getsalary(self):
        if self._emptype == "P" or self._emptype == "p":
            Opemp = Per_Emp()
            return Opemp.calculatesalary(self._empexp)
        else:
            print("Invalid Employee. Please enter only 'p' or 'P'")

    # 3
    @staticmethod
    def addnote():
        notes = input("Enter Notes : ")
        file = open("notes.txt", "a")
        file.writelines("\n")
        file.writelines(notes)
        file.close()

Running=True
while(Running):
    print("1. Add Emp")
    print("2. Display Emp")
    print("3. Add Notes")
    print("4.Quit")
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        c = Employee()
        if validation.validateemail(c._empemail) and validation.validatetemobile(c._empmob):
            obj = myconnect()
            obj.savetodb(c._empname, c._empemail, c._empmob, c._emptype, c._empexp, c._empsalary)
        else:
            print("Invalid Email OR Mobile Number!")
    elif choice == 2:
        obj = myconnect()
        obj.display()
    elif choice == 3:
        Employee.addnote()
    elif choice == 4:
        print("goodbye")
        Running=False
    else:
        print("invalid choice")
