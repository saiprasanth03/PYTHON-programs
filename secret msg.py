from pyexpat.errors import messages
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plane_text,shift_key):
    cipher_text=""
    for char in plane_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the cipher text: {cipher_text}")
def decryption(cipher_text,shift_key):
    plane_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plane_text+=alphabet[new_position]
        else:
            plane_text+=char
    print(f"Here is the plane text: {plane_text}")

wanna_end = True
while  wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")

    if what_to_do == "encrypt":
        msg = input("Enter the message:\n").lower()
        shift = int(input("Enter the shift of the message:\n"))
        encryption(plane_text=msg,shift_key=shift)
    elif what_to_do == 'decrypt':
        msg = input("Enter the message:\n").lower()
        shift = int(input("Enter the shift of the message:\n"))
        decryption(cipher_text=msg,shift_key=shift)
    else:
        print("please enter correctly")
    play_again = input("Do you want to play again? (yes/no)\n")
    if play_again == "no":
        wanna_end = False
print("Have a nice day! Bye...")





























#
# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# def encrypt(plane_msg,shift):
#     cipher_text=""
#     for char in plane_msg:
#         if char in alphabet:
#             position=alphabet.index(char)
#             new_pos=(position+shift)%26
#             cipher_text+=alphabet[new_pos]
#         else:
#             cipher_text+=char
#     print(f"Your cipher text is {cipher_text}")
#
# def decrypt(cipher_msg,shift):
#     plane_text=""
#     for char in cipher_msg:
#         if char in alphabet:
#             position=alphabet.index(char)
#             new_pos=(position-shift)%26
#             plane_text+=alphabet[new_pos]
#         else:
#             plane_text+=char
#     print(f"Your plane text is {plane_text}")
# to_contionue=True
# while(to_contionue):
#     what_to_do=input(f"Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()
#     if what_to_do=="encrypt":
#         msg=input("Enter msg to encrypt: ")
#         shift=int(input("Enter shift value: "))
#         encrypt(plane_msg="msg",shift=shift)
#     elif what_to_do=="decrypt":
#         msg = input("Enter msg to decrypt: ")
#         shift = int(input("Enter shift value: "))
#         decrypt(cipher_msg="msg", shift=shift)
#     else:
#         print("Enter your choice correctly")
#     play_agian=input("Do you want to play again(y/n)").lower()
#     if play_agian=="n":
#         to_contionue = False
# print("Good bye!....")
#






