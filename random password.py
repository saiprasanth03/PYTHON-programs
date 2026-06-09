import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','+','<','>']
print("\n**********  RANDOM PASSWORD GENERATOR  **********\n")
n_letters=int(input("Enter number of letters you want in your password: "))
n_numbers=int(input("Enter number of numbers you want in your password: "))
n_symbols=int(input("Enter number of symbols you want in your password: "))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list.append(char)
for j in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list.append(char)
for k in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list.append(char)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password=""
for char in password_list:
    password +=  char
print("\nRANDOM PASSWORD IS",password)

