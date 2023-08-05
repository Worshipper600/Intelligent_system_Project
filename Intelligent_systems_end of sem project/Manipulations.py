from Modified_DE import *
from original_differencial_evolution_algorithm import *

population =[10,10,10,10,10,30,30,30,30,30,50,50,50,50,50,70,70,70,70,70,90,90,90,90,90]
iterations =[10,30,50,70,90,10,30,50,70,90,10,30,50,70,90,10,30,50,70,90,10,30,50,70,90]
function_names = ['sphare', 'Rastrigin', 'Ackley', 'Rosenbrock', 'Beale', 'Goldstein_Price', 'bohachevsky', 'booth', 'matyas', 'zakharov', 'six_hump']

for popsize in population:
    for fn in function_names:
        for N in iterations:
            best_eval, best_sol, end = Original_DE(popsize, fn, N, MaxItr=25, beta_min=0, beta_max=1, pCR=0.25, lower=-30, upper=30)
            print()
            print(f"Best evaluation {fn}:", best_eval)
            print(f"Best solution {fn}:", best_sol)
            print(f"Time{fn}:", end)
