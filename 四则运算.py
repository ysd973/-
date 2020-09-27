import profile
import random
from fractions import Fraction

#四则运算

def szys():

    sym = ['＋', '－', '×', '÷']

    f= random.randint(0, 3)

    z = random.randint(0, 1)#设置一个随机值，如果是1就进行整数运算，如果是0进行分数运算

    n1 = random.randint(1, 20)

    n2 = random.randint(1, 20)

    n3 = random.randint(1, 20)

    n4 = random.randint(1, 20)

    result = 0

    if z==0 :

        n1, n2 = max(n1, n2), min(n1, n2)

        if f == 0:#加法

            result  = n1 + n2

        elif f == 1:#减法，要先比较大小，防止输出负数

            n1, n2 = max(n1, n2), min(n1, n2)

            result  = n1 - n2

        elif f== 2:#乘法

            result  = n1 * n2

        elif f == 3:#除法，要比较大小，并循环取整除

            n1, n2 = max(n1, n2), min(n1, n2)

            while n1 % n2 != 0:

                n1 = random.randint(1, 10)

                n2 = random.randint(1, 10)

                n1, n2 = max(n1, n2), min(n1, n2)

            result  = int(n1 / n2)

        print(n1, sym[f], n2, '= ', end='')

        return result

    if z == 1:

        n1, n2 = min(n1, n2), max(n1, n2)#把n1，n2中小的放在前面，保证f1为真分数

        n3, n4 = min(n3, n4), max(n3, n4)#把n3，n4中小的放在前面，保证f2为真分数

        f1 = Fraction(n1, n2)#初始化f1为n1/n2

        f2 = Fraction(n3, n4)#初始化f2为n3/n4

        if f == 0:#加法

            result  = f1 + f2

        elif f == 1:#减法，要先比较大小，防止输出负数

            f1, f2 = max(f1, f2), min(f1, f2)

            result  = f1 - f2

        elif f== 2:#乘法

            result  = f1 * f2

        elif f == 3:#除法，要比较大小，并循环取整除

            while n1 % n2 != 0:

                n1 = random.randint(1, 20)

                n2 = random.randint(1, 20)

                n1, n2 = min(n1, n2), max(n1, n2)

                n3, f2 = min(n3, n4), max(n3, n4)

            result  = Fraction(f1 / f2)

        print(f1, sym[f], f2, '= ', end='')

        return result





print('输入数字1进行四则运算')
print('输入数字2进行性能测试')

n=int(input())

#当输入1时，进行四则运算，调用函数syzs()

if n==1:

    while True:

        result  = szys()

        j= input()

        s=eval(j)

        if s== result :

            print('rright')

        else:

            print('error.，the answer is', result )
if n==2:
    profile.run('szys()')
