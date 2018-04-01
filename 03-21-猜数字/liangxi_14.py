a = input("请出题者输入数字：")
a = float(a)
b = input("请猜题者输入数字：")
b = float(b)
c = 0
if b == a:
    print("猜对了！")
    c += 1
    print("一共猜测了", c, "次")
else:
    while b != a:
        b = input("不对，请猜题者再次输入数字：")
        b = float(b)
        if b > a:
            print("您输入的数字大了！")
        elif b < a:
            print("您输入的数字小了！")
        c += 1
    else:
        print('恭喜，您猜对了！')
        print("游戏结束，再见!")
        print("一共猜测了", c + 1, "次")

