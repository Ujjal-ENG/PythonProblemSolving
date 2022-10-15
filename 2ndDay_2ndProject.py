#Greetings

print("Welcome to the tip calculator")

#Ask the total bill to the customer

totalBill = float(input("Give the total bill: $"))

splitBill = int(input("How many People goes to be the bill: "))

tips = int(input("What was the tip you provide: "))


tipAsPerson = tips/100
totalTipAmount = tipAsPerson * totalBill
totalBillPayPerson = totalBill + totalTipAmount
eachPersonPay = totalBillPayPerson/splitBill
finalAmount = round(eachPersonPay,2)
print(f"Each person should be pay: ${finalAmount}")