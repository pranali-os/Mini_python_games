print("Welcome to the Python pizza deliveries !")

pizza_size = (input("What size of pizza you want small(s), medium(m), large(l)"))

pepperoni = (input("Do you want pepporoni on your pizza, Y or N ?"))

cheese = (input("Do you want an extra cheese, Y or N ?"))

#small = 15
#medium = 20
#large = 25

#pepperoni = 2 , 3
#extra_cheese = 1

#pepperoni_small = 15 

bill = 0

if pizza_size in ["small" , "s"] :
    bill = 15
    #print(f"Your pizza price is ${small}")
    if pepperoni == "Y":
       bill += 2 
    if cheese ==  "Y":  
      bill +=1          
    print(f"Your final bill is ${bill}")

elif pizza_size in ["medium" , "m"]:
    bill = 20
    if pepperoni == "Y":
       bill += 3
    if cheese ==  "Y":  
      bill +=1          
    print(f"Your final bill is ${bill}")
    #print(f"Your pizza price is ${medium}")

elif pizza_size in ["large" , "l"] :
    bill = 25
    if pepperoni == "Y":
       bill += 3
    if cheese ==  "Y":  
      bill +=1          
    print(f"Your final bill is ${bill}")
    #print(f"Your pizza price is ${medium
    #print(f"Your pizza price is ${large}")



    




