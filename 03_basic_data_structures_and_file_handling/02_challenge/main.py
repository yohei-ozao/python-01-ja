import math
import random

#User choice
hand_type = ("rock", "scissors", "paper")
input_string = int(input("Select your hand by 0/1/2 (0=rock, 1=scissors, 2=paper) :"))
print(hand_type[int(input_string)])

x = random.random() * 3
#print(hand_type[math.floor(x)])
computer_choice = math.floor(x)

if ((input_string == 0 and computer_choice == 1) 
    or (input_string == 1 and computer_choice == 2)
    or (input_string == 2 and computer_choice == 0)
    ) :
    print("You win!")
elif input_string == computer_choice:
    print("It is a draw")
elif ((input_string == 0 and computer_choice == 2) 
      or (input_string == 1 and computer_choice == 0) 
      or (input_string == 2 and computer_choice == 1)
      ):
    print("Computer win")