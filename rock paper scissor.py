#rock,paper,scissor
import random

user_in=input("Rock,Paper,Scissor:")
comp=random.randint(0,2)
comp1=int(comp)
if(comp1==0):
    comp_in="rock"
elif(comp1==1):
    comp_in="paper"
elif(comp1==2):
    comp_in="scissor"
print(f"you choosen {user_in} computer choosen {comp_in}")
if(user_in==comp_in):
    print("Match draw")
elif((user_in=="rock" and comp_in=="paper") or (user_in=="paper" and comp_in=="scissor") or (user_in=="scissor" and comp_in=="rock")):
    print("You lost the match")
elif((user_in=="paper" and comp_in=="rock") or (user_in=="rock" and comp_in=="scissor") or (user_in=="scissor" and comp_in=="paper")):
    print("You won the match")
else:
    print("pleasa enter valid input")