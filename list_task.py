trainees=['John',[2,['James','Mary']]]
print(trainees[1][0])
print(trainees[1][1][0])

trainees.append(56)
print(trainees)

trainees[1][1].insert(1,'Mike')
print(trainees)

trainees[1][0]=8
print(trainees)

trainees.remove('John')
trainees[0][1].remove('Mary')
print(trainees)

print(len(trainees))
