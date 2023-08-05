import numpy as np 
import time 
from evalution_functions import *


def Mordified_DE(PopSize, fn, N, MaxItr, lower=-30, upper=30):

    besteval = float('inf')
    worse_eval = float('-inf')
    
    func = select_function(fn)

    # Initialization
    start = time.time()
    population = {}

    for i in range(PopSize):
        population[i] = np.random.uniform(lower, upper, N)
        SolEval = func(population[i])
        if SolEval < besteval:
            bestsol = population[i]
            besteval = SolEval
        if SolEval > worse_eval:
            worst_sol = population[i]
            worse_eval = SolEval

    for k in range(MaxItr):
        for i in range(PopSize):
            # Select two random solutions from the population that isn't i
            rnd = [j for j in range(PopSize) if j != i]
            rnd = np.random.choice(rnd, len(rnd), replace=False)
            sol2 = population[rnd[1]]
            sol3 = population[rnd[2]]

            # Mutation
            F = np.random.uniform(0, 1)
            newsol = population[i] + F * (bestsol - population[i]) + F * (bestsol - sol2)
            
            # Crossover
            crossover_sol = np.zeros(N)
            if np.mod(k, 2) == 0:
                pCR = np.random.uniform(0, 0.25)
            else:
                pCR = np.random.uniform(0.25, 0.5)
            for j in range(N):
                if np.random.uniform() <= pCR:
                    crossover_sol[j] = population[i][j]
                else:
                    crossover_sol[j] = newsol[j]
            
            # Selection
            current_eval = func(population[i])
            crossover_sol_eval = func(crossover_sol)
            
            if crossover_sol_eval < current_eval:
                population[i] = crossover_sol
                current_eval = crossover_sol_eval
            
            if current_eval < besteval:
                bestsol = population[i]
                besteval = current_eval

    end = time.time() - start
    return besteval, bestsol, end
