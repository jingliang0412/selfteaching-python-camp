#这是一个打印乘法表的程序，并使用流程控制打印除去偶数的乘法表

def Multiplication_table(a):    #定义一个乘法表，它的功能是输出一个a*a的乘法表
    for x in range(1,a+1):   #判断当x在1至a之间（即1，2,……,a）时,开始循环
        for y in range(1,x+1):   #判断当y在1至x之间（即1，2,……,x）时,开始循环
            print(x,'*',y,'=',x*y,end = '   ')   #打印“x*y=”及其运算结果
            if x == a and y == a-1:   #判断当x=a且y=a-1时，执行以下语句
                print("\n")   #打印一个“换行符”即“回车”  
        
        print("\n")   #打印一个“换行符”即“回车”
    
    else:   #当循环结束时，执行以下程序
        return ' '  #为了不出现“None”，返回一个“空格”

def Multiplication_table1(a):   #定义一个乘法表，它的功能是输出一个去掉偶数行的a*a的乘法表
    x = 1   #给x赋值为1
    while x <= a:   #判断当x在1至a之间（即1，2,……,a）时,开始循环
        y = 1   #给y赋值为1
        while y <=x:    #判断当y在1至x之间（即1，2,……,x）时,开始循环
            if x % 2 != 0:   #判断当x为奇数时，执行语句
                print(x,'*',y,'=',x*y,end = '   ')   #打印“x*y=”及其运算结果
                if x == a and y == a-1:   #判断当x=a且y=a-1时，执行以下语句
                    print("\n")   #打印一个“换行符”即“回车”

            y += 1   #把y+1的值赋给y,即y=y+1
        while x % 2 != 0:   #判断当x为奇数时，开始循环。说明：这里是可以用if语句代替的，我的主要目的是测试一下break的功能
            print("\n")   #打印一个“换行符”即“回车”
            break   #跳出while循环
        
        x += 1   #把x+1的值赋给x,即x=x+1
    
    else:   #当循环结束时，执行以下程序
        return ' '  #为了不出现“None”，返回一个“空格”



print("Wecome！这是一个打印乘法表的程序")   #打印：欢迎界面

print("以下是关于本程序的说明：\n")   #打印：本程序的说明
print("1.本程序仅能打印正整数的乘法表,且只能进行二元计算;\n")
print("2.退出程序请输入“.”（重要）;\n")
print("3.使用本程序时请确认已切换到全英文输入法;\n")
print("4.请根据提示一步一步进行，谢谢合作!\n")

d0 = input("退出打印请输入“.”，继续打印请输入任意值，请输入：")   #打印：输入提示，并将用户输入的值赋给d0

while d0 != '.':    #用while语句（循环语句）判断：当d0不等于'.'时，开始循环
    d1 = input("请输入一个正整数：")    #打印：输入第一个正整数的提示，并将用户输入的值赋给d1

    while not d1.isdigit() or int(d1) < 0:   #用while语句（循环语句）判断：当d1不是正整数时，开始循环
        d1 = input("\n您的输入有误，请重新输入一个正整数：")    #重新为d1赋值，直到用户输入为正整数时，循环结束

    else:   #当循环结束时，执行以下程序
        print("以下为",d1,'*',d1,"的乘法表：")   #打印提示
        print(Multiplication_table(int(d1)))    #调用Multiplication_table（）函数，并把它返回的结果打印出来
        print("以下为",d1,'*',d1,"去掉偶数行的乘法表：")    #打印提示
        print(Multiplication_table1(int(d1)))    #调用Multiplication_table1（）函数，并把它返回的结果打印出来
        d0 = input("\n继续运算请输入任意值，退出计算请输入“.”，请输入：")   #打印：询问用户是否继续运算，并将用户输入的值赋给d0，循环继续，返回到第48行开始执行

else:   #当d0等于'.'时，不执行循环，程序结束
    print("再见！")   #打印程序结束的提示