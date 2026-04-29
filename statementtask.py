num1=int(input('Enter first Number:'))
num2=int(input('Enter second Number: '))
num3=int(input('Enter second Number: '))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

temp=int(input('Enter Temperature:'))
if temp>=30:
    print('The Temperature is too high')
elif temp>=15:
    print('Normal Temperature')
else:
    print('Cold Temperature')

balance=float(input('Enter Balance:'))
if balance<100:
    print('Insufficient funds')
elif balance>=100 and balance<1000:
    print('Moderate balance')
else:
    print('High balance')

x=float(input('Enter number:'))
y=float(input('Enter number:'))
if x>=10 and x<=20 and y>100:
    print('Conditions Met')
else:
    print('Conditions not Met')

password=input('Enter Password:')
correct_password='secret123'
if password==correct_password:
    print('Access granted')
else:
    print('Access Denied')

password=input('Enter Password:')
email=input('Enter Email;')
correct_email='admin@gmail.com'
correct_password='admin123'
if password==correct_password and email==correct_email:
    print('Access granted')
else:
    print('Access Denied')

