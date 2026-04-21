days=('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
print(days[3])



print(days[0:4])

days=list(days)

days[4]='Friday'
days.append('Jan')

days=tuple(days)
print(days)