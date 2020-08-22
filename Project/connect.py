import sqlite3


class myconnect:

    def __init__(self):
        self.con = sqlite3.connect("emp.db")
        self.con.execute(''' create table if not exists emp(
                              id integer primary  key AUTOINCREMENT,
                              name text,
                              email text,
                              mobile_no text,
                              type text,
                              experience integer,
                              salary text
                        ) ''')

    def savetodb(self, ename, eemail, emob, etype, eexp, esalary):
        with self.con:
            self.con.execute(
                "insert into emp(name,email,mobile_no,type,experience,salary) values(:name,:email,:mobile_no,:type,:experience,:salary)",
                {'name': ename, 'email': eemail, 'mobile_no': emob, 'type': etype, 'experience': eexp,
                 'salary': esalary})
        self.con.commit()

    def display(self):
        eid = input("enter the emp id: ")
        with self.con:
            dataEmp = self.con.execute(
                'select id,name,email,mobile_no,type,experience,salary from emp where id=:id',
                {'id': eid})
            l = dataEmp.fetchall()
            print("Name : " + l[0][1])
            print("Email : " + l[0][2])
            print("Mobile No. : " + l[0][3])
            print("Employee Type : " + l[0][4])
            print("Experience : ", l[0][5])
            print("Salary : ", l[0][6])

