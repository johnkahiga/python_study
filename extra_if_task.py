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
elif length>=10 and password.upper() and password.isdigit():
    print('strong') 
else:
    print('does not meet the requirements')

password=input('Enter Password:')
if password.upper:
    print('Invalid')
elif password[-1].isdigit():
    print('Invalid')
else:
    print('Valid pasword')

num=int(input('Enter Number'))
if num%3 ==0:
    print('fizz')
elif num%5 ==0:
    print('buzz')
elif num%3 ==0 and num%5 ==0:
    print('fizzbuzz')
else:
    print('num')

