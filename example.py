# import
# 导入
from pyfrac import * # you must import this
from math import ceil # not necessary


'''Fraction class manual
search your problems with "Ctrl+F", like "call numerator"'''
'''Fraction 类使用手册
你可以直接用 Ctrl+F 搜索问题，比如“调用分子”'''

'''Create a fraction'''
'''创建一个分数'''
# create a fraction with no input, return frac(0, 1), which means zero fisrt
# 无输入创建一个分数，会返回分数 frac(0, 1)，意思是零分之一
fracNone = frac()

# input a num, will reduce automatically
# 输入一个数字，它会自动化简
# the denominator will always be positive and not complex
# 化简结果中分母永远为正实数
frac0 = frac(0.5)
print(frac0)
# 1 / 2

# the numbers follow behind the first number will be seen as denominator
# 第一个数之后的数字都会被认为是分母
frac1 = frac(0.5, 2)
print(frac1)
# 1 / 4

# if more than one numbers are behind the first one, multiply them as denominator
# 如果第一个数之后的数字超过一个，会将他们相乘作为分母
frac2 = frac(1, 2, 3)
print(frac2)
# 1 / 6

# it support complex
# 它支持复数
frac3 = frac(1+0.5j, 2)
print(frac3)
# (2 + 1j) / 4

# you can combine fractions
# 你可以输入分数
frac4 = frac(frac1, frac2)
print(frac4)
# 3 / 2

# Tags: take too long, crash, run slowly, error output
# 标签：花费时间过长，崩溃，程序跑得慢
# what you SHOULD NOT do
# 请 别 脑 抽 这 么 干
# frac5 = frac(1 / 3)
# the input is actually a complex float, will return a complex fraction as well, not frac(1, 3)
# 输入的数字实际上是个过于复杂的小数，返回的也是个很复杂的小数，而不是frac(1, 3)
# please do like this
# 请这样做
frac5 = frac(1, 3)


'''Call'''
'''调用'''
# Tags: IDLE, Interactive console, display
# 标签：IDLE，交互式控制窗口，直接显示
# in interactive console like IDLE, you can check fraction variable like this
# 在交互式控制窗口（像IDLE），你可以这样来查看一个分数变量
# >>> frac0
# frac(1, 4)

# Tags: call content
# 标签：调用内容
# to call the fraction, a tuple(numerator, denominator) will be returned
# 引用这个分数，会返回一个包含分子和分母的元组
print(frac1())
# (1, 4)

# Tags: call numerator, call denominator
# 标签：调用分子，调用分母
# to get specific content of the fraction, input index
# 要获取一个分数中某个数，输入索引值
print(frac1(0)) # en: call numerator; zh: 调用分子
# 1
print(frac1(1)) # en: call denominator; zh: 调用分母
# 4
print(frac1(2)) # en: same as frac1(); zh: 作用与frac1()相同

'''Transform'''
'''转换'''
# Tags: transform to integer
# 标签：转换为整型
# just use int() like transform a float
# 直接像转换一个浮点小数到整数一样使用int()即可
# error will be occured if the fraction contains complex
# 如果这个分数包含复数，会报错
# will not change the fractions itself
# 不会改变这个分数本身
print(int(frac0))
# 0

# Tags: transform to float
# 标签：转换成浮点小数
# much like integer transform, read that above instead
# 和整数转换极为相似，可以直接参照它（就在上面贴贴）
print(float(frac0))
# 0.5

# Tags: transform to complex
# 标签：转换成复数
# just use complex() like transform a float
# 直接像转换一个浮点小数到复数一样使用complex()即可
# will not change the fractions itself
# 不会改变这个分数本身
print(complex(frac0))
# (0.5 + 0j)

# Tags: transform to boolean
# 标签：转换成布尔类型
# just use bool() like transform a float
# 直接像转换一个浮点小数到布尔类型一样使用bool()即可
# will not change the fractions itself
# 不会改变这个分数本身
print(bool(frac0))
# True
# if numerator is 0, return False
# 如果分子为0，返回False

'''Computing operation'''
'''计算处理'''
# Tags: normal operation, add, sub, multiply, division, floor, mod, power
# 标签：一般计算，加，减，乘，除，整除，取余，乘方
# normal computing operations are all supported
# 常见的运算都支持
print(frac0 + frac1)
frac0 + 0.25
# 3 / 4)

print(frac0 - frac1)
frac0 - 0.25
# 1 / 4

print(frac0 / 2)
# 1 / 4
frac0 / frac1
# 2

print(frac0 * frac1)
frac0 * 0.25
# 1 / 8

print(frac0 // frac1)
frac0 // 0.25
# 2

print(frac0 % frac1)
frac0 % 0.25
# frac(0, 1)

print(frac0 ** 2)
# frac(1, 4)
# we support this but you'd better not do power with float like numbers
frac1 ** frac0
# frac(1, 2)

# some operations of functions
# 一些函数运算
# calculate numerator / denominator
# 计算 分子/分母
print(frac0.calc())
# 0.5

# abs() to get module
# 用abs()函数取模
print(abs(frac0))
# 0.5

# take floor and mod
# 同时整除并取余
print(divmod(frac0, 1))
# (0, frac(1, 2))

# take ceil of the fraction
# 向上取整
print(ceil(frac0))
# 1


# comparison operation is also supported
# 比较运算符同样支持
# >, >=, <, <=, do not support complex or fracctions with complex
# 注意 >, >=, <, <= 不支持复数或含有复数的分数即可

# bit operation is supported
# 支持位运算符
# every number that matches will operate together
# 对应的数字相互运算
# every number that operates with fractions will be converted into fraction
# 与分数相运算的数字会先转换成分数

'''String Convertion'''
'''字符串转换'''
# str() function
# str() 函数
print(str(frac0))
# "1 / 2"

# string format
# 格式化字符串
print("{}".format(frac0))
# "1 / 2"

'''Other Functions'''
'''其他函数'''
# get greatest common divisor
# 获取一组数的最大公约数
print(frac.getmaxdiv(set((4, 6))))
# 2
