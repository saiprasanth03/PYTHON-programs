import high_low_data
import high_low_logo
import random
import os
print(high_low_logo.logo)
print("\n")
score=0
def profile_info(account):
    name=account["name"],
    description=account["description"],
    country=account["country"],
    return f"{name}, a {description}, from{country}"
def followers_count(follow_count_1,follow_count_2,guess):
    if follow_count_1 > follow_count_2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False

choice2=random.choice(high_low_data.data)
to_continue=True
while to_continue:
    choice1=choice2
    choice2 = random.choice(high_low_data.data)
    while choice1==choice2:
        choice2 = random.choice(high_low_data.data)
    follow_count_1=choice1["followers"]
    follow_count_2=choice2["followers"]
    print(f"choice 1: {profile_info(choice1)}")
    print(high_low_logo.vs)
    print(f"choice 2: {profile_info(choice2)}")
    guess=int(input("Who has the more followers? (1 or 2)"))
    result=followers_count(follow_count_1,follow_count_2,guess)
    os.system('cls')
    if result == True:
        score= score + 1

        print(f"you are right and score is:{score}")
    else:
        print(f"you are wrong, your final score is {score}")
        to_continue = False