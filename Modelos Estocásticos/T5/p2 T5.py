import math

K = 15
# C = 2

lambdaa = 10 # llegan 10 clientes en intervalo de 1 hora => Poisson(lambda = 10)
mu = 6 # Tiempo de servicio promedio:  10 minutos  = 1/6 hora => media = 1/mu  => exp(mu = 6)

costo_encola = 10
costo_cajero = 15


def first_sum(C):
    counter = 0

    for i in range(0, C+1):
        to_add = (lambdaa**i) / (math.factorial(i) * (mu ** i))
        counter += to_add

    return counter


def second_sum(C):

    counter = 0

    for j in range(C + 1, K+1):
        counter += ((1 / (math.factorial(C) * (C**(j - C)))) * ((lambdaa / mu) ** j))

    return counter


def p0(C):
    return (1/(first_sum(C)+second_sum(C)))


def p_n(n, c):

    return p0(c) * ((1 / (math.factorial(c) * (c**(n - c)))) * ((lambdaa / mu) ** n))


def Lq(C, K):

    counter = 0

    # Sumatoria de C+1 a K
    for j in range(C + 1, K + 1):
        counter += (j - C) * p_n(j, C)

    return counter


for C in range(1, K):

    P0 = 1 / (first_sum(C) + second_sum(C))

    costo_total = C * costo_cajero + Lq(C, K) * costo_encola

    print(f'C = {C}, Lq = {Lq(C,K)}, Costo total = {costo_total}')



