credit_score=int(input('Enter your credit score:'))
if credit_score>700:
    annual_income=float(input('Enter annual income:'))
    if annual_income>50000:
        print('Loan approved')
    else:
        print('Income requirement not met')
else:
    print('Credit Score too low')
