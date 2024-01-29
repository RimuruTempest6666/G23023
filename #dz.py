#dzz

#Array20.ДанмассивразмераN ицелыечислаK иL(1≤K ≤L≤N).Найти сумму элементов массива с номерами от K до L включительно.
#print("1 <= K <= L <= N")
#N = int(input("N= "))
#K = int(input("K= "))
#L = int(input("L= "))
#lst = []
#for i in range(N):
#    lst.append(randint(-100,100))
#if 1 <= K <= L <= N:
#    g = sum(lst[K-1:L])
#    print(g)
#else:
#    print("net")


#Array21. Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти среднее арифметическое элементов массива с номерами от K до L включительно.
#print("1 <= K <= L <= N")
#N = int(input("N= "))
#K = int(input("K= "))
#L = int(input("L= "))
#lst = []
#for i in range(N):
#    lst.append(randint(-100,100))
#if 1 <= K <= L <= N:
#    g = sum(lst[K-1:L])
#    h = len(lst[K-1:L])
#    j = g/h
#    print(j)
#else:
#    print("net")



#Array22. Дан массив размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти сумму всех элементов массива, кроме элементов с номерами от K до L включительно.
#print("1 <= K <= L <= N")
#N = int(input("N= "))
#K = int(input("K= "))
#L = int(input("L= "))
#lst = []
#for i in range(N):
#    lst.append(randint(-100,100))
#print(lst)
#if 1 <= K <= L <= N:
#    lst[K-1:L]=[]
#    g = sum(lst)
#    print(g)
#else:
#    print("net")


#dzz2

#Proc16. Описать функцию Sign(X) целого типа, возвращающую для вещественного числа X следующие значения: −1, еслиX <0; 0, еслиX =0; 1, еслиX >0. С помощью этой функции найти значение выражения Sign(A) + Sign(B) для данных вещественных чисел A и B.

def Sign(x):
    g = None
    if x<0:
        g=-1
    elif x==0:
        g=0
    elif x>0:
        g=1
    return g

#a = int(input("a = "))
#b = int(input("b = "))

#print(Sign(a)+Sign(b))


#Proc17. Описать функцию RootsCount(A, B, C) целого типа, определяющую количество корней квадратного уравнения A·x2 + B·x + C = 0 (A, B, C — вещественные параметры, A ̸= 0). С ее помощью найти количество корней для каждого из трех квадратных уравнений с данными коэффициентами. Количество корней определять по значению дискриминанта:D = B2 − 4·A·C.
def RootsCount(a, b, c):
    if a != 0:
        g=None
        D = b**2-4*a*c
        if D<0:
            g = 0
        elif D==0:
            g=1
        elif D>0:
            g=2
        return g

#for i in range(3):
#    a = int(input("a = "))
#    b = int(input("b = "))
#    c = int(input("c = "))
#    print(RootsCount(a, b, c))


#Proc18. Описать функцию CircleS(R) вещественного типа, находящую площадь круга радиуса R (R — вещественное). С помощью этой функции найти площади трех кругов с данными радиусами. Площадь круга ради- уса R вычисляется по формуле S = π·R2. В качестве значения π использо- вать 3.14.
def CircleS(R):
    S = 3.14*R
    return S

#for i in range(3):
#    R = int(input("R = "))
#    print(CircleS(R))