# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.
def calc_gross(salary,benefits):
    gross=salary+benefits
    return gross
basic_salary=float(input('Enter Basic Salary'))
benefits=float(input('Enter benefits'))
gross_salary=calc_gross(basic_salary,benefits)

