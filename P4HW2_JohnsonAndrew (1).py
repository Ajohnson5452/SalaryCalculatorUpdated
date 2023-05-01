# CTI-110

   # P3HW2 - Salary

   # Andrew Johnson

   # 3/31/2023
#1st Input
name = (input("Do you want to enter a employee or \"Done\" to terminate: "))
hours = 0
payrate = 0

#overtime_pay
overtime_pay = 0
#overtime_hours
overtime_hours = 0
#regular pay
reg_pay = 0
#Overtime Total
overtime_total = 0
gross = 0
number = 1
#total Employees
employee_num = 0  
#total Gross
total_gross = 0
#total overtime
total_overtime = 0
#total regular hours
total_regular_hours = 0
    
while name != "Done":
    employee_num += 1 
    name = (input("Enter name: "))
    hours = float(input(f"Number of hours {name} worked: "))
    payrate = float(input(f"What is {name}'s pay rate:$ "))
    payrate += 1
    if hours <= 40:
        pay = (payrate * hours)
        reg_pay = hours * payrate
        gross = reg_pay + overtime_total
        total_gross += gross 
        total_regular_hours += reg_pay
        print("---------------------------------------")
        print(f"Employee Name: {name}")
        print(f"Hours Worked: {hours}")
        print(f"Pay Rate:$ {payrate}")
        print(f"Regular Pay:$ {reg_pay}")
        print(f"Gross Pay:$ {gross}")
    if hours > 40:
        pay = ((payrate * hours) + (overtime_pay * overtime_hours))
        overtime_hours = (( hours - 40))
        overtime_pay = payrate + (payrate / 2)
        overtime_total =  overtime_pay * overtime_hours
        hours -= overtime_hours
        reg_pay = hours * payrate
        gross = reg_pay + overtime_total
        print("---------------------------------------")
        print(f"Employee Name: {name}")
        print(f"Hours Worked: {hours}")
        print(f"Pay Rate:$ {payrate}")
        print(f"Overtime: {overtime_hours}")
        print(f"Overtime Pay Rate:${overtime_pay}")
        print(f"Overtime Pay:$ {overtime_total}")
        print(f"Regular Pay:$ {reg_pay}")
        print(f"Gross Pay:$ {gross}")
        total_gross += gross
        total_overtime += overtime_hours
        total_regular_hours += reg_pay
        print("-----------------------------------------")
       
    name = (input("Do you want to enter another employee: or \"Done\" to terminate: "))
        
        #Total Number of Employees:
print(f"Number of Employees: {employee_num} ") 
        
        #Total amount paid for overtime:
print(f"Total Overtime:$ {total_overtime}") 
        #Total amount paid for regular hours:
print(f"Total Regular Hours:$ {total_regular_hours}")
        #Total amount paid in gross:
print(f"Total Gross:$ {total_gross}") 
            









    #control C to get out of loop
