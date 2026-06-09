# person student facualty
class university:
    def __init__(self,university):
        self.university=university
    def details(self):
        print("university is ",self.university)
class course(university):
    def __init__(self,university,course):
        university.__init__(university)
        self.course=course
    def details(self):
        print(f"i did {self.course} from {self.university} ")
class branch(university):
    def __init__(self,university,branch):
        university.__init__(university)
        self.branch=branch
        print(branch)
class student(course,branch):
    def __init__(self,course,branch,university,name):
        super().__init__(course,branch)
        course.__init__(self,self.course,self.university)
        branch.__init__(self,self.branch,self.university)
        self.name=name
        print(name)

class facualty(branch):
    def __init__(self, branch, university, name):
        super().__init__(branch)
        branch.__init__(self, branch,university)
        self.name = name
        print(name)


facualty("CSE","SRM","Srinivas\n")
student("EAMCET","CSE","SRM","Prasanth")

# class University:
#     def _init_(self, university_name):
#         self.university = university_name
#         print(university_name)
# class Course(University):
#     def _init_(self, course_name, university_name):
#         super()._init_(university_name)  # Use super() for cleaner inheritance
#         self.course = course_name
#         print(course_name)
# class Branch(University):
#     def _init_(self, branch_name, university_name):
#         super()._init_(university_name)  # Use super() for cleaner inheritance
#         self.branch = branch_name
#         print(branch_name)
# class Student(Course, Branch):
#     def _init_(self, course_name, branch_name, university_name, name):
#         Course._init_(self, course_name, university_name)
#         Branch._init_(self, branch_name, university_name)
#         self.name = name
#         print(name)
#
# class Faculty(Branch):
#     def _init_(self, branch_name, university_name, name):
#         Branch._init_(self, branch_name, university_name)
#         self.name = name
#         print(name)
#
# # Faculty("CSE", "SRM", "Srinivas")
# Student("EAMCET", "CSE", "SRM","Prasanth")