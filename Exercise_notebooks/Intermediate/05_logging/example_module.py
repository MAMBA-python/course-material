import numbers

import logging 
logger = logging.getLogger(__name__)

def check_if_nummerical(a):

    logger.info('running check_if_nummerical function inside the example_module')
    
    return isinstance(a, numbers.Number)
    
