text="software developer"
text1=text.capitalize()
print(text1)
text2=text.casefold()
print(text2)

text3=text.endswith('R')
print(text3)
text4=text.startswith('S')
print(text4)
#lower
text5=text.lower()
print(text5)
#upper
text6=text.upper()
print(text6)

# strip used to remove leading and trailing whitespace
text = "     Software Developer"
print(len(text))
print(text)
text=text.strip()
print(len(text))
print(text)

#split
email="JohnKahiga27@gmail.com"
splitted=email.split('@')
print(splitted)

text9=text.split()
print(text9)

text="       jUnIoR deVelOper  "
text10=text.strip().capitalize()
print(text10)