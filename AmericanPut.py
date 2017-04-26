import math
import numpy


# noinspection PyPep8Naming
def american_put(S, K, r, sigma, T, n):

    u = math.exp(sigma * math.sqrt(T / n))
    d = math.exp(-sigma * math.sqrt(T / n))

    R = math.exp(r * T / n)
    p = (R - d) / (u - d)

    P = numpy.zeros((n + 1, n + 1))

    for i in range(0, n+1):
        P[n][i] = K - (S * math.pow(u, n - i) * math.pow(d, i))
        P[n][i] = P[n][i] if P[n][i] > 0 else 0

    for j in range(n - 1, -1, -1):
        for i in range(0, j+1):
            P[j][i] = ((p * P[j + 1][i]) + ((1 - p) * P[j + 1][i + 1])) / R

    print("Put value = ", P[0][0])
    print("delta = ", (P[1][0] - P[1][1])/(S*u - S*d))


american_put(100, 105, 0.05, 0.3, 0.75, 300)
