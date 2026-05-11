# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
email=input('Enter Email: ')
def email_validate(email):
    if '@'  in email and '.'  in email:
        valid='Valid Email'
    else:
        valid='Invalid Email'
    return valid

email1=email_validate(email)
print(email1)


# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks=int(input('Enter Student marks: '))
def mark_check(marks):
    if marks>0 and marks<=100:
        if marks >79:
            res='Grade A'
        elif marks>=60 and marks<79:
            res='Grade B'
        elif marks>=49 and marks<60:
            res='Grade C'
        elif marks>=40 and marks<49:
            res='Grade D'
        else:
            res='Grade E'
    else:
        res='Mark not within range'
    return res
mark1=mark_check(marks)
print(mark1)

# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
prods=[['omo','30kshs','300'],['milk','50kshs','200'],['bread','45kshs','359'],['coffee','kshs','79']]
def total_stock(prods):
    total=0
    for p in prods:
        total=total+ int(p[2])
    return total
stock1=total_stock(prods)
print(stock1)

# Write a program that prints the largest of 4 inputs taken as input from a user.
def largest_number(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        large=num1
    elif num2>num3 and num2>num3 and num2>num4:
        large=num2
    elif num3>num1 and num3>num2 and num3>num4:
        large=num3
    else:
        large=num4
    return large
input1=int(input('Enter the first number:'))
input2=int(input('Enter the second number:'))
input3=int(input('Enter the third number:'))
input4=int(input('Enter the fourth Number'))
numlarge=largest_number(input1,input2,input3,input4)
print(numlarge)

# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.

number=int(input('Enter the number'))
def type_number(number):
    if number%2==0:
        result='Number is even'
    else:
        result='Number is odd'
    return result
number1=type_number(number)
print(number1)



