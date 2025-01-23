year = int(input("Enter the desired year here: "))

if (year % 4 == 0) and (year % 400 == 0) and (year % 100 == 0):
  print(f"So the year {year} is leap year")
else:
  print(f"So the year {year} is not leap year")

print("Welcome to Python Pizza Deliveries!!")
print("Small Pizza(S),Medium Pizza(M) and Large Pizza(L) price is $15,$20 and $25")
size = input("What size do you want? S,M or L ")

extra_cess = input("Do you want to extra chees Y or N> ")

if size.upper() == 'S':
  bill = 15
  print("Pepperoni for Small Pizza: +$2")
  add_pepparoni = input("Do you want pepperoni> Y or N> ")
  if(add_pepparoni == 'Y'):
    totalBill = bill + 2
    print(f"Your final bill is: ${totalBill}")
  else:
    print(f"Your final bill is: ${bill}")
    
    
elif size.upper() == 'M':
  bill = 20
  print("Pepparoni for Medium and Large Pizza: +$3")
  add_pepparoni = input("Do you want pepperoni> Y or N> ")
  if(add_pepparoni == 'Y'):
    totalBill = bill + 3
    print(f"Your final bill is: ${totalBill}")
  else:
    print(f"Your final bill is: ${bill}")
    
    
    
elif size.upper() == 'L':
  bill = 25
  print("Pepparoni for Medium and Large Pizza: +$3")
  add_pepparoni = input("Do you want pepperoni> Y or N> ")
  if(add_pepparoni == 'Y'):
    totalBill = bill + 3
    print(f"Your final bill is: ${totalBill}")
  else:
    print(f"Your final bill is: ${bill}")

else:
  print("Paglami Koro,Tikvabe value de")
    
    

print('Welcome to Treasure Island')
print('Your mission is find the Treasure')
choice1 = input("Right or left").lower()

if choice1 == 'left':
  choice2 = input("Wait or swim").lower()
  if choice2 == 'wait':
    choice3 = input("Red,Blue or Yellow").lower()
    if choice3 == "yellow":
      print("your are won the game!!! congrats")
    else:
      print("gameover")
  else:
    print("gameover")
else:
  print("gameover")