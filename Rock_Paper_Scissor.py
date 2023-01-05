# Rock-paper-scissor


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

game_image=[rock,paper,scissors]
#rock = "0"
#paper = "1"
#scissors = "2"
user = int(input(print("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n")))
computer = int(random.randint(0,2))
if user >2 or user < 0:
 print("you typed invalid number ,you lose!")
else:
  print(game_image[user])

     
  print("Computer chose:")
  print(game_image[computer])
  if user==0 and computer == 2:
    print("you win!")
  elif computer ==0 and user  == 2:
    print("you lose")
  elif computer>user:
    print("you lose")
  elif user> computer:
    print("you win!")
  elif computer == user:
    print("it's draw")
