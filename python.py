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
#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#x3 = int(input())
#y3 = int(input())
#a = math.sqrt(math.fabs(x2-x1)**2+math.fabs(y2-y1)**2)
#b = math.sqrt(math.fabs(x3-x2)**2+math.fabs(y3-y2)**2)
#c = math.sqrt(math.fabs(x1-x3)**2+math.fabs(y1-y3)**2)
#p = (a + b + c)/2
#S = math.sqrt(p*(p-a)*(p-b)*(p-c))
#print('a = ', a)
#print('b = ', b)
#print('c = ', c)
#print('S = ', S)


#Bonus kalculator
#while True: print(eval(input('>>>')))


#Begin22.Поменять местами содержимое переменных A и B и вывести новые значения A и B.
##A = int(input())
##B = int(input())
##C = A
##A = B
##B = C
##print('A = ', A)
##print('B = ', B)


#Begin23.Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A,B, C.
##A = int(input())
##B = int(input())
##C = int(input())
##G = A
##A = B
##B = C
##C = G
##print('A = ', A)
##print('B = ', B)
##print('C = ', C)


#Begin24.Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A,B, C.
##A = int(input())
##B = int(input())
##C = int(input())
##G = A
##A = C
##C = B
##B = G
##print('A = ', A)
##print('B = ', B)
##print('C = ', C)


#Begin25.Найти значение функции y = 3x6 − 6x2 − 7 при данном значении x
##x = int(input())
##y = 3*x**6-6*x**2-7
##print('y = ', y)


#Begin26.Найти значение функции y = 4(x−3)6 − 7(x−3)3 + 2 при данном значении x.
##x = int(input())
##y = 4*(x-3)**6-7*(x-3)**3 + 2
##print('y = ', y)


#Begin27.Дано число A. Вычислить A8, используя вспомогательную переменную и три операции умножения. Для этого последовательно находить A2,A4, A8. Вывести все найденные степени числа A.
##A = int(input())
##G = A**2
##H = G**2
##J = H**2
##print('G = ', G)
##print('H = ', H)
##print('J = ', J)


#Begin28.Дано число A. Вычислить A15, используя две вспомогательные переменные и пять операций умножения. Для этого последовательно находить A2, A3, A5, A10, A15. Вывести все найденные степени числа A.
##A = int(input())
##G = A**2
##H = A**3
##J = A**5
##K = A**10
##L = A**15
##print('G = ', G)
##print('H = ', H)
##print('J = ', J)
##print('K = ', K)
##print('L = ', L)


#Begin29.Дано значение угла α в градусах (0 < α < 360). Определить значение этого же угла в радианах, учитывая, что 180◦ = π радианов. В качестве значения π использовать 3.14.
##print('0<a<360')
##a = int(input())
##if 0<a<360:
##    F = a*(3.14/180)
##    print('F = ', F)
##else:
##    print('Читать научись!!')


#Begin30.Дано значение угла α в радианах (0 < α < 2·π). Определить значениеэтого же угла в градусах, учитывая, что 180◦ = π радианов. В качестве значения π использовать 3.14.
##print('0<a<6.28')
##a = int(input())
##if 0<a<6.28:
##    F = a/(3.14/180)
##    print('F = ', F)
##else:
##    print('Читать научись!!')


#Begin31.Дано значение температуры T в градусах Фаренгейта. Определить значение этой же температуры в градусах Цельсия. Температура по Цельсию Tc и температура по Фаренгейту Tf связаны следующим соотношением:Tc = (Tf − 32)·5/9.
##Tf = int(input())
##Tc = (Tf-32)*(5/9)
##print('Tc = ', Tc)


#Begin32.Дано значение температуры T в градусах Цельсия. Определить значение этой же температуры в градусах Фаренгейта. Температура по Цельсию Tc и температура по Фаренгейту Tf связаны следующим соотношением:Tc = (Tf − 32)·5/9.
##Tc = int(input())
##Tf = Tc/(5/9)+32
##print('Tf = ', Tf)


#Integer1.Дано расстояние L в сантиметрах. Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).
##L = int(input("Введите кол-во см "))
##meters = L//100
##print('Полных метров ', meters)


