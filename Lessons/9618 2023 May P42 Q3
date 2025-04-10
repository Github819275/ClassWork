class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay = HourlyPay  # PRIVATE HourlyPay : REAL
        self.__EmployeeNumber = EmployeeNumber  # PRIVATE EmployeeNumber : STRING
        self.__JobTitle = JobTitle  # PRIVATE JobTitle : STRING
        self.__PayYear2022 = [0.0 for i in range(52)]  # PRIVATE PayYear2022[0:51] OF REAL

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, week_number, hours_worked):
        week_pay = self.__HourlyPay * hours_worked
        self.__PayYear2022[week_number] = week_pay

    def GetTotalPay(self):
        total = 0
        for i in range(52):
            total = total + self.__PayYear2022[i]
        return total


class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue = BonusValue  # PRIVATE BonusValue : REAL

    def SetPay(self, week_number, hours_worked):
        new_hours = hours_worked * ((100+self.__BonusValue)/100)
        Employee.SetPay(self, week_number, new_hours)


def EnterHours():
    file2 = open('HoursWeek1.txt', 'r')
    for i in range(8):
        number = file2.readline().strip()
        hours = float(file2.readline().strip())
        for j in range(8):
            compare = EmployeeArray[j].GetEmployeeNumber()
            if number == compare:
                EmployeeArray[j].SetPay(1, hours)
    file2.close()


# Main Program
EmployeeArray = []
file = open('Employees.txt', 'r')
hourly_pay = file.readline().strip()
while len(hourly_pay) > 0:
    is_manager = False
    hourly_pay = float(hourly_pay)
    employee_number = file.readline().strip()
    unknown = file.readline().strip()
    try:
        bonus_value = float(unknown)
        is_manager = True
        job_title = file.readline().strip()
    except:
        job_title = unknown
    if is_manager == True:
        temp = Manager(hourly_pay, employee_number, job_title, bonus_value)
    else:
        temp = Employee(hourly_pay, employee_number, job_title)
    EmployeeArray.append(temp)
    hourly_pay = file.readline().strip()
file.close()


EnterHours()
for i in range(8):
    obj = EmployeeArray[i]
    print('Employee number: ',  obj.GetEmployeeNumber(), ' Total Pay: ', obj.GetTotalPay())
