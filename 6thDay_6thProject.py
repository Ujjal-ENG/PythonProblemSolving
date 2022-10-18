import random

wordList = ['ardvark','baboon','camel'];

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




