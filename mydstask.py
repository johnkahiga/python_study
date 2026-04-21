my_ds=[23,'Jane',(560),['Lesson','Maths',{'currency':'KES'}],987,(76,'John')]
my_ds1=my_ds[3][2]
print(my_ds1['currency'])

print(my_ds[2])

print(my_ds[3][1])

my_ds[3][2]['amount']=90
print(my_ds)

my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)

my_ds[5]=list(my_ds[5])
my_ds[5][1]='Jane'
my_ds[5]=tuple(my_ds[5])
print(my_ds)
print(my_ds)



