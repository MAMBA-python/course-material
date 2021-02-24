import numpy as np

def column_mean(arr):
    """ berekent het gemiddelde van elke kolom in een 2d array
    

    Parameters
    ----------
    arr : np.array
        2 dimensionale numpy array.

    Returns
    -------
    mean_col : np.array
        1 dimensionale numpy array met gemiddelde per kolom.

    """
    
    mean_col = np.mean(arr, axis=0)
    
    return mean_col