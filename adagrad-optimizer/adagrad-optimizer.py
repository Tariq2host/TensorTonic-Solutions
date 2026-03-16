import numpy as np

def adagrad_step(w, g, G, lr=0.1, eps=0.0):
    w = np.array(w, dtype=float)
    g = np.array(g, dtype=float)
    G = np.array(G, dtype=float)
    
    G += g**2                   # accumulate squared gradients
    w -= lr * g / (np.sqrt(G+ eps))  # update weights correctly
    
    return w,G