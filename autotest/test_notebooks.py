

# Remove the temp directory and then create a fresh one
import os
import pytest

#these notebooks are excluded because they contain errors on purpose
_exclude_nb_list = ['use_Jupyter.ipynb','py_exploratory_comp_4.ipynb',
                    '02_strings_exercise.ipynb', '03_lists_exercise.ipynb',
                    '04_dictionaries_exercise.ipynb', '01_recap1_exercise.ipynb',
                    '01_Data inlezen met Pandas.ipynb', 
                    '01_functions_exercise.ipynb', 
                    ]

def get_notebooks(exercise_nb_dir):
    """
    These are the notebooks that should be saved without output
    
    Parameters
    ----------
    exercise_nb_dir: str
        root folder with only notebooks that should be save without output
        
    Returns
    -------
    notebook_list: list of str
        full paths of all notebooks in exercise_nb_dir
    
    """
    notebook_list = []
    for root, dirs, files in os.walk(exercise_nb_dir):
        for file in files:
            if file.endswith(".ipynb"):
                if not '.ipynb_checkpoints' in os.path.join(root, file):
                    notebook_list.append(os.path.join(root, file))
    
    return notebook_list

def run_notebook(fname):
    """
    
    Parameters
    ----------
    fname: str
        full file name of the notebooks that will be run
    
    """

    pth, fn = os.path.split(fname)

    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    from nbconvert.preprocessors import CellExecutionError
    
    with open(fname) as f:
        nb = nbformat.read(f, as_version=4)
        
    ep = ExecutePreprocessor(timeout=600)
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.split(fname)[0]}})
        msg = 'succesfully executed the notebook %s' %fname
        print(msg)
        
        return True
    except CellExecutionError:
        #raise RuntimeError('Error executing the notebook %s' % fname)
        return False
    
def test_notebooks():

    notebook_lst = get_notebooks(r'../Exercise_notebooks/Basic')
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _exclude_nb_list:
            out = run_notebook(fname)
            assert out==True, 'Error executing the notebook %s' % fname
            
    notebook_lst = get_notebooks(r'../Exercise_notebooks/On_topic')
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _exclude_nb_list:
            out=run_notebook(fname)
            assert out==True, 'Error executing the notebook %s' % fname

if __name__ == '__main__':
    test_notebooks()