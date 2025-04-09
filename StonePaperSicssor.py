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
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
if player_choice == "0":
    player = rock
elif player_choice == "1":
    player = paper
else:
    player = scissors

choices = [rock, paper, scissors]
computer = random.choice(choices)

print(player)
print(computer)

if player == rock and computer == paper:
    print('You loose')
elif player == rock and computer == scissors:
    print('You win')
elif player == paper and computer == rock:
    print('You win')
elif player == paper and computer == scissors:
    print('You loose')
elif player == scissors and computer == rock:
    print('You loose')
elif player == scissors and computer == paper:
    print('You win')
else:
    print('draw')
