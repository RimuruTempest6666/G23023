#dz


#Дележ яблок - n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Входные данные: Программа получает на вход числа n и k  - целые, положительные, не превышают 10000. Выходные данные: Выведите ответ на задачу.
#n = int(input("n = "))
#k = int(input("k = "))
#if n<10000 and k<10000:
#    T = k//n
#    print('T = ', T)
#else:
#    print('Net')


#Дележ яблок - n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок останется в корзинке? Входные данные: Программа получает на вход числа n и k  - целые, положительные, не превышают 10000. Выходные данные: Выведите ответ на задачу.
#n = int(input("n = "))
#k = int(input("k = "))
#if n<10000 and k<10000:
#    T = k%n
#    print('T = ', T)
#else:
#    print('Net')


#Сумма цифр - Дано трехзначное число. Найдите сумму его цифр.Входные данные: Вводится целое положительное число. Гарантируется, что оно соответствует условию задачи.Выходные данные: Выведите ответ на задачу.
N = int(input("N = "))
if 99<N<1000:
    d1 = N%10
    N = N//10
    d10 = N%10
    N = N//10
    d100 = N%10
    T = d1 + d10 + d100
    print('T = ', T)
else:
    print('Net')





