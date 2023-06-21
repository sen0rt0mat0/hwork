# ДЕЛИТЕЛИ ЧИСЛА
#
# count = 0
# for number in range(1, 10000):
# 	dels = []
#
# 	for i in range(1, int(number ** 0.5) + 1):
# 		if i * i == number:
# 			dels.append(i)
# 		elif number % i == 0:
# 			dels.append(i)
# 			dels.append(number // i)
# 		if len(dels) > 7:
# 			break
#
# 	if len(dels) == 7:
# 		count += 1
#
# print(count)


# 5 ЗАДАНИЕ

# k = 0
# for n in range(1,1000):
#     s = bin(n)[2:]
#     if s.count('1') % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     if s.count('1') % 2 == 0:
#         s += '0'
#     else:
#         s += '1'
#     if 20 <= int(s, 2) <= 50:
#         k += 1
# print(k)

# for n in range(1,1000):
#     s = bin(n)[2:]
#     if s.count('1') > s.count('0'):
#         s += '1'
#     else:
#         s += '0'
#     if int(s, 2) < 43:
#         print(int(s,2))

# for n in range(1,1000):
#     s = bin(n)[2:]
#     s = (8 - len(s)) * '0' + s
#     s1 = ''
#     for x in s:
#         if x == '1':
#             s1 += '0'
#         else:
#             s1 += '1'
#     if int(s1,2) - n == 99:
#         print(n)

# 6 ЗАДАНИЕ

# from turtle import *
# k = 25
# screensize(7000,7000)
# tracer(0)
# forward(100*k)
# right(90)
# forward(100*k)
# right(30)
# down()
# for i in range(11):
#     forward(25*k)
#     right(90)
# up()
# for x in range(60,120):
#     for y in range(-130,-45):
#         goto(x*k,y*k)
#         dot(2, 'red')
# done()
# update()

# 12 ЗАДАНИЕ

# t = '1' * 8 + '2' * 8
# while ('111' in t) or '222' in t:
#     if ('111' in t):
#         t = t.replace('111', '2', 1)
#     if ('222' in t):
#         t = t.replace('222','1',1)
# print(t)


# 14 задание

# r = []
# for x in '0123456789ABCDE':
#     for y in '0123456789ABCDE':
#         t = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)
#         if t % 56 == 0:
#             r.append(t)
#             break
# if r:
#     print(min(r)//56)


# 15 задание
# НА ДЕЛ

# for A in range(1, 3000):
#     f = 0
#     for x in range(1, 1000):
#         if ((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == False:
#             f = 1
#     if f == 0:
#         print(A)

# НА ПОБИТОВУЮ

# for A in range(1,1000):
#     k = 0
#     for x in range(1, 1000):
#         if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))) == False:
#             k = 1
#             break
#     if k == 0:
#         print(A)
#         break

# НА ГРАФИКИ

# for a in range(1, 1000):
#     k = 0
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if ((a <= (x**2 <= 64)) and ((x**2 <= 25) <= a)) == False:
#                 k = 1
#                 break
#         if k == 1:
#             break
#     if k == 0:
#         print(a)

# A = list(range(-1000, 1000))
# for x in range(-1000, 1000):
#     if (((x in A) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in A))) == False:
#         A.remove(x)
# print(A)

# НА ОТРЕЗКИ

# НА МИНИМУМ
# P = list(range(5, 31))
# Q = list(range(14, 24))
# A = []
# for x in range(1, 100):
#     if (((x in P) == (x in Q)) <= (not(x in A))) == False:
#         A.append(x)
# print(A)

# НА МАКСИМУМ
# P = list(range(5, 31))
# Q = list(range(14, 24))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if (((x in P) == (x in Q)) <= (not(x in A))) == False:
#         A.remove(x)
# print(A)

# 16 Задание
# from functools import *
# @lru_cache(None)

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 2:
#         return f(n-1) + 1
#     if n > 0 and n % 3 < 2:
#         return f((n-(n%3))/3)
#
# for n in range(1,1001):
#     if f(n) == 5:
#         print(n)
#         break


# f = [0] * 2024
# for n in range(len(f)):
#     if n == 1:
#         f[n] = 1
#     if n > 1:
#         f[n] = n * f[n-1]
# print(f[2023]/f[2020])

# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 3 == 0:
#         return f(n / 3)
#     if n % 2 != 0:
#         return 1 + f(n - 1)
# k = 0
# for n in range(1,901):
#     if f(n) == 9:
#         k += 1
# print(k)
# for n in range(1, 1001):
#     if f(n) == 5:
#         print(n)
#         break

# Задание 17

# f = open('C:/Users/starm/Downloads/17 (8).txt')
# a = [int(i) for i in f]
# n = []
# for g in range(len(a) - 1):
#     if (a[g] % 3 == 0 or a[g+1] % 3 == 0) and (a[g] + a[g+1]) % 5 == 0:
#         n.append(a[g] + a[g+1])
# print(len(n), max(n))

# f = open('17.txt')
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] % 10 == 0:

# Задание 23

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

# Задание 24

# f = open('C:/Users/starm/Downloads/24 (1).txt').readlines()
# m = 1000000
# for i in range(len(f)):
#     tmp = f[i].count('N')
#     if tmp < m:
#         m = tmp
#         ms = i
#
# alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# let = ''
# num_let = 0
# for i in alf:
#     tmp = f[ms].count(i)
#     if num_let <= tmp:
#         num_let = tmp
#         let = i
# print(let)

# f = open('C:/Users/starm/Downloads/24_demo (2).txt').readline()
# f = f.replace('Y', ' ').replace('Z',' ')
# print(max(len(i) for i in f.split()))

# f = open('C:/Users/starm/Downloads/24_demo (3).txt').readline()
# c = 'XYZ'*4 + 'X'
# print(c in f)

# f = open('C:/Users/starm/Downloads/zadanie24_1.txt').readline()
# c = 1
# m = 0
# for i in range(len(f)-1):
#     if f[i] != f[i+1]:
#         c += 1
#         m = max(c, m)
#     else: c = 1
#
# print(m)

# from fnmatch import *
# f = open().readline()
# for c in 'QWERTYUIOPASDFGHJLZXCVBNM':
#     f = f.replace(c, ' ')
#
# f = f.split('KK')
#
# a = []
# for c in s:
#     if ' ' not in c and 'K' not in c and fnmatch(c, '43??78???34'):
#         a += [int(c)]
# m = max(a)
#
# p = 1
# while m > 0:
#     if (m % 10) % 2 != 0
#         p *= m % 10
#     m//=10
# print(p)

# Задание 25

# for x in range(1,1000000+1):
#     s = str(x)
#     if s[:2] == '34' and '62' in s and x % 107 == 0:
#         print(x,x//107)

# from fnmatch import *
# for x in range(0,10**10,121):
#     if fnmatch(hex(x)[2:], '1?ded?ced'):
#         print(x, x//121)

# from fnmatch import *
# for x in range(0,10**8,2023):
#     if fnmatch(str(x), '11[02468]??[13579]11'):
#         print(x, x//2023)
