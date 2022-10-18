# 

# studentNumber = input("Enter the numbers of class test of the students: ").split(',')

# for number in range(0, len(studentNumber)):
#   studentNumber[number] = int(studentNumber[number])

# max = 0
# for eachNumber in studentNumber:
#   result = max(eachNumber)
# print(max)

for number in range(1,16):
  if number % 3 ==0:
    print('Fizz')
  elif number % 5 ==0:
    print('Buzz')
  elif number % 3 == 0 and number % 5 == 0 :
    print('FizzBuzz')
  else:
    print(number)


