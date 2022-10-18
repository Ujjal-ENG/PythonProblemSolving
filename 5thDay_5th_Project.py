# 

studentNumber = input("Enter the numbers of class test of the students: ").split(',')

for number in range(0, len(studentNumber)):
  studentNumber[number] = int(studentNumber[number])

max = 0
for eachNumber in studentNumber:
  if max < eachNumber:
    max = eachNumber
print(max)

