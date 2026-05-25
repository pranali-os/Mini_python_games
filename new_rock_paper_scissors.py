rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
#random_elements = [rock, paper,scissors]
random_elements = random.randint(0,2)
print(random_elements)

elements = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors")
elements = (int(elements))
#print(type(elements))

if elements == 0:
    print("Your move:",rock)
if random_elements == 0:
    print("Computer move:",rock)

if elements == 1:
    print("Your move",paper)
if random_elements == 1:
    print("Computer move",paper)

if elements == 2:
    print("Your move", scissors)
if random_elements == 2:
    print("Computer move:",scissors)

if elements == random_elements:
    print("This is Tie")
if elements == 0 and random_elements == 1:
    print("Computer lost, you win.")
if elements == 1 and random_elements == 0:
    print("You lost, computer win.")

if elements == 0 and random_elements == 2:
    print("you win, computer lost.")
if elements == 2 and random_elements == 0:
    print("computer win, you lost.") 

if elements == 2 and random_elements == 1:
    print("You win, computer lost.")  
if elements == 1 and random_elements == 2:
    print("Computer win, you lost.")
                    