#Integer2.Дана масса M в килограммах. Используя операцию деления нацело,найти количество полных тонн в ней (1 тонна = 1000 кг).
##M = int(input("Введите кол-во  "))
##T = M//1000
##print('T = ', T)


#Integer3.Дан размер файла в байтах. Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл(1 килобайт = 1024 байта).
##M = int(input("Введите кол-во  "))
##T = M//1024
##print('T = ', T)


#Integer4.Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B(без наложений). Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
##A = int(input("A = "))
##B = int(input("B = "))
##if A>B:
##    T = A//B
##    print('T = ', T)
##else:
##     print('Net')   


#Integer5.Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.
##A = int(input("A = "))
##B = int(input("B = "))
##if A>B:
##    T = A%B
##    print('T = ', T)
##else:
##     print('Net')  


#Integer6◦Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию деления нацело, для нахождения единиц — операцию взятия остатка от деления
##N = int(input("N = "))
##if 9<N<100:
##    digit10 = N//10
##    digit1 = N%10
##    print('digit10 = ',digit10 )
##    print('digit1 = ',digit1 )
##else:
##    print('Net')


#дано трехзначное число. его цифры по отдельности
##N = int(input("N = "))
##if 99<N<1000:
##    digit1 = N%10
##    print('digit1 = ',digit1 )
##    N = N//10
##    digit10 = N%10
##    print('digit10 = ',digit10 )
##    N = N//10
##    digit100 = N%10
##    print('digit100 = ',digit100 )
##    N = N//10
##else:
##    print('Net')


#Integer7.Дано двузначное число. Найти сумму и произведение его цифр.
##N = int(input("N = "))
##if 9<N<100:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    T = d1+d10
##    G = d1*d10
##    print('T = ', T)
##    print('G = ', G)
##else:
##    print('Net')


#Integer8.Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
##N = int(input("N = "))
##if 9<N<100:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    T = d1*10+d10
##    print('T = ', T)
##else:
##    print('Net')


#Integer9◦Дано трехзначное число. Используя одну операцию деления нацело,вывести первую цифру данного числа (сотни).
##N = int(input("N = "))
##if 99<N<1000:
##    T = N//100
##    print('T = ', T)
##else:
##    print('Net')


#Integer10◦Дано трехзначное число. Вывести вначале его последнюю цифру(единицы), а затем — его среднюю цифру (десятки).
##N = int(input("N = "))
##if 99<N<1000:
##    digit1 = N%10
##    print('digit1 = ',digit1 )
##    N = N//10
##    digit10 = N%10
##    print('digit10 = ',digit10 )
##else:
##    print('Net')


#Integer11◦Дано трехзначное число. Найти сумму и произведение его цифр.
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d1+d10+d100
##    G = d1*d10*d100
##    print('T = ', T)
##    print('G = ', G)
##else:
##    print('Net')


#Integer12.Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d100+d10*10+d1*100
##    print('T = ', T)
##else:
##    print('Net')


#Integer13◦Дано трехзначное число. В нем зачеркнули первую слева цифру и приписали ее справа. Вывести полученное число.
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d10*100+d1*10+d100
##    print('T = ', T)
##else:
##    print('Net')


#Integer14◦Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d1*100+d100*10+d10
##    print('T = ', T)
##else:
##    print('Net')


#Integer15◦Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213).
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d10*100+d100*10+d1
##    print('T = ', T)
##else:
##    print('Net')


#Integer16◦Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).
##N = int(input("N = "))
##if 99<N<1000:
##    d1 = N%10
##    N = N//10
##    d10 = N%10
##    N = N//10
##    d100 = N%10
##    T = d100*100+d1*10+d10
##    print('T = ', T)
##else:
##    print('Net')


#Integer17◦Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру,соответствующую разряду сотен в записи этого числа
##N = int(input("N = "))
##if 999<N:
##    H = N//100
##    T = H%10
##    print('T = ', T)
##else:
##    print('Net')


#Integer18◦Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру,соответствующую разряду тысяч в записи этого числа.
##N = int(input("N = "))
##if 999<N:
##    H = N//1000
##    T = H%10
##    print('T = ', T)
##else:
##    print('Net')

















