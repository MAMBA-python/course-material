def my_add(argument1, argument2):
    """
    adds two input arguments.
    
    Parameters
    ----------
    argument1 : int, float, str
        input argument 1
    argument2 : int, float, str
        input arguement 2
        
    Returns
    -------
    results : int, float or str
        the two added input arguments   
    """
    result = argument1 + argument2
    return result
    
print(my_add(2,4))