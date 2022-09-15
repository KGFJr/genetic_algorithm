import numpy as np

def single_point_crossover(parents, crossover_p):
    if np.random.random()<crossover_p:
        b = 0.95
        l=len(parents[0])
        point=np.random.choice(l)
        parents0b = np.multiply(parents[0],b) 
        parents01_b = np.multiply(parents[0],1-b)
        
        parents1b = np.multiply(parents[1],b) 
        parents11_b = np.multiply(parents[1],1-b)
        
        child1 = parents0b + parents11_b
        child2 = parents01_b + parents1b
        
        
        #child11 = np.multiply(parents[0][:point],b) 
        #child12 = np.multiply(parents[1][:point],1-b)
        
        #child21 = np.multiply(parents[0][point:],1-b)
        #child22 = np.multiply(parents[1][point:],b)
       
        #child = np.concatenate(child1,child2)
        child=np.concatenate((child1[:point],child2[point:]))
    else:
        child=parents[0]
    return child
