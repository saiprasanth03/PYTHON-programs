import math

def area(a,b):
    Area=a*b
    cans = math.ceil(Area / 7)
    print(f"To paint {Area} sq meters of wall {cans} cans are required")
h=int(input("Enter height: "))
w=int(input("Enter width: "))
area(h, w)
