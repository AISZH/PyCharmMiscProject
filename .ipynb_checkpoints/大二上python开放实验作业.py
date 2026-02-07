'''
print("  *  ")
print(" *** ")
print("*****")
print(" *** ")
print("  *  ")

print("    小池  ")
print("泉眼无声惜细流")
print("树阴照水爱阴柔")
print("小荷才露尖尖角")
print("早有蜻蜓立上头")


r=int(input('请输入圆的半径：'))
s=round(3.14*r*r)
print('圆的面积是：',s)

print((3.14) * 2)

import math

def xiebian(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
a, b = map(float, input("请输入直角边的值（用空格分隔）:").split())
print("斜边长为：", xiebian(a, b))

import math
def C(hypotenuse,angle):
    a=math.sin(math.radians(angle))*hypotenuse
    b=math.cos(math.radians(angle))*hypotenuse
    c=a+b+hypotenuse
    return c
print(C(100,35))
'''
wine=0
for i in range (3):
    wine=(wine+1)/2
print(f"壶中原来有{wine}斗酒")
