class NegativeSalaryException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

Salary=int(input("Enter Salary:"))
if Salary<0:
    try:
        raise NegativeSalaryException("Negative Salary")
    except Exception as e:
        print(e)
else:
    print("Salary=",Salary)