import numpy as np

def single_point_crossover(parents, crossover_p):
    if np.random.random()<crossover_p:
        b = 0.2
        l=len(parents[0])
        point=np.random.choice(l)
        child=np.concatenate((float(b)*parents[0][:point]+float(1-b)*parents[1][:point],float(1-b)*parents[0][point:]+float(b)*parents[1][point:]))
    else:
        child=parents[0]
    return child
