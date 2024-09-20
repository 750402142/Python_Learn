

money = 5000000
name  = input("请输入您的姓名")


print(name)


def check_money():
    print(f"{name},您银行卡中的余额为{money}")

def saving_money(num):
    global money
    money += num
    print(f"存取后您的余额为{money}")
def putting_money(num):
    num = int(input("您要取出的余额为:"))
    global money
    money -= num
    print(f"取钱后您的余额为{money}")
def back_menu():
    print("返回到主菜单")

def main():
    print("-------------主菜单------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")    # 通过\t制表符对齐输出
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

while True:
    result  = main()
    if result == "1":
        check_money()
    elif result == "2":
        num = int(input("您要存取的余额为:"))
        saving_money(num)
        continue
    elif result == "3":
        num =  input("您要取出的余额为:")
        putting_money(num)
        continue
    elif result == "4":
        back_menu()
        break




