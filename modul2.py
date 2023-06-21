# def f(start, end):
#     if start == end: return True
#     if start < 10: return False
#     return f(start//10 + start % 10, end) or f((start//10) * (start % 10), end)
#
# k = 0
# for x in range(10,100):
#     if f(x, 8):
#         k += 1
# print(k)

# def f(start, end):
#     if start > end or start == 20: return False
#     if start == end: return True
#     if start < end:
#         return f(start+1, end) + f(start+2, end) + f(start**2, end)
#
# print(f(6,18)*f(18,27))

# def f(x,k):
#     if x == 28 and k == 5:
#         return True
#     elif x  > 28:
#         return 0
#     return f(x+1,k+1) + f(x+2,k+1) + f(x*2,k+1)
#
# print(f(1,0))

# import math
# def f(start,end):
#     if start > end:return False
#     if start == end:return True
#     if start < end:
#         return f(start+1,end)+f(start+4,end)+f(start+math.factorial(start),end)
#
# print(f(1,10)*f(10,20))

# def f(start,end,prev=0):
#     if start > end: return False
#     if start == end: return True
#     if start < end:
#         return f(start+1,end,1)+f(start+2,end,2)+(0 if prev == 3 else f(start*2, end, 3))
#
# print(f(1, 15))

# s = set() # создаём пустое множество, чтобы избежать повторений
# def f(x, k):
#     global s
#     if k == 6:
#         s.add(x)
#     else:
#         f(x+1,k+1)
#         f(x+2,k+1)
#         f(x*2,k+1)
#
# f(1,0)
# s = sorted(s) # делаем из множества массив
# print(s)
# del s[:s.index(34)] # Методом тыка, смотря на весь массив подбираем индекс начала
# del s[s.index(64):] # Методом тыка, смотря на весь массив подбираем индекс конца
# print(s)
# print(len(s))

# def f(x,y):
#     if x > y or x == 21: return False
#     if x == y: return True
#     if x < y:
#         return f(x+1,y) + f(2*x+1,y)
#
# print(f(1,25))

# def f(x,y,k=0):
#     if x > y or x == 30 or x == 40: return False
#     if x==y:return True
#     if x < y:
#         return f(x+1,y,1)+f(x+3,y,2) + (0 if k == 3 else f(x*2,y,3))
#
# print(f(3,20)*f(20,60))

# def f(x,y):
#     if x > y:return False
#     if x==y:return True
#     if x < y:
#         return f(x+3,y)+f(x+4,y)+f(x**2,y)
#
# print(f(3,21)*f(21,36))

# s = set()
# def f(x,k):
#     global s
#     if k == 11:
#         if x < 0:
#             s.add(x)
#     else:
#         f(x-2,k+1)
#         f(x*-3,k+1)
# f(91,0)
# print(s)
# print(len(s))

# def f(x,y):
#     if x > y: return False
#     if x == y: return True
#     if x < y:
#         return f(x+2,y,) + f(x+3,y) + f(2*x-1,y)
#
# print(f(2,11))


# def f(x,y,k=0):
#     if x > y: return False
#     if x == y: return k % 2
#     if x < y:
#         return f(x+2, y, k+1) + f(x*2, y, k+1) + (0 if x == 1 else f(x**2, y, k+1))
#
# print(f(1,100))

# fib = [1,1]
# for i in range(30):
#     fib.append(fib[i]+fib[i+1])
# print(fib)
# def F(x,y):
#   if x > y:
#     return 0
#   if x == y:
#     return 1
#   return F(x+1,y)+F(x+3,y)+F(fib[x-1],y)
# print(F(6,21))

# def f(x,y,k):
#     if x > y or k > 3:
#         return False
#     elif x == y:
#         return True
#     k = 0 if k < 0 else k + (x % 6 == 0)
#     return f(x+2,y,k) + f(x*2,y,k) + f(x*3,y,k)
#
# print(f(1,300,0))

# def f(x,y):
#     if x > y: return False
#     if x == y: return True
#     if x < y:
#         if x % 2 == 0:
#             return f(x+1,y) + f(x*1.5,y)
#         else:
#             return  f(x+1,y)
#
# print(f(1,20))

# def f(x,y,k):
#     if x > y or k > 2: return False
#     if x == y: return True
#     if x < y:
#         if x % 2 != 0:
#             return f(x+2,y,k) + f(x+3,y,k) + f(x*2, y, k+1)
#         else:
#             return f(x+2,y,k) + f(x+3,y,k)
#
# print(f(3,46,0))

# s = set()
# def f(x,k):
#     if k == 7:
#         s.add(x)
#     else:
#         f(x+1,k+1)
#         f(x+5,k+1)
#         f(x*3,k+1)
# f(1,0)
# print(len(s))

# import math
# def f(x,y):
#     if x > y or x == 12: return False
#     if x == y: return True
#     if x < y:
#         return f(x+1,y) + f(x+4, y) + f(math.factorial(x+1),y)
# print(f(2, 24))

# def f(x,y):
#     if x < y: return False
#     if x == y: return True
#     if x > y:
#         return f(x-2,y) + f(x//2,y)
#
# print(f(28,10)*f(10,1))

# f = open('C:/Users/starm/Downloads/24.txt').readlines()
# m = 1000000
# for i in range(len(f)):
#     tmp = f[i].count('G')
#     if tmp < m:
#         m = tmp
#         ms = i
# alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# let = ''
# numb_let = 0
# for i in alp:
#     tmp = f[ms].count(i)
#     if numb_let <= tmp:
#         numb_let = tmp
#         let = i
#
# print(let)

