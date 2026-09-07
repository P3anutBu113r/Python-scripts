from calendar import weekday

StaffName = input("What is the staff members name? ")
WeekDayHours = int(input("How many weekday hours worked? "))
WeekEndHours = int(input("How many week end hours worked? "))
while True:
    Role = input("What is the employee role? [J] Junior or [S] Senior")
    Role = Role.upper()

    if Role == "J":
        Rate = 15
        Role = "Junior"
        break

    elif Role == "S":
        Rate = 22
        role = "Senior"
        break
    else:
        print("Invalid role")
WeekDayPay = WeekDayHours * Rate
WeekEndPay = WeekEndHours * Rate * 2
Pay = WeekDayPay + WeekEndPay
TotalHours = WeekDayHours + WeekEndHours
print("Name: ", StaffName)
print("Total Hours worked: ", TotalHours)
print("Role: ", Role)
print("Total Pay: ", Pay)