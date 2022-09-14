import numpy as np

def single_point_crossover(parents, crossover_p):
    if np.random.random()<crossover_p:
        b = 0.2
        l=len(parents[0])
        point=np.random.choice(l)
        child1 = np.multiply(parents[0][:point],b) + np.multiply(parents[1][:point],1-b)
        #float(b)*parents[0][:point]+float(1-b)*parents[1][:point]
        child2 = np.multiply(parents[0][point:],1-b) + np.multiply(parents[1][point:],b)
        #float(1-b)*parents[0][point:]+float(b)*parents[1][point:]
        child = np.concatenate(child1,child2)
        # child=np.concatenate((parents[0][:point],parents[1][point:]))
    else:
        child=parents[0]
    #print(parents[0])
    return child
