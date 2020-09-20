import profile
import random

#四则运算

def szys():

    sym = ['＋', '－', '×', '÷']

    f= random.randint(0, 3)

    n1 = random.randint(1, 20)

    n2 = random.randint(1, 20)

    result = 0

    if f== 0:#加法

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

print('输入数字1进行四则运算')

n=int(input())

#当输入1时，进行四则运算，调用函数syzs()

if n==1:

    while True:

        result  = szys()

        j= input()

        s= int(j)

        if s== result :

            print('right')

        else:

            print('error.，the answer is', result )
    
