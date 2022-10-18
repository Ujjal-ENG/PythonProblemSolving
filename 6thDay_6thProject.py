import random

wordList = ['ardvark','baboon'];

chosenWord = random.choice(wordList)
print(f"Here the randomly choosen word: {chosenWord}")

display = []

wordLength = len(chosenWord)
for _ in range(len(chosenWord)):
  display += '_'
print(display)

endOfTheGame = False

while not endOfTheGame:
  
  guess = input("Put a one variable: ").lower()
  for position in range(len(chosenWord)):
    letter  = chosenWord[position]
    if letter == guess:
      display[position] = letter
  print(display)
  
  if "_" not in display:
    endOfTheGame = True
    print("You Win")
# sum = 0
# factor = 1
# for i in range(0,6):
  
#   if i < 2:
#     factor = 1
#   else:
#     factor = factor * i
  
#   sum = sum + factor
    
#   print(sum)