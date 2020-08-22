class Per_Emp:

      basic_salary = 5000
      def calculatesalary(self,exp):
            if (exp >= 15):
                  return self.basic_salary + (self.basic_salary * 20) / 100
            elif (10 <= exp < 15):
                  return self.basic_salary + (self.basic_salary * 10) / 100
            elif (5 <= exp < 10):
                  return self.basic_salary + (self.basic_salary * 5) / 100
            else:
                  return self.basic_salary
