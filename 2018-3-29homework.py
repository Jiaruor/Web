#2018-3-29魏波 作业

#课堂练习.1.画星星
j = 1
while j <= 10:
    i = 1
    while i <= j :
        print('*',end='')
        i += 1
    j += 1
    print()

#课堂练习.2.99乘法表
i = 1
while i < 10:
    j = 1
    while j < i:
        print('%d*%d=%d  ' %(j,i,i*j), end='')
        j += 1
    print()
    i += 1

print()
#2.3.1.1.使⽤if，编写程序，实现以下功能：

Id = input("请输入用户名")
password = input('请输入密码')

if Id == 'weibo' and password == '123456':
    print('欢迎%s进入源码世界' %Id)
else:
    print('账户和密码不匹配,请重新输入')

#2.3.1.2.使⽤while，完成以下图形的输出

x = 1
while x < 6:
    x += 1
    y = 1
    while x > y :
        print('*', end='')
        y += 1
    print()
while x < 10:
        y = 0
        while 9 - x > y:
            print('*', end='')
            y += 1
        print()
        x += 1

#2.3.1.3.计算 1 - 2 + 3 ... + 99所有数的总和？

i = 1
s = 0
while i < 100:
    s += i*(-1)**(i+1)
    i = i+1
print('1 - 2 + 3 ... + 99='+str(s))

#2.3.1.4.continue和break区别？
#答:continue结束当前循环,继续下一次循环;break直接结束所有循环.

#2.3.2.1.选做题.⽤⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤⽤字符串串格式化）
i = 3
while i > 0 :
    Id = input("请输入用户名")
    password = input('请输入密码')
    if Id == 'weibo' and password == '123456':
        print('欢迎光临')
    else:
        print('账户和密码不匹配,请重新输入')
    i -=1
print('错误超过3次,明天再来')

#2.3.3.面试题
#2.3.3.1.打印结果是：  (选E)
# x  =  “foo”
# y = 2
# print(x+y)
#A.foo  B.foofoo  C.foo2  D.2  E.An  exception  is  thrown

#2.3.3.2. while的循环次数是多少？
k=1000
i= 0    #循环的次数
while  k>1:
    i += 1      #每次循环开始i+1
    print(k)
    k  =  k/2
print(i)
#答:循环10次.

#2.3.4.每日一练
# 1.name = input(“>>>”) name变量是什么数据类型？
#答:name的数据类型为字符串.

# 2.简述 int 和 9 等数字 以及 str 和 "xxoo" 等字符串的关系？
#答:int和str为类名,9和"xxoo"为类容,统一类名的内容拥有共同的特性和功能,可以相互运算.

# 3.⼀⻔语⾔的基础组成部分有哪些？
#答:一门编程语言主要由变量/数据类型/运算符/流程控制/函数/对象等组成.

# 4.运算符有哪些分类？
#答:数学运算/比较运算/赋值运算/逻辑运算/位运算等.

# 5.什么是关键字？
#答:具有特殊意义的标志符.

# 6.判断对错
# 6.1.Python是⼀种跨平台、开源、免费的⾼级动态编程语⾔                   True
# 6.2.已知 x = 3，那么赋值语句 x = 'abcedfg' 是⽆法正常执⾏的。         False
# 6.3.Python 3.x完全兼容Python 2.x                                  False