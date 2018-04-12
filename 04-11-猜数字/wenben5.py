import time
import datetime
import re
import os
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#获取当前时间
start = time.clock()#程序开始的时间
#有昵称的函数
def youxi():
    f = input("你好，请输入你的昵称：")
    print("请选择1:开始游戏  2：查询历史数据 3、更改昵称")
    k = input("你的选择是：")
    k = int(k)
    while k < 1 or k > 3:
        k = input("你的选择是：")
        k = int(k)
    if k == 1:
        print("游戏开始时间：", nowTime)
        e = open("cde.txt", "at")#打开或创建一个文件
        a = input("请出题者输入数字：")
        a = float(a)
        b = input("请猜题者输入数字：")
        b = float(b)
        c = 0
        while b != a:
            if b > a:
                b = input("大了，请猜题者再次输入数字：")
                b = float(b)
            elif b < a:
                b = input("小了，请猜题者再次输入数字：")
                b = float(b)
            c += 1
        else:
            print('恭喜，您猜对了！')
            print("一共猜测了", c + 1, "次")
            d  = (time.clock() - start)
            print("游戏一共用时：", d, "秒")
            e.write("玩家昵称：" + str(f) + '\n')
            e.write("所猜数字：" + str(b) + '\n')
            e.write("猜测次数：" + str(c + 1) + '\n')
            e.write("游戏开始时间：" + str(nowTime) + '\n')
            e.write("游戏历时：" + str(d) + '\n' + '\r')
    elif k == 2:
        m = open("cde.txt", "at")
        s = m.read()
        print(s)
        m.close()
#更改昵称
    elif k==3:
        j=open("cde.txt","r+")
        g=j.read()
        j.seek(0,0)
        xxx=input("输入新的昵称：")
        j.write(g.replace(f,xxx))
        j.close()
        print("修改昵称成功！")
#没有昵称的函数
def jb():
    f = input("你好，请创建你的游戏昵称：")
    print("游戏开始时间：", nowTime)
    k = open("cde.txt", "at")
    a = input("请出题输入数字：")
    a = float(a)
    b = input("请猜题者输入数字：")
    b = float(b)
    c = 0
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
        print("一共猜测了", c + 1, "次")
        e = (time.clock() - start)
        print("游戏一共用时：", e, "秒")
        k.write("玩家昵称：" + str(f) + '\n')
        k.write("所猜数字：" + str(b) + '\n')
        k.write("猜测次数：" + str(c + 1) + '\n')
        k.write("游戏开始时间：" + str(nowTime) + '\n')
        k.write("游戏历时：" + str(e) + '\n'+'\r' )
#主程序
print("----欢迎来到猜数字游戏！----")
print("是否有昵称？ 1、有  2、没有")
d=int(input("你的选择是："))
while d<1 or d>2:
    print("请输入有效的数字！")
    d = int(input("你的选择是："))
if d==1:
    youxi()
elif d==2:
    jb()
