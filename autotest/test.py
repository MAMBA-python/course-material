

# Remove the temp directory and then create a fresh one
import os

#these notebooks are excluded because they contain errors on purpose
_exclude_nb_list = ['use_Jupyter.ipynb',]

def get_exercise_notebooks(exercise_nb_dir):
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

def run_notebook_no_output(fname):
    """
    
    Parameters
    ----------
    fname: str
        full file name of the notebooks that will be run
    
    """
    # run autotest on each notebook
    pth, fn = os.path.split(fname)
#    testdir = r'tests'
#    cmd = 'jupyter ' + 'nbconvert ' + \
#          '--to ' + 'notebook ' + \
#          '--execute ' + '{} '.format(fname)
#    ival = os.system(cmd)
#    assert ival == 0, 'could not run {}'.format(fname)
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
    except CellExecutionError:
        msg = 'Error executing the notebook %s' % fname
        print(msg)
    
    
def test_notebooks():

    for dpth in [faqdir, nbdir]:
        # get list of notebooks to run
        files = get_Notebooks(dpth)

        # run each notebook
        for fn in files:
            yield run_notebook, dpth, fn


if __name__ == '__main__':
    
    notebook_lst = get_exercise_notebooks(r'../Exercise_notebooks/Basic')
    for fname in notebook_lst[:3]:
        if os.path.split(fname)[-1] not in _exclude_nb_list:
            run_notebook_no_output(fname)