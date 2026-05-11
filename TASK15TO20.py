# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.
def calc_gross(salary,benefits):
    gross=salary+benefits
    return gross
basic_salary=float(input('Enter Basic Salary:'))
benefits=float(input('Enter benefits:'))
gross_salary=calc_gross(basic_salary,benefits)
print(gross_salary)
def find_NHIF(gross_salary):
    if gross_salary <= 5999: 
        nhif= 150
    elif gross_salary <= 7999: 
        nhif= 300
    elif gross_salary <= 11999:
        nhif= 400
    elif gross_salary <= 14999: 
        nhif= 500
    elif gross_salary <= 19999: 
        nhif= 600
    elif gross_salary <= 24999: 
        nhif= 750
    elif gross_salary <= 29999: 
        nhif=850
    elif gross_salary <= 34999: 
        nhif= 900
    elif gross_salary <= 39999:
        nhif= 950
    elif gross_salary <= 44999:
        nhif= 1000
    elif gross_salary <= 49999: 
        nhif= 1100
    elif gross_salary <= 59999: 
        nhif= 1200
    elif gross_salary <= 69999: 
        nhif= 1300
    elif gross_salary <= 79999:
        nhif= 1400
    elif gross_salary <= 89999:
        nhif= 1500
    elif gross_salary <= 99999: 
        nhif= 1600
    else: 
        nhif= 1700
    return nhif

find1=find_NHIF(gross_salary)
print('NHIF is',find1)

# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
def find_NSSF(gross_salary):
    if gross_salary>=18000:
        nssf=0.06 * gross_salary
    else:
        nssf='Minimum gross salaray is 18000'
    return nssf
find2=find_NSSF(gross_salary)
print('NSSF is',find2)

# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
def find_NHDF(gross_salary):
    nhdf = gross_salary *  0.015
    return nhdf
find3=find_NHDF(gross_salary)
print('NHDF is',find3)

# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
def find_taxableincome():
    taxable_income = gross_salary - (find1 + find2 + find3) 
    return taxable_income
find4=find_taxableincome()
print('Taxable income is',find4)

# Continue with the same program and find the person's PAYEE using the taxable income above.
def find_payee(taxable_income):
    if taxable_income <= 24000:
        tax = taxable_income * 0.1
    elif taxable_income <= 32333:
        tax = (24000 * 0.1) + (taxable_income - 24000) * 0.25
    elif taxable_income <= 500000:
        tax = (24000 * 0.1) + (8333 * 0.25) + (taxable_income - 32333) * 0.30
    elif taxable_income <= 800000:
        tax = (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.30) + (taxable_income - 500000) * 0.32
    else:
        tax = (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.30) + (300000 * 0.32) + (taxable_income - 800000) * 0.35
    personal_relief=2400
    return max(0,tax-personal_relief)
taxable_income = gross_salary - (find1 + find2 + find3)
find5=find_payee(taxable_income)
print('payee is',find5)

# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def find_netsalary():
    net_salary = gross_salary - (find1+find2+find3+find4+find5)
    return net_salary
find6=find_netsalary()
print(find6)


