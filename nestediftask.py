account_type=input('Enter account type standard or premium:').lower().strip
tran_amount=float(input('Enter Transaction amount:'))
if account_type== 'standard':
    if tran_amount>500:
        print('Transaction exceeds the limit for Standard accounts.')
    else:
        print('Transaction approved.')
elif account_type=='premium':
    if tran_amount>1000:
        print('Transaction exceeds the limit for Premium accounts.')
    else:
        print('Transaction approved.')
else:
    print('“Wrong account type')