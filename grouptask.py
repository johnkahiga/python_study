# Q1
# A registration portal must verify emails. Create a program that checks whether an email contains both @ and .com before accepting it.
email = input("Enter your email: ")
if "@" in email and ".com" in email:
    print("Registration successful!")
    
else:
    print("Invalid email. Must contain '@' and '.com'.")

# Q2
# A cinema only allows adults into some movies. Build a system that checks age and denies entry to anyone below 18 years.
name=input('Enter your Name:')
age = int(input("Enter your age: "))
if age >= 18:
    val=f"Entry granted for {name}. Enjoy the movie!"
else:
    val=f"Entry denied for {name}. This movie is for adults only."
print(val)

# Q3
# A library wants automatic fines. Create a program that charges KES 20 per late day after seven allowed days.
# days_kept = int(input("How many days have you had the book? "))
# grace_period = 7
# rate_per_day = 20
# late_days = days_kept - grace_period
# fine = late_days * rate_per_day
# if days_kept > grace_period:
#     value=fine
# else:
#     value="No fine. Thank you for returning it on time!"
# print(value)

# Q4
# A social media platform verifies popular users. Build a program that grants verification once followers exceed 10,000.
# followers = int(input("Enter your follower count: "))
# if followers > 10000:
#     print("Verification granted")
# else:
#     print("Verification denied. You need more than 10,000 followers.")