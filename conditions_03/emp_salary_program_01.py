# calc net salary based on gross salary and tax
# inputs
emp_name = 'Yahia Momtaz'
emp_gross_salary = 3000

if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0

emp_net_salary = emp_gross_salary - emp_gross_salary * tax / 100
print(emp_net_salary)
emp_annual_net_salary = emp_net_salary * 12
print(emp_annual_net_salary)
