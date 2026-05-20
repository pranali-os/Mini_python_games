print("Welcome to the tip calculator!")

bill = input("what was the total bill ?")
total_bill = float(bill)
print(total_bill)

tip = input("How much tip would you like to give? 10, 12 or 15?")
tip = int(tip)
print(type(tip))

tip_rupees = (tip/100)* total_bill
print(tip_rupees)

final_bill = total_bill + tip_rupees
print(final_bill)

head_count = input("How many people to split the bill")
head_count = int(head_count)

head_count_rupees = ((final_bill)/(head_count))
head_count_rupees = round(head_count_rupees, 3)
print(head_count_rupees)



print(f"Each person should pay: {head_count_rupees}")