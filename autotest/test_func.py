# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:18:44 2020

@author: onno_
"""


# Remove the temp directory and then create a fresh one
import os
from subprocess import Popen, PIPE
import nbformat

def run_notebook(fdir, fname, clearoutput=True, timeout=60):
    """ Run a single notebook and add the process to a list of active
    processes.
    
    Parameters
    ----------
    fname: str
        full file name of the notebooks that will be run
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
    clearoutput : bool, optional
        If True the output cells are cleared after running the notebook
    timeout : int, optional
        if it takes more seconds than this to run a cell an error is raised.
        
    Returns
    -------
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
    """
    
    print('running --> {}'.format(fname))
    
    cmd_args = f'jupyter nbconvert --ExecutePreprocessor.timeout={timeout} --to notebook --execute "{fname}" --output "{fname}"'
    p = Popen(cmd_args, stdout=PIPE, stderr=PIPE, encoding='utf8', cwd=fdir)
    assert p.wait()==0
    
    if clearoutput:
        clear_output(fdir, fname)
    
    return 0

def clear_output(fdir, fname):
    """ clear the output of a notebook. This should be done to reduce size
    and improve the speed of the git stuff.
    
    Parameters
    ----------
    fname: str
        full path of the notebook which is cleared of output
    
    """
    fpath = os.path.join(fdir, fname)
    nb = nbformat.read(fpath, nbformat.NO_CONVERT)
    
    for cell in nb.cells:
        if hasattr(cell, "outputs"):
            cell.outputs = []
        if hasattr(cell, "execution_count"):
            cell["execution_count"] = None
            
    nbformat.write(nb, fpath)
    print('cleared output --> {}'.format(os.path.split(fname)[-1]))