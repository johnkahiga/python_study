password=input('Enter Password:')
email=input('Enter Email:')
correct_email='admin@gmail.com'
correct_password='admin123'
if password==correct_password and email==correct_email:
    print('Access granted')
elif email==correct_email and password!=correct_password:
    print('Wrong Password')
else:
    print('Email not found')

email=input('Enter Email:')
if '@' not in email or '.' not in email:
    print('Invalid email')
elif email.endswith('@gmail.com'):
    print('Gmail account')
else:
    print('Other email provider')

password=input('Enter Password:')
length=len(password)

if length<6:
    print('Weak')
elif length>=6 and length<10 and password.isdigit():
    print('Moderate')
elif length>=10 and password.isupper() and password!=password.isalpha():
    print('strong') 
else:
    print('does not meet the requirements')

password=input('Enter Password:')
if password[0].upper()==False and password[-1].isdigit()==False :
    print('Invalid')
else:
    print('Valid pasword')

num=int(input('Enter Number'))
if num%3 ==0 and num%5 ==0:
    print('fizzbuzz') 
elif num%3 ==0:
    print('fizz')
elif num%5 ==0:
    print('buzz')
else:
    print('num')

score=float(input('Enter Score'))
if score>=80:
    print('A')
elif score>=70 and score<80:
    print('B')
elif score>=60 and score<70:
    print('C')
elif score>=50 and score<60:
    print('D')
else:
    print('Failed')

num11=int(input('Enter first number'))
num22=int(input('Enter second number'))
if num11==num22:
    print('Equal')
elif num11>num22:
    print('num11 is greater')
else:
    print('num22 is greater')

day=int(input('Enter Day'))
if day>=1 and day<=5:
    print('Weekday')
elif day ==6 or day ==7:
    print('Weekend')
else:
    print('Invalid input')

temp=float(input('Enter the temperature'))
if temp<=0:
    print('Freezing')
elif temp<=15:
    print('Cold')
elif temp<=30:
    print('Warm')
else:
    print('Hot')

year=int(input('Enter a year'))
if year%4 ==0:
    print('Leap Year')
elif year%100==0:
    print('Century Year')
else:
    print('Common Year')