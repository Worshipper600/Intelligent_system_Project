import numpy as np
import time
from evalution_functions import *



def Original_DE(PopSize, fn, N, MaxItr, beta_min=0, beta_max=1, pCR=0.25, lower=-30, upper=30):
    best_eval = float('inf')
    best_sol = None

    func = select_function(fn)

    # Initialization
    start = time.time()
    population = np.random.uniform(low=lower, high=upper, size=(PopSize, N))

    for i in range(PopSize):
        sol_eval = func(population[i])
        if sol_eval < best_eval:
            best_sol = population[i]
            best_eval = sol_eval

    for k in range(MaxItr):
        for i in range(PopSize):
            rnd = np.random.choice([j for j in range(PopSize) if j != i], size=2, replace=False)
            sol2 = population[rnd[0]]
            sol3 = population[rnd[1]]

            F = np.random.uniform(beta_min, beta_max)
            newsol = population[i] + F * (best_sol - population[i]) + F * (sol2 - sol3)

            crossover_sol = np.where(np.random.uniform(size=N) <= pCR, population[i], newsol)

            current_eval = func(population[i])
            crossover_sol_eval = func(crossover_sol)

            if crossover_sol_eval < current_eval:
                population[i] = crossover_sol
                current_eval = crossover_sol_eval

            if current_eval < best_eval:
                best_sol = population[i]
                best_eval = current_eval

    end = time.time() - start
    return best_eval, best_sol, end


def Original_DE_2(PopSize, fn, N, MaxItr, beta_min=0, beta_max=1, pCR=0.25, lower=-30, upper=30):
    best_eval = float('inf')
    best_sol = None

    func = select_function(fn)

    # Initialization
    start = time.time()
    population = np.random.uniform(low=lower, high=upper, size=(PopSize, N))

    for i in range(PopSize):
        sol_eval = func(population[i])
        if sol_eval < best_eval:
            best_sol = population[i]
            best_eval = sol_eval

    for k in range(MaxItr):
        for i in range(PopSize):
            rnd = np.random.choice([j for j in range(PopSize) if j != i], size=5, replace=False)
            
            sol1 = population[rnd[0]]
            sol2 = population[rnd[1]]
            sol3 = population[rnd[2]]
            sol4 = population[rnd[3]]
            sol5 = population[rnd[4]]

            F = np.random.uniform(beta_min, beta_max)
            newsol = sol1 + F * (sol2 - sol3) + F * (sol4 - sol5)

            crossover_sol = np.where(np.random.uniform(size=N) <= pCR, population[i], newsol)

            current_eval = func(population[i])
            crossover_sol_eval = func(crossover_sol)

            if crossover_sol_eval < current_eval:
                population[i] = crossover_sol
                current_eval = crossover_sol_eval

            if current_eval < best_eval:
                best_sol = population[i]
                best_eval = current_eval

    end = time.time() - start
    return best_eval, best_sol, end

def Original_DE_3(PopSize, fn, N, MaxItr, beta_min=0, beta_max=1, pCR=0.25, lower=-30, upper=30):
    best_eval = float('inf')
    best_sol = None

    func = select_function(fn)

    # Initialization
    start = time.time()
    population = np.random.uniform(low=lower, high=upper, size=(PopSize, N))

    for i in range(PopSize):
        sol_eval = func(population[i])
        if sol_eval < best_eval:
            best_sol = population[i]
            best_eval = sol_eval

    for k in range(MaxItr):
        for i in range(PopSize):
            rnd = np.random.choice([j for j in range(PopSize) if j != i], size=4, replace=False)
            
            sol1 = population[rnd[0]]
            sol2 = population[rnd[1]]
            sol3 = population[rnd[2]]
            sol4 = population[rnd[3]]
#             sol5 = population[rnd[4]]

            F = np.random.uniform(beta_min, beta_max)
            newsol = best_sol + F * (sol1 - sol2) + F * (sol3 - sol4)

            crossover_sol = np.where(np.random.uniform(size=N) <= pCR, population[i], newsol)

            current_eval = func(population[i])
            crossover_sol_eval = func(crossover_sol)

            if crossover_sol_eval < current_eval:
                population[i] = crossover_sol
                current_eval = crossover_sol_eval

            if current_eval < best_eval:
                best_sol = population[i]
                best_eval = current_eval

    end = time.time() - start
    return best_eval, best_sol, end