# f = open('C:/Users/starm/Downloads/17var01.txt')
# a = [int(i) for i in f]
# n = []
# n1 = []
# for x in range(len(a)-1):
#     if (a[x] + a[x+1]) == max(a):
#         n.append(a[x] + a[x+1])
#         n1.append(a[x]**2+a[x+1]**2)
# print(len(n),max(n1))

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (((not x) or y or (not z)) and ((not x) == ((not y) or z))) == True:
#                 print(x, z, y)

# for n in range(1,1000):
#     print(n)
#     s = bin(n)[2:]
#     print(s)
#     if s.count('1') % 2 == 0:
#         s += '0'
#         s += '1'
#         print(s)
#     else:
#         s += '1'
#         s += '0'
#         print(s)
#     if int(s, 2) > 90:
#         print(int(s, 2), n)
#         break
# print(int('1011101', 2))

# from turtle import *
# tracer()
# k = 10
# for i in range(36):
#     forward(10*k)
#     right(50)
# update()
# done()

# for n in range(2, 100):
#     f = 0
#     for a in range(-100, 100):
#         for b in range(-100, 100):
#             if ((-47 + n*(31+a)+82 == 0) and (-19 + n*(9+b)-23 == 0)) == True:
#                 print(a,b,n)

# def I3_(c):
#     s = ''
#     h = '0123456789ABCD'
#     while c > 0:
#         s = h[c % 13] + s
#         c = c // 13
#     return s
#
# for x in range(16, 40):
#     if I3_(13**40 + 13**x - 13**15).count('C') == ((I3_(13**40 + 13**x - 13**15).count('0')/3)):
#         print(I3_(13 ** 40 + 13 ** x - 13 ** 15))
#         print(I3_(13 ** 40 + 13 ** x - 13 ** 15).count('C'))
#         print(I3_(13 ** 40 + 13 ** x - 13 ** 15).count('0'))
#         print(x)

# c = 0
# for a in range(1, 100):
#     f = 0
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (((x**2 <= a) <= (x <= 5)) or ((y**2 <= a) <= (y < 2))) == False:
#                 f = 1
#                 break
#         if f == 1:
#             break
#     if f == 0:
#         c = c + 1
# print(c)

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n <= 2:
#         return n * n
#     if n > 2:
#         return f(n-2) + g(n-1)*2-n
#
# def g(n):
#     if n <= 2:
#         return n + 1
#     if n > 2:
#         return g(n - 1) + f(n - 2) + n
#
# print(((f(5) + g(3))**0.5 + g(3) + g(2))**0.5)

# f = open('C:/Users/starm/Downloads/17__1va5d.txt')
# a = [int(i) for i in f]
# n = []
# sr_chet = sum([t for t in a if t % 2 == 0]) / len([t for t in a if t % 2 == 0])
# for j in range(len(a) - 1):
#     if (a[j] % 3 == 0 or a[j+1] % 3 == 0) and (a[j] < sr_chet or a[j+1] < sr_chet):
#         n.append(a[j] + a[j+1])
# print(len(n), max(n))

# def f(start, end):
#     if start == end:
#         return 1
#     if start > end or start == 19:
#         return 0
#     if start < end:
#         return f(start + 2, end) + f(start * 2, end) + f(start * 3, end)
#
# print(f(3, 28) * f(28, 35))

# x = 0
# y = 0
# z = 0
#
# f = open('C:/Users/starm/Downloads/24__1va5g.txt').readline()
# print('ZZZZZZZ' in f)

# x = 500019, 18
# y = 333396
# z = 166585, 7

# f = [0]* 400000
# f[0] = 1
# f[1] = 1
# for n in range(2, len(f)):
#     f[n] = f[n-1] + f[n-2]
#     if f[n] < 400000 and f[n] > 300000:
#         print(f[n])

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(factorial(9))

# f = open('C:/Users/starm/Downloads/27_B__1va5j.txt')
# a = [int(i) for i in f]
# mn = md = maxs = 0
# for j in range(1, len(a)):
#     if a[j-1] > md and (a[j-1] % 7 == 0) and (a[j-1] % 49 != 0) :
#         md = a[j-1]
#     if a[j-1] > mn and (a[j-1] % 7 != 0) and (a[j-1] % 49 != 0):
#         mn = a[j-1]
#
# print(md * mn, md, mn)

# n = []
# for g in range(1, len(a)):
#     if (a[g-1] % 7 == 0) and (a[g-1] % 49 != 0):
#         n.append(a[g-1])
# print(sorted(n))

# P = [2,4,6,8,10,12,14,16,18,20]
# Q = [3,6,9,12,15,18,21,24,27,30]
# A = list(range(1, 1000))
# for x in range(1, 1000):
#     if (((x in A) <= (not(x in P))) and ((not(x in Q)) <= (not(x in A)))) == False:
#         A.remove(x)
# print(A)

# f = open('C:/Users/starm/Downloads/27-2b__1vrrg.txt')
# n = int(f.readline())
# s = 0
# d = []
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     s += max(a, b)
#     d.append(abs(a-b))
# d.sort()
#
# print(s)

# for A in range(1, 3000):
#     f = 0
#     for x in range(1, 1000):
#         if ((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == False:
#             f = 1
#     if f == 0:
#         print(A)


