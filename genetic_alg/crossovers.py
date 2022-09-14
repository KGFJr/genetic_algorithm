import numpy as np

def single_point_avg_crossover(parents, crossover_p):
    if np.random.random()<crossover_p:
        b = 0.2
        l=len(parents[0])
        point=np.random.choice(l)
        child=np.concatenate((
            (b)*parents[0][:point]+(1-b)*parents[1][:point],
            (1-b)*parents[0][point:]+(b)*parents[1][point:]))
    else:
        child=parents[0]
    return child
