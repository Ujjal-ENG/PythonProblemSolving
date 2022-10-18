studentHeights = input("Input a list of student heights: ").split(',')

for n in range(0, len(studentHeights)):
  studentHeights[n] = int(studentHeights[n])

sum = 0
for item in studentHeights:
  sum += item

average = int(sum / len(studentHeights))
print(average)

