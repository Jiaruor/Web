#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#作业1.11.1.4
#求和运算
#用户输入
a = input('请输入一个数')
b = input('请输入第二个数')
a = int (a) #切换数据类型为整数
b = int (b)
print('a+b=',a+b)

#作业1.11.2.1
#编写1个python程序，完成以下要求： 从键盘获取⽤户的姓名、姓名、家庭地址 使⽤⼀个print进⾏输出
name = input('你叫什么名字')
age= input('几岁了')
id = input('你在哪里')
like = input('喜欢干什么')
print(age,name,id,like)

#作业1.11.2.2
#需求：等待⽤⽤户输⼊⼊名字、地点、爱好，根据⽤⽤户的名字和爱好进⾏⾏⾏任意现实如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
#用户输入
name = input('你叫什么名字')
age= input('几岁了')
id = input('你在哪里')
like = input('喜欢干什么')
print(age,'岁的',name,'喜欢在',id,like)  #输出变量及字符串

#作业1.11.2.3
#计算 1 + 2 + 3 ... + 99 的总和

i = 1   #设置变量
sum = 0 #设置变量
while i<=100:   #设置循环条件
    sum +=i     #求和
    i +=1       #一次累加之后自加
print (sum)     #输出结果
