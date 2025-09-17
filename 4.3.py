'#111111'
a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
print(sum)

'#2232222222'
a = 2
b = 3
c = 7
if (a + b > c) and (a + c > b) and (b + c > a):
    print((1 / 2) * a * b)
else:
    print('Некорректные данные треугольника')

'#333333'
n = int(input())

if n > 1440:
    n = n - 1440
    chas = n // 60
    min = n % 60
else:
    chas = n // 60
    min = n % 60
print(chas, ':', min)

'#44444'

def calcul(a,b,l,N):
    return 2 * l + (2 * N - 1) * a + 2 * (N -1) * b
print(calcul(2, 1, 3,4))

'#555555'
a = [2, 5, 6]
a2 = sum(a) - max(a) - min(a)
a3 = sum(a) - a2 - max(a)
print(a3)

'666666'
per,vtor,tret,chet = map(int,input().split())
print('Yeah' if (per + vtor) % 2 == (tret + chet) % 2 else 'Noooope')

'7777777'
n = int(input())
print('Yeah' if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else 'Noooope')

'88888'
a, b, c = map(int,input().split())
if a == b == c:
    print('3')
if a == b and a != c:
    print('2')
if a == c and c != b:
    print('2')
if c == b and b != a:
    print('2')
if a != b != c != a:
    print('0')

'99999'
n, m, k = map(int,input().split())
print('Yeah' if k <= m * n and (k % m == 0 or k % n == 0) else 'Noooope')