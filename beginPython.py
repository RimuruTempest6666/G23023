#print("Hello,world!")
import math

#Begin1. Дана сторона квадрата a. Найти его периметр P = 4·a
##a = 8
##P = 4 * a
##print('P = ',  P)


#Begin2. Дана сторона квадрата a. Найти его площадь S = a

##print('Введите целое число - сторону квадрата')
##a = int(input())
##S = a * a
##print('S = ', S)


#Begin3.Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
##print('Введите целые числа - стороны прямоуг')
##a = int(input())
##b = int(input())
##S = a*b
##P = 2*(a + b)
##print('S = ', S)
##print('P = ', P)


#Begin4.Дан диаметр окружности d. Найти ее длину L = π·d. В качестве значения π использовать 3.14.
##print('Введите целое число')
##d = int(input())                               
##L = 3.14*d
##print('L = ', L)


#Begin5.Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
##print('Введите целое число')
##a = int(input())
##V = a*a*a
##S = 6*a*a
##print('V = ', V)
##print('S = ', S)


#Begin6.Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c).
##print('Введите целое число')
##a = int(input())
##b = int(input())
##c = int(input())
##V = a*b*c
##S = 2*(a*b + b*c + a*c)
##print('V = ', V)
##print('S = ', S)


#Begin7.Найти длину окружности L и площадь круга S заданного радиуса R:L = 2·π·R, S = π·R2
##print('Введите целое число')
##R = int(input())
##L = 3.14*R*2
##S = 3.14* R**2
##print('S = ', S)
##print('L = ', L)



#Begin8.Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2.
##print('Введите целое число')
##a = int(input())
##b = int(input())
##M = (a + b)/2
##print('M = ', M)


#Begin9.Даны два неотрицательных числа a и b. Найти их среднее геометрическое, то есть квадратный корень из их произведения: √a·b.
##print('Введите целое число')
##a = int(input())
##b = int(input())
##c = math.sqrt(a*b)
##print('c = ', c)


#Begin10.Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
##print('Введите целое число')
##a = int(input())
##b = int(input())
##c = a+b
##k = a-b
##g = a*b
##h = a**2/b**2
##print('c = ', c)
##print('k = ', k)
##print('g = ', g)
##print('h = ', h)


#Begin11.Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.
##a = int(input())
##b = int(input())
##math.fabs(a)
##c = math.fabs(a) +math.fabs(b)
##k =math.fabs(a) -math.fabs(b)
##g =math.fabs(a) *math.fabs(b)
##h =math.fabs(a) /math.fabs(b)
##print('c = ', c)
##print('k = ', k)
##print('g = ', g)
##print('h = ', h)


#Begin12.Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P:c =√a2 + b2, P = a + b + c.
##a = int(input())
##b = int(input())
##c =math.sqrt(a**2+b**2)
##P = a + b + c
##print('c = ', c)
##print('P = ', P)


#Begin13.Даны два круга с общим центром и радиусами R1 и R2 (R1 > R2).Найти площади этих кругов S1 и S2, а также площадь S3 кольца, внешний радиус которого равен R1,
#а внутренний радиус равен R2:S1 = π·(R1)2, S2 = π·(R2)2, S3 = S1 - S2.
##R1 = int(input())
##R2 = int(input())
##S1 = 3.14*R1*2
##S2 = 3.14*R2*2
##S3 = S1 - S2
##print('S1 = ', S1)
##print('S2 = ', S2)
##print('S3 = ', S3)


#Begin14◦. Дана длина L окружности. Найти ее радиус R и площадь S круга, ограниченного этой окружностью, учитывая, что L = 2·π·R, S = π·R2. В качестве значения π использовать 3.14.
#L = int(input())
#R = L/(3.14*2)
#S = 3.14*R**2
#print('R = ', R)
#print('S = ', S)


#Begin15◦. Дана площадь S круга. Найти его диаметр D и длину L окружности, ограничивающей этот круг, учитывая, что L = 2·π·R, S = π·R2. В качестве значения π использовать 3.14.
#S = int(input())
#D = math.sqrt((4*S)/3.14)
#L = D*3.14
#print('D = ', D)
#print('L = ', L)


#Begin16◦. Найти расстояние между двумя точками с заданными координата- ми x1 и x2 на числовой оси: |x2 − x1|.
#x1 = int(input())
#x2 = int(input())
#C = math.fabs(x1-x2)
#print('C = ', C)


#Begin17◦. Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
#A = int(input())
#B = int(input())
#C = int(input())
#G = math.fabs(A-C)+math.fabs(B-C)
#print('G = ', G)


#Begin18◦. Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.
#print('Точка C расположена между точками A и B.')
#A = int(input())
#B = int(input())
#C = int(input())
#if A<C<B or A>C>B:
#        G = math.fabs(A-C)*math.fabs(B-C)
#        print('G = ', G)
#else: print('Читать научись!!')

#Begin19◦. Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного прямоугольника.
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#L = math.fabs(x2-x1)
#W = math.fabs(y2-y1)
#P = (L+W)*2
#S = L*W
#print('P = ', P)
#print('S = ', S)


#Begin20◦. Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости. Расстояние вычисляется по формуле √(x2 − x1)2 + (y2 − y1)2.
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#C = math.sqrt(math.fabs(x2-x1)**2+math.fabs(y2-y1)**2)
#print('C = ', C)


#Begin21◦. Даны координаты трех вершин треугольника: (x1, y1), (x2, y2), (x3, y3).Найти его периметр и площадь, используя формулу для расстояния между двумя точками на плоскости (см. задание Begin20). Для нахождения площади треугольника со сторонами a, b, c использовать формулу Герона: S = √p·(p − a)·(p − b)·(p − c),где p = (a + b + c)/2 — полупериметр.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = math.sqrt(math.fabs(x2-x1)**2+math.fabs(y2-y1)**2)
b = math.sqrt(math.fabs(x3-x2)**2+math.fabs(y3-y2)**2)
c = math.sqrt(math.fabs(x1-x3)**2+math.fabs(y1-y3)**2)
p = (a + b + c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('S = ', S)