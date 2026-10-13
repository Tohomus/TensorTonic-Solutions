import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    arr=np.asarray(x,dtype=float)

    result=1/(1+np.exp(-arr))

    return result