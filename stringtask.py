name="   JOHn ."
name=name.strip(' .').lower()
print(name)

sentence1="The Dog Breed is German Shepherd"
print(sentence1[8:-9])

sentence2="Defeats for the Clinton forces, this was her moment fo triumph"
print(sentence2[16:-32])

sentence3="The lazy dog; ran so fast; it hit the wall"
split=sentence3.split(';')
print(len(split))

first_name="Joh.n"
first_name=first_name.strip().replace('.','')
last_name=" Do,e"
last_name=last_name.strip().replace(',','')
full_name=first_name+" "+last_name
print(full_name)

r = '["E","W","C"]' 
r=r.replace('[','').replace(']','').replace(',','').replace('"','')
print(r)