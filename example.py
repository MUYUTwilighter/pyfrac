# import
# 导入
from pyfrac import *

'''Fraction class manual
search your problems with "Ctrl+F", like "call numerator"'''
'''Fraction 类使用手册
你可以直接用 Ctrl+F 搜索问题，比如“调用分子”'''

'''Create a fraction'''
'''创建一个分数'''
# input a num, will reduce automatically
# 输入一个数字，它会自动化简
# the denominator will always be positive and not complex
# 化简结果中分母永远为正且不是复数
frac0 = frac(0.5)
print(frac0)
# >>> frac(1, 2)

# the numbers follow behind the first number will be seen as denominator
# 第一个数之后的数字都会被认为是分母
frac1 = frac(0.5, 2)
print(frac1)
# frac(1, 4)

# if more than one numbers are behind the first one, multiply them as denominator
# 如果第一个数之后的数字超过一个，会将他们相乘作为分母
frac2 = frac(1, 2, 3)
print(frac2)
# frac(1, 6)

# it support complex
# 它支持复数
frac3 = frac(1+0.5j, 2)
print(frac3)
# frac((2 + 1j), 4)

# you can combine fractions
# 你可以输入分数
frac4 = frac(frac1, frac2)
print(frac4)
# frac(3, 2)

# Tags: take too long, crash, run slowly
# 标签：花费时间过长，崩溃，程序跑得慢
# what you SHOULD NOT do
# 请 别 脑 抽 这 么 干
# frac5 = frac(1 / 3)
# the input is actually a complex float, will take quite a while to be reduced
# 输入的数字实际上是个过于复杂的小数，会花上很久来化简


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
frac1()
# (1, 4)

# Tags: call numerator, call denominator
# 标签：调用分子，调用分母
# to get specific content of the fraction, input index
# 要获取一个分数中某个数，输入索引值
frac1(0) # en: call numerator; zh: 调用分子
# 1
frac1(1) # en: call denominator; zh: 调用分母
# 4
frac1(2) # en: same as frac1(); zh: 作用与frac1()相同

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
int(frac0)
# 0

# Tags: transform to float
# 标签：转换成浮点小数
# much like integer transform, read that above instead
# 和整数转换极为相似，可以直接参照它（就在上面贴贴）
float(frac0)
# 0.5

# Tags: transform to complex
# 标签：转换成复数
# just use complex() like transform a float
# 直接像转换一个浮点小数到复数一样使用complex()即可
# will not change the fractions itself
# 不会改变这个分数本身
complex(frac0)
# (0.5 + 0j)

# Tags: transform to boolean
# 标签：转换成布尔类型
# just use bool() like transform a float
# 直接像转换一个浮点小数到布尔类型一样使用bool()即可
# will not change the fractions itself
# 不会改变这个分数本身
bool(frac0)
# True
# if numerator is 0, return False
# 如果分子为0，返回False

'''Computing operation'''
'''计算处理'''
# Tags: normal operation, add, sub, multiply, division, floor, mod, power
# 标签：一般计算，加，减，乘，除，整除，取余，乘方
# normal computing operations are all supported
# 常见的运算都支持
frac0 + frac1
frac0 + 0.25
# frac(3, 4)

frac0 - frac1
frac0 - 0.25
# frac(1, 4)

frac0 / 2
# frac(1, 4)
frac0 / frac1
# frac(2, 1)

frac0 * frac1
frac0 * 0.5
# frac(1, 8)

frac0 // frac1
frac0 // 0.25
# 2

frac0 % frac1
frac0 % 0.25
# 0

frac0 ** 2
# frac(1, 4)
# we support this but you'd better not do power with float like numbers
frac1 ** frac0
# frac(1, 2)

# comparison operation is also supported
# 比较运算符同样支持
# >, >=, <, <=, do not support complex or fracctions with complex
# 注意 >, >=, <, <= 不支持复数或含有复数的分数即可
