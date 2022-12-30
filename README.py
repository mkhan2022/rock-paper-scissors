# rock-paper-scissors
#VERSION 1
import random
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

choices = [rock, paper, scissors]
user_choice = int(input("Choose rock(0), paper(1) or scissors(2)"))
if user_choice == 0:
    print(choices[0])
    computer_choice = random.randint(0,2)
    if computer_choice == 0: 
        print(choices[0])
        print("Draw")
    elif computer_choice == 1: 
        print (choices[1])
        print("You lose")
    else: 
        print(choices[2])
        print("You Win!")
elif user_choice == 1: 
    print(choices[1])
    computer_choice = random.randint(0,2)
    if computer_choice == 0: 
        print(choices[0])
        print("You win!")
    elif computer_choice == 1: 
        print (choices[1])
        print("Draw")
    else: 
        print(choices[2])
        print("You Lose!")
else: 
    print(choices[2])
    computer_choice = random.randint(0,2)
    if computer_choice == 0: 
        print(choices[0])
        print("You Lose!")
    elif computer_choice == 1: 
        print (choices[1])
        print("You win!")
    else: 
        print(choices[2])
        print("Draw")

  #or... VERSION 2
import random
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
game_images= [rock, paper, scissors]
user_choice = int(input("Choose rock(0), paper(1) or scissors(2)"))
computer_choice = random.randint(0,2)
print("computer chose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0: 
  print("you typed an invalid numebr, you lose.")
elif computer_choice == 0 and user_choice ==2:
  print("you lose!")
elif user_choice == 0 and computer_choice == 2: 
  print("You win!")
elif computer_choice> user_choice: 
  print("you lose!")
elif user_choice > computer_choice: 
  print("You win!")
elif computer_choice == user_choice:
  print("it is a draw!")
