'''num= (int(input("Enter any number to check if its odd or even: \n")))

if num % 2 == 0:
    print("The number you've entered is even.")
else:
    print("The number you've entered is odd.")  '''

'''weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

bmi = (int(bmi))
print(bmi)

if bmi < 18.5 :
   print("underweight")
elif bmi < 25:
   print("normal weight")
else:
    print("overweight") 
'''

height = input("what's your height ? ")
height = int(height)


if height >= 120  :
   print("you can ride the rollercoaster")

   bill = 0 
   age = input("What's your current age? ")
   age = int (age)

   if age <= 12:
    bill = 5
    print("Please pay your bill $5.")
   elif age <= 18:
    bill = 7
    print("Please pay your bill $7.")
   elif age > 18 and age < 45:
    bill = 12
    print("Please pay your bill $12.")
   elif age > 45 and age < 55:
    bill = 0
    print("You won't have to pay any penny.")    

   photo = input("Do you want to be photo taken? Type Y to take else N.")
   
   if photo == 'Y' :
     bill += 3
     print(f"Here's your final bill: ${bill}")
   else:
     print(f"Your final bill is: ${bill}")
      
   
         

else:
   print("Come back later. Happy to have you :) ")  


   
