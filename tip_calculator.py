#just printing a welcome to the user
print("Welcome To Leo's Bill Tip/Split Calculator")
#just a line break from the welcome message
print("\n")
#Asking the user to enter the amount on the bill by making a variable and making sure the input will be a float
total_bill = float(input("What is the total bill?:$ "))
#Asking the user for the % tip they'd like to leave
percentage_tip = int(input("What % tip would you like to give? Don't be cheap now!: "))
#Asking the user for the # of people splitting the bill
number_of_people = int(input("How many people are splitting the bill?: "))
#added a line break to seperate the input and output for a nice cosmetic look
print("\n")
#Calculate what each person owes based on the bill and tips the user entered
#%.2f ensures that its 2 decimal places after when rounded which i had to google to fix because i was getting values printed out as 132.2 instead of 132.20
payment_per_person = ("%.2f" % round(float(((percentage_tip / 100 +1) * total_bill) / number_of_people), 2))
#Print the $ amount of the tip
tip_amount = "%.2f" % float(percentage_tip / 100 * total_bill)
print(f"Tip amount: ${tip_amount}")
#convert total bill and tip amount to floats so they can be added
total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Your bill including tip is: ${tip_and_total}")
#Print what each person needs to pay
print(f"Each person owes: ${payment_per_person} No, your buddy did not forget his wallet so make sure he pays up!")