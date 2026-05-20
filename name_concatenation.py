def couple_name_generator():
 print("Welcome to the couple name generator!")

 name1 = input("what's your name?\n")
 name2 = input("what's your spouse name?\n")

 #print(len(name1))
 #print(len(name2))

#name1 = name1.strip()
#name2 = name2.strip()

 '''if len(name1) < 3:
   print("Your name is too short" + name1)
 else:
  print("Names are: " + name1)'''

 first_three = name1[:3]

 last_three = name2[-3:]

 combined_name = last_three + first_three

 return combined_name

print(couple_name_generator())




