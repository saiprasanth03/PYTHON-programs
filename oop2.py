class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            print("True")
        else:
            print("False")
p1=person("prasanth",14)
p2=person("guna",16)
