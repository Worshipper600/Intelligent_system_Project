
import numpy as np
import math


def select_function(fn):
    evaluation_functions = {
        'sphare': sphare,
        'Rastrigin': Rastrigin,
        'Ackley': Ackley,
        'Rosenbrock': Rosenbrock,
        'Beale': Beale,
        'Goldstein_Price': Goldstein_Price,
        'bohachevsky': bohachevsky,
        'booth': booth,
        'matyas': matyas,
        'zakharov': zakharov,
        'six_hump': six_hump,
        
    }

    if fn in evaluation_functions:
        return evaluation_functions[fn]
    else:
        raise ValueError(f"Invalid function name: {fn}")

def cosd(n):
    return np.cos(n * np.pi /180)

def sind(n):
    return np.sin(n * np.pi /180)


# 1
def sphare(x):    
    return sum(x ** 2)
# 2
def Rastrigin(x):
    N = len(x)
    result = 10 * N
    for i in x:
        result += i ** 2 - 10 * cosd(2 * math.pi * i)
    return result
# 3
def Ackley(x):
    return -20 * np.exp(-0.2 * np.sqrt(1/len(x) * sum([i ** 2 for i in x]))) - np.exp(1/len(x) *\
        sum([np.cos(i * 2 * np.pi) for i in x])) + 20 + np.exp(1)
    # return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2)))

# 4
def Rosenbrock(x):
    result = 0
    for i in range(len(x)-1):
        result += 100 * (x[i+1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return result

# 5
def Beale(x):
    return (1.5 - x[0] + x[0] * x[1]) ** 2 + (2.25 - x[0] + x[0] * (x[1] ** 2)) ** 2 + (2.625 - x[0] + x[0] * (x[1]**3)) ** 2

# 6
def Goldstein_Price(x):
    return (1+(x[0]+x[1]+1)**2*(19-14*x[0]+3*x[0]**2-14*x[1]+6*x[0]*x[1]+3*x[1]**2))*(30+(2*x[0]-3*x[1])**2*(18-32*x[0]+12*x[0]**2
    +48*x[1]-36*x[0]*x[1]+27*x[1]**2))

# 7
def bohachevsky(x):
    return x[0]**2 + 2*x[1]**2 - 0.3*cosd(3*math.pi*x[0])- 0.4*cosd(4*math.pi*x[1]) + 0.7


# 9
def booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

# 10
def matyas(x):
    return 0.26*(x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]

# 11
def zakharov(x):
    return (x[0]*2 + x[1]**2) + (0.5*x[0] + x[1])**2 + (0.5*x[0] + x[1])**4

# 12
def six_hump(x):
    return (4 - 2.1*x[0]**2 + x[0]**4/3)*x[0]**2 + x[0]*x[1] + (-4 + 4*x[1]**2)*x[1]**2

