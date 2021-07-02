import math

K = 6

lambdaa = 480 # LLEGAN 480 AUTOS POR DIA
mu = 72 # TASA DE MUERTE 1/3 DE HORA => MU = 3 POR HORA => 72 POR DIA


def first_sum(C):
    counter = 0

    for i in range(0, C+1):
        counter += (lambdaa**i) / (math.factorial(i) * (mu ** i))

    return counter


def p_n(n, C):

    # n > c

    p0 = 1 / (first_sum(C))

    return p0 * (lambdaa**n) / (math.factorial(n) * (mu ** n))


def Balance(C):

    return (365 * 480 * (1-p_n(C, C)) * 4000) - (C * 120000)



current_max = (0,0)

for j in range (1, 30):

    print(f"C = {j}; Balance = {Balance(j)}")

    if Balance(j) > current_max[1]:
        current_max = (j, Balance(j))


print(f"C Optimo = {current_max[0]}; Balance = {current_max[1]}")
