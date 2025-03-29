
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Student(Person):
    def __init__(self, firstname, lastname, dept):
        Person.__init__(self, firstname, lastname)
        # super().__init__(firstname, lastname)
        self.dept = dept

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.dept)

    def get_dept(self):
        return self.dept


s1 = Student('Manju', 'A', 'CS')
print(s1.firstname, s1.lastname, s1.dept)
print(s1)

print(s1.get_dept())

#

s2 = Student("Test", "B", "EC")
print(s2 is s1)

s3 = s2
print(s3 is s2)