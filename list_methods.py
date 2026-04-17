my_list=['Mike','mary','Junior',100,200,True,False]

my_list.remove(100)
print(my_list)

my_list.pop(0)
print(my_list)

my_list.append('Hope')
print(my_list)

my_list.insert(1,'Philip')
my_list.insert(5,1000)
print(my_list)

list=[10,20,30,['Mary','Kim',[1000,2000,3000]],40,50,60]
list.append(70)
list[3].insert(1,'Jane')
list[3][3].insert(1,1500)
list[3][3].remove(2000)
print(list)

list2=['Mike','Mary','Junior']
print(list2.count('Mike'))

list3=[23,55,23,234]
list3.sort(reverse=True)
print(list3)

list2.extend(list3)
print(list2)

list2.clear()
print(list2)
