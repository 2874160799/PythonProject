class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {'语文':'0','数学':'0','英语':'0'}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生：{self.name}(学号：{self.id})的成绩是")
        for course in self.grades:
            print(f"{course}{self.grades[course]}")

zeng = Student("张三","001")
zeng.set_grade("语文",90)
zeng.set_grade("数学",92)
zeng.print_grades()