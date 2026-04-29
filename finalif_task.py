# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".
start_date = '2024-01-01'
end_date = '2024-12-31'
if start_date<end_date:
    val='Valid Period'
elif start_date>end_date:
    val='Invalid period'
else:
    val='One day period'
print(val)

# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
str1=input('Enter string one')
str2=input('Enter string 2')
length1=len(str1)
length2=len(str2)
if length1>length2:
    le='str1 is longer'
elif length2>length1:
    le= 'str2 is longer'
else:
    le='Both have equal length'
print(le)

# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids=[101,102,103]
user_id=105
if user_id in valid_ids:
    print('Access Granted')
else:
    print('Access Denied')

# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
var='But'
var1=type(var)
if var1==str:
    print('String Detected')
elif var1==int:
    print('integer Detected')
else:
    print('Unknown Type')

# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.
x=7
y=14
if y%2==0:
    if x%2==0:
        print('x and y are both even numbers')
    else:
        print('only y is even')
else:
    if x%2==0:
        print('only x is even')
    else:
        print('Neither x nor y are even')