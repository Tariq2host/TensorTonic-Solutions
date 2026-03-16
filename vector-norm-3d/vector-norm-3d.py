import numpy as np

def vector_norm_3d(v):
    v = np.array(v)
    
    # case 1 → single vector
    if v.ndim == 1:
        s = 0
        for x in v:
            s += x**2
        return float(np.sqrt(s))   # ← return scalar
    
    # case 2 → many vectors
    result = []
    for vect in v:
        s = 0
        for x in vect:
            s += x**2
        result.append(np.sqrt(s))
    
    return np.array(result)