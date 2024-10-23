class Person:
    def __init__(self,name):
        print(id(self)," was ready")
        self.name=name
    
    def greet(self):
        print(f"Hello Im {self.name}")
    
class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id=student_id
    def greet(self):
        print(f"Hello, my name is {self.name} and my student ID is {self.student_id}")
    
student1 = Student("Alice","12345")    
student1.greet()    