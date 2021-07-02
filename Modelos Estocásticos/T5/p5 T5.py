import math

K = 6

lambdaa = 4 # LLEGAN 4 LLAMADAS POR MINUTO
mu = 0.5 # TIEMPO ATENCION CADA LLAMADA : 2 MINS


def first_sum(C):
    counter = 0

    for i in range(0, C+1):
        counter += (lambdaa**i) / (math.factorial(i) * (mu ** i))

    return counter


def p_n(n, C):

    # n > c

    p0 = 1 / (first_sum(C))

    return p0 * (lambdaa**n) / (math.factorial(n) * (mu ** n))

print(1 / (first_sum(1)))


for j in range (1, 20):
    for i in range(0, 20):

        if i==j:
            print(f"C = {j}; P{i} = {p_n(i, j)}, Perdidos = {p_n(i, j) * (lambdaa)}")