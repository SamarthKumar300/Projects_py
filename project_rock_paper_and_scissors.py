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

user_choice= input("What fo you want to choose? rock,paper or scissors ");

choices=["rock","paper","scissors"]

if user_choice == choices[0]:
    print(rock);
elif user_choice == choices[1]:
    print(paper);
elif user_choice == choices[2]:
    print(scissors);

import random
from secrets import choice;

num_random=random.randint(1,3) ;

computer_choice=choices[num_random - 1];

if computer_choice == choices[0]:
    print(rock);
elif computer_choice == choices[1]:
    print(paper);
elif computer_choice == choices[2]:
    print(scissors);

if user_choice=="rock"  and computer_choice == "paper":
    print(f"You lost");

elif user_choice == 'paper' and computer_choice == 'scissors':
    print("You lost");

elif user_choice == 'scissors' and computer_choice == 'rock':
    print("You lost");

elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win");

elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win");

elif user_choice == 'scissors'  and computer_choice == 'paper':
    print("You win ");

elif user_choice == 'scissors'  and computer_choice == 'scissors':
    print("Draw");

elif user_choice == 'rock'  and computer_choice == 'rock':
    print("Draw ");

elif user_choice == 'paper'  and computer_choice == 'paper':
    print("Draw ");
