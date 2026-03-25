class student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

p1=student()
p1.change_school("xyz school")
print(student.school)