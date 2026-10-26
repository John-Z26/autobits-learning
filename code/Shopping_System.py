# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5. 退出购物
#商品类
class Goods:
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount
    #打印商品信息
    def __str__(self):
        return f"商品名称：{self.name},商品价格：{self.price},商品数量：{self.amount}"
    #修改商品信息
    def update(self,price=None,amount=None):
        if price != None:
            self.price = price
        if amount != None:
            self.amount = amount
#购物系统类
class ShoppingSystem:
    def __init__(self):
        self.goods_list = []
    #添加商品
    def add_goods(self):
        name = input("请输入商品名称:")
        for g in self.goods_list:
            if g.name == name:
                print("该商品已存在，请重新输入")
                return
        price = int(input("请输入商品的价格："))
        amount = int(input("请输入商品数量："))
        if price>=0 and amount>0:
            goods = Goods(name,price,amount)
            self.goods_list.append(goods)
            print("商品信息添加成功！")
        else:
            print("商品价格要大于等于0，商品数量要大于0")
    #修改商品信息
    def update_goods(self):
        name = input("请输入要修改的商品名称:")
        for g in self.goods_list:
            if g.name == name:
                price = int(input("请输入修改后的商品价格:"))
                amount = int(input("请输入修改后的商品数量:"))
                if price>=0 and amount>0:
                    g.update(price,amount)
                    print("商品信息修改成功")
                    print(f"当前学生信息：{g}")
                    return
                else:
                    print("商品价格要大于等于0，商品数量要大于0")
                    return
        print("该商品信息不存在，请重新输入")
    #删除商品信息
    def delete_goods(self):
        name = input("请输入要删除的商品名称:")
        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                print("删除成功~")
                return
        print("该商品信息不存在，请重新输入")
    #查询购物车
    def show_goods(self):
        if not self.goods_list:
            print("购物车中暂时没有商品，快去添加吧~")
        for g in self.goods_list:
            print(f"{g}")
    #运行系统
    def run_system(self):
        print("欢迎进入购物车系统~")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("1.添加商品 2.修改商品 3.删除商品 4.查询购物车 5.退出购物")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice = input("请输入您的操作(1-5)：")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.update_goods()
                case "3":
                    self.delete_goods()
                case "4":
                    self.show_goods()
                case "5":
                    print("本次使用结束~")
                    break
                case _:
                    print("输入错误，请输入1-5之间的数字")
ShoppingSystem().run_system()