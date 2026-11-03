#基于面向对象的编程思想完成如下系统开发
#某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和 VIP 会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
#核心功能
# 1. **会员登录**：会员通过卡号和密码登录系统
# 2. **借书**：会员可以借阅库存中有余量的图书
# 3. **还书**：会员可以归还借阅的图书
# 4. **查看我的借阅**：展示当前会员已经借阅的图书列表
# 5. **退出系统**
#借阅规则
# 1. 普通会员最多可借 **3** 本
# 2. VIP 会员最多可借 **6 + VIP 等级** 本（VIP 等级，默认为 1）
#注意
# 1. 登录成功（卡号和密码均正确）后，才可以访问该系统
# 2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

from abc import ABC,abstractmethod
import json
#书籍类
class Book:
    def __init__(self,book_id,title,author,book_number):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.book_number = book_number
        self.__available_num = book_number
    def borrow_book(self):
        if self.__available_num >0:
            self.__available_num -= 1
            return True
        else:
            return False
    def return_book(self):
        self.__available_num +=1
        return True
    def get_book_number(self):
        return self.__available_num
#抽象类：一种只能被继承，不能被实例化的类，作用就是规定子类必须要实现哪些方式，强制子类必须遵守统一的代码规范
#Python中的抽象类，需要继承abc模块中的ABC类---->ABC：Abstract Base Class
#会员类
class Member(ABC):
    def __init__(self,card_number,name,password):
        self.card_number = card_number
        self.name = name
        self.__password = password
        self.__borrow_book = []
    def borrow_book(self,book:Book):  #借书
        if len(self.__borrow_book)>=self.get_book_max():
            print("借阅失败，超过借阅数量最大限制")
            return False
        if book.borrow_book():
            self.__borrow_book.append(book)
            print(f"{self.name}已成功借阅书籍{book.title}")
            return True
        else:
            print(f"借阅失败，{book.title}已被借完")
            return False
    def return_book(self,book:Book):
        if book in self.__borrow_book:
            book.return_book()
            self.__borrow_book.remove(book)
            print(f'{self.name}已成功归还书籍{book.title}')
        else:
            print(f"归还失败，您没有借阅该书籍{book.title}")
    def get_password(self):
        return self.__password
    def get_borrow_book(self):
        return self.__borrow_book
    #获取用户所能借的书的数量（需要在子类实现）
    @abstractmethod
    def get_book_max(self):
        pass
#普通会员
class NorMember(Member):
    def get_book_max(self):
        return 3
#vip会员
class VipMember(Member):
    def __init__(self,card_number,name,password,vip_level):
        self.vip_level = vip_level
        super().__init__(card_number,name,password)
    def get_book_max(self):
        return 6 + self.vip_level
#图书管理系统
class LibrarySystem:
    def __init__(self):
        self.books={}   #--->{key:value,图书编号：图书名字}
        self.members={}    #--->{会员卡号：会员名字}
        self.current_member:Member|None=None
        #加载数据（书籍，会员）
        self.load_books_data()
        self.load_members_data()
    def load_books_data(self):
        #加载data/books.json中的数据
        with open('data/books.json','r',encoding="utf-8")as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["编号"]]=Book(book["编号"],book["标题"],book["作者"],book["数量"])
            print("书籍数据加载成功")

    def load_members_data(self):
        with open('data/members.json','r',encoding="utf-8")as f:
            members_data = json.load(f)
            for member in members_data:
                if member ["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NorMember(member["卡号"],member["姓名"],member["密码"])
                elif member ["卡号"].startswith("V"):
                    self.members[member["卡号"]] = VipMember(member["卡号"], member["姓名"], member["密码"],member["会员等级"])
            print("加载会员信息成功")
    def login(self):
        while True:
            print("[登录]")
            member_id=input("请输入卡号：").strip()
            password=input("请输入密码：")
            #判断卡号是否存在
            if member_id not in self.members.keys():
                print("卡号不存在，请重新输入")
                continue
            #判断密码是否正确
            member=self.members[member_id]
            if member.get_password() == password:
                print(f"登陆成功,欢迎您{member.name}")
                #记录当前登录信息
                self.current_member=member
                return True
            else:
                print("密码错误，请重新输入")
                continue
    def borrow_book(self):#借阅图书
        #1.展示图书列表
        for book in self.books.values():
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}，总数{book.book_number}，可借阅数：{book.get_book_number()}")
        #2.获取要借阅的图书编号
        book_id = input("请输入要借阅的图书编号：")
        if book_id not in self.books.keys():
            print("借阅失败，图书编号不存在")
            return
        self.current_member.borrow_book(self.books[book_id])
    #归还图书
    def return_book(self):
        borrowed_book=self.current_member.get_borrow_book()
        print("已经借阅的图书为")
        for book in borrowed_book:
            print(f"编号：{book.book_id}，标题：{book.title}")
        book_id=input("请输入要归还的图书编号：")
        if book_id not in self.books.keys():
            print("还书失败，该图书编号不存在")
            return
        self.current_member.return_book(self.books[book_id])
    #查看借阅
    def show_borrow_book(self):
        borrowed_books = self.current_member.get_borrow_book()
        if len(borrowed_books)>0:
            for book in borrowed_books:
                print(f"编号：{book.book_id},标题{book.title}")
        else:
            print("您还没有借阅任何图书")
    #运行系统
    def run(self):
        if self.login():
            while True:
                print("""
1.借阅图书
2.归还图书
3.查看借阅
4.退出系统""")
                choice = input("请选择操作(1~4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrow_book()
                    case "4":
                        print("感谢您的使用")
                        break
                    case _:
                        print("输入无效，请重新输入(1~4)")
if __name__ == "__main__":
    ls=LibrarySystem()
    ls.run()