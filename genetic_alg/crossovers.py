import numpy as np

def single_point_crossover(parents, crossover_p):
    if np.random.random()<crossover_p:
        b = 0.2
        l=len(parents[0])
        point=np.random.choice(l)
        child11 = np.multiply(parents[0],b) 
        child12 = np.multiply(parents[1],1-b)
        
        child21 = np.multiply(parents[0],1-b)
        child22 = np.multiply(parents[1],b)
        
        child111 = child11 + child21
        child222 = child12 + child12
        
        
        #child11 = np.multiply(parents[0][:point],b) 
        #child12 = np.multiply(parents[1][:point],1-b)
        
        #child21 = np.multiply(parents[0][point:],1-b)
        #child22 = np.multiply(parents[1][point:],b)
       
        #child = np.concatenate(child1,child2)
        child=np.concatenate((child111 [:point],child222[point:]))
    else:
        child=parents[0]
    return child
