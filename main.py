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

your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

import random
computer_choice=random.randint(0,2)

if your_choice>=3 or your_choice<=0:
  print("You typed an invalid number, you lose")
elif your_choice==0 and computer_choice==0: 
  print(f"{rock}\nComputer chose:\n{rock}\nDraw")
elif your_choice==1 and computer_choice==1:
  print(f"{paper}\nComputer chose:\n{paper}\nDraw")
elif your_choice==2 and computer_choice==2:
  print(f"{scissors}\nComputer chose:\n{scissors}\nDraw")

if your_choice==0 and computer_choice==1:
  print(f"{rock}\nComputer chose:\n{paper}\nYou lose")
elif your_choice==0 and computer_choice==2:
  print(f"{rock}\nComputer chose:\n{scissors}\nYou win")

if your_choice==1 and computer_choice==0:
  print(f"{paper}\nComputer chose:\n{rock}\nYou win")
elif your_choice==1 and computer_choice==2:
  print(f"{paper}\nComputer chose:\n{scissors}\nYou lose")

if your_choice==2 and computer_choice==0:
  print(f"{scissors}\nComputer chose:\n{rock}\nYou lose")
elif your_choice==2 and computer_choice==1:
  print(f"{scissors}\nComputer chose:\n{paper}\nYou win")

