"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1. 添加学生成绩**：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
        1.3 验证成绩范围（0-100 分）
        1.4 创建学生对象并添加到系统
    2. 修改学生成绩**：根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生，显示该生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3. 删除学生成绩**：根据输入的学生姓名，删除对应的学生成绩
    4. 查询指定学生成绩**：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式为："姓名：张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"
    5. 展示全部学生成绩**：展示出系统中所有学生的成绩
"""
#学生类
class Students:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    #打印学生成绩
    def __str__(self):
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语{self.english}|总分：{self.chinese+self.math+self.english}"
   #修改学生成绩
    def update(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
#教务系统类
class StudentSystem:
    version = 1.0
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = []
        # 1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        # 1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
        # 1.3 验证成绩范围（0-100 分）
        # 1.4 创建学生对象并添加到系统
    def add_student(self):
        name =  input("请输入学生的姓名：")
        #判断学生姓名是否存在，如果存在就无法添加
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，请重新输入")
                return
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        # 判断分数是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Students(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生的各科成绩必须在0~100之间！")
    #修改学生成绩
    # 2.1输入要修改的学生姓名
    # 2.2根据姓名查找该学生，显示该生当前成绩信息
    # 2.3输入新的语文、数学、英语成绩
    # 2.4更新学生成绩数据
    def update_student(self):
        name = input("请输入要修改的学生：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
            chinese = int(input("请输入修改后的语文成绩："))
            math = int(input("请输入修改后的数学成绩："))
            english = int(input("请输入修改后的英语成绩："))
            # 判断分数是否在0-100之间
            if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                s.update_list(chinese,math,english)
                print("学生成绩修改成功")
                print(f"当前成绩：{s}")
                return
            else:
                print("学生的各科成绩必须在0~100之间！")
                return
        print("未找到该学生，修改失败")
    #3.删除学生成绩 ：根据输入的学生姓名，删除对应的学生成绩
    def delete_student(self):
        name = input("请输入要修改的学生：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
    # 4.查询指定学生成绩 ：根据输入的学生姓名，查找对应的学生成绩，并输出
    # 4.1输出格式为："姓名：张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"
    def search_student(self):
        name = input("请输入要查询的学生：")
        for s in self.student_list:
            if s.name == name:
                print(f"{s}")
                return
        print("未查询到该学生，请重新输入")
    #5.展示全部学生成绩 ：展示出系统中所有学生的成绩
    def show_student(self):
        for s in self.student_list:
            print(f"{s}")
    #运行系统
    def run(self):
        print(f"欢迎使用教务系统V{StudentSystem.version}")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询全部学生 6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print()
            choice = input("请输入操作指令(1-6):")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.search_student()
                case "5":
                    self.show_student()
                case "6":
                    print("Bye~")
                    break
                case _:
                    print("输入错误，请输入1-6之间的数字")
if __name__ == "__main__":
    studentsystem =StudentSystem()
    studentsystem.run()