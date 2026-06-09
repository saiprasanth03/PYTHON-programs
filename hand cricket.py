import random
start=True
done=True
first_your_batting=False
first_computer_batting=False
your_chosen=input("Enter even or odd: ").lower()
your_num=0
if your_chosen=="even" or your_chosen=="odd":
    your_num=int(input("Enter a number(1 - 6) for toss: "))
else:
    start=False
    done=False
    print("Retry and enter correctly")
your_final_score=0
comp_final_score=0
target_score=0
second_innings_score=0

entered_correctly=True
while start:
    comp_num= random.randint(0,6)
    you_done=""
    comp_done=""
    entered_correctly=True
    total_sum=your_num+comp_num
    if total_sum%2==0 and your_chosen=="even":
        print(f"your number is {your_num} and computer number is {comp_num}")
        print(f"sum is {total_sum} which is even number")
        bat_or_bowl=input("Choose batting or bowling:\n").lower()
        if bat_or_bowl=="batting":
            you_done="batting"
        elif bat_or_bowl=="bowling":
            you_done="bowling"
        else:
            start=False
            done=False

    elif total_sum%2!=0 and your_chosen=="odd":
        print(f"your number is {your_num} and computer number is {comp_num}")
        print(f"sum is {total_sum} which is odd number")
        bat_or_bowl = input("Choose batting or bowling:\n").lower()
        if bat_or_bowl == "batting":
            you_done = "batting"
        elif bat_or_bowl == "bowling":
            you_done = "bowling"
        else:
            start=False
            done=False

    elif total_sum%2!=0 and your_chosen=="even":
        print(f"your number is {your_num} and computer number is {comp_num}")
        print(f"sum is {total_sum} which is odd number")
        comp_chosen=random.randint(1,2)
        if comp_chosen==1:
            comp_done="batting"
            print(f"you lost the toss and computer chosen {comp_done}")
        else:
            comp_done="bowling"
            print(f"you lost the toss and computer chosen {comp_done}")

    elif total_sum%2==0 and your_chosen=="odd":
        print(f"your number is {your_num} and computer number is {comp_num}")
        print(f"sum is {total_sum} which is even number")
        comp_chosen = random.randint(1, 2)
        if comp_chosen == 1:
            comp_done = "batting"
            print(f"you lost the toss and computer chosen {comp_done}")
        else:
            comp_done = "bowling"
            print(f"you lost the toss and computer chosen {comp_done}")
    else:
        entered_correctly=False
        start = True
        done = False

    if (you_done=="batting" or comp_done=="bowling") and entered_correctly==True and start==True:
        first_your_batting = True
        first_innings_sum=0
        print("****************** first innings starts ******************")
        print("Now you are batting")
        not_out=True
        while not_out:
            first_batting=int(input("Enter a number(1 - 6): "))
            first_bowling=random.randint(1,6)
            if first_batting!=first_bowling:
                first_innings_sum += first_batting
                print(f"you entered {first_batting} and computer entered {first_bowling}")
                print(f"your score is {first_innings_sum}")
            else:
                print(f"You entered {first_batting} and computer entered {first_bowling} so you are out")
                print(f"your final score is {first_innings_sum}")
                not_out=False
        target_score=first_innings_sum+1
        your_final_score=first_innings_sum

        is_comp_not_out=True
        while is_comp_not_out:
            second_innings_sum=0
            print("****************** second innings starts ******************")
            print(f"Now you are bowling and computer is batting")
            print(f"computer's target is {target_score}")
            not_out = True
            while not_out:
                second_batting=random.randint(1,6)
                second_bowling = int(input("Enter a number(1 - 6): "))
                if second_batting!=second_bowling:
                    second_innings_sum += second_batting
                    print(f"you entered {second_bowling} and computer entered {second_batting}")
                    print(f"computer score is {second_innings_sum}")
                    if second_innings_sum >= target_score:
                        is_comp_not_out = False
                        not_out = False
                        start = False
                        done = True
                else:
                    print(f"You entered {second_batting} and computer entered {second_bowling} so computer is out")
                    print(f"Computer score is {second_innings_sum}")
                    is_comp_not_out=False
                    not_out = False
                    start = False
                    done = True
                comp_scored=second_innings_sum
                second_innings_score=second_innings_sum
                comp_final_score=second_innings_sum

    elif (you_done=="bowling" or comp_done=="batting") and entered_correctly==True and start==True:
        first_computer_batting = True
        first_innings_sum = 0
        print("****************** first innings starts ******************")
        print("Now you are bowling")
        not_out = True
        while not_out:
            first_bowling = int(input("Enter a number(1 - 6): "))
            first_batting = random.randint(1, 6)
            if first_batting != first_bowling:
                first_innings_sum += first_batting
                print(f"you entered {first_bowling} and computer entered {first_batting}")
                print(f"computer score is {first_innings_sum}")
            else:
                print(f"You entered {first_bowling} and computer entered {first_batting} so computer is out")
                print(f"computer final score is {first_innings_sum}")
                not_out = False
        target_score = first_innings_sum + 1
        comp_final_score = first_innings_sum
        is_comp_not_out = True
        while is_comp_not_out:
            second_innings_sum = 0
            print("****************** second innings starts ******************")
            print(f"Now you are batting and computer is bowling")
            print(f"yours target is {target_score}")
            not_out = True
            while not_out:
                second_bowling = random.randint(1, 6)
                second_batting = int(input("Enter a number(1 - 6): "))
                if second_batting != second_bowling:
                    second_innings_sum += second_batting
                    print(f"you entered {second_batting} and computer entered {second_bowling}")
                    print(f"your score is {second_innings_sum}")
                    if second_innings_sum >= target_score:
                        is_comp_not_out = False
                        not_out = False
                        start = False
                        done=True
                else:
                    print(f"You entered {second_batting} and computer entered {second_bowling} so computer is out")
                    print(f"your score is {second_innings_sum}")
                    is_comp_not_out = False
                    not_out = False
                    start = False
                    done = True
                comp_scored = second_innings_sum
                second_innings_score = second_innings_sum
                comp_final_score = second_innings_sum
    else:
        start = False
        print("Retry and enter your choice correctly.")

while done:
    if first_your_batting==True:
        if (your_final_score +1 > comp_final_score) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so you win the match")
            done=False
        elif (your_final_score +1 < comp_final_score) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so you lost the match")
            done = False
        elif (your_final_score ==comp_final_score) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so Draw match")
            done = False
    else:
        if (your_final_score  < comp_final_score +1) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so you win the match")
            done=False
        elif (your_final_score > comp_final_score+1) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so you lost the match")
            done = False
        elif (your_final_score ==comp_final_score) and entered_correctly==True:
            print(f"your score is {your_final_score} and computer score is {comp_final_score} so Draw match")
            done = False