

# Remove the temp directory and then create a fresh one
import os
import pytest
import sys
from subprocess import Popen, PIPE
import logging
import nbformat

#these notebooks are excluded because they contain errors on purpose
_exclude_nb_list = ['use_Jupyter.ipynb','py_exploratory_comp_4.ipynb',
					'01_numbers_exercise.ipynb',
                    '02_strings_exercise.ipynb', '03_lists_exercise.ipynb',
                    '04_dictionaries_exercise.ipynb', '01_recap1_exercise.ipynb',
                    '01_data_inlezen_met_pandas_dutch.ipynb', 
                    '01_functions_exercise.ipynb', 
                    '02_py_exploratory_comp_4.ipynb',
                    '02_py_exploratory_comp_4_sol.ipynb',
                    '03-func.ipynb',
                    '02_classes_exercise.ipynb',
                    '01_file_io_exercise.ipynb',
                    '01-IntroDBWorkshop.ipynb',
                    '02_common_pitfalls.ipynb',
                    '01-errors.ipynb',
                    '02_exceptions_exercise.ipynb',
                    '03_py_exploratory_comp_7.ipynb',
                    '03_py_exploratory_comp_7_sol.ipynb',
                    '01-testing1_exercise.ipynb',
                    '02-testing2_exercise.ipynb',
                    '03-defensive.ipynb',
                    '01_datetime_exercise.ipynb',
                    '01_conditionals_exercise.ipynb',
                    '02-cond.ipynb',
                    '03_for_loops_exercise.ipynb',
                    '04-loop.ipynb',
                    '01-debugging_exercise.ipynb',
                    '09 - Geographic Plots.ipynb',
                    ]

_keep_output_list = ['02_py_exploratory_comp_4_sol.ipynb']

#make projectdir accessible inside this script
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
os.chdir(TEST_DIR)

try:
    os.remove('tests.log')
except FileNotFoundError:
    pass
except PermissionError:
    pass

logging.basicConfig(filename='tests.log',level=logging.DEBUG)

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
    for root, dirs, files in os.walk(os.path.join(sys.path[0], 
                                                  exercise_nb_dir)):
        for file in files:
            if file.endswith(".ipynb"):
                if not '.ipynb_checkpoints' in os.path.join(root, file):
                    notebook_list.append(os.path.join(root, file))
    
    return notebook_list

def run_notebook(fname, active_processes):
    """ Run a single notebook and add the process to a list of active
    processes.
    
    Parameters
    ----------
    fname: str
        full file name of the notebooks that will be run
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
        
    Returns
    -------
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
    """
    file_l = os.path.split(fname)
    
    print('running --> {}'.format(file_l[-1]))
    
    cmd_args = 'jupyter nbconvert --ExecutePreprocessor.timeout=1200 --to notebook --execute "{}" --output "{}"'.format(file_l[1], file_l[1])
    p = Popen(cmd_args, stdout=PIPE, stderr=PIPE, encoding='utf8', cwd=file_l[0])
    active_processes.append(p)
    
    return active_processes

def clear_output(fname):
    """ clear the output of a notebook. This should be done to reduce size
    and improve the speed of the git stuff.
    
    Parameters
    ----------
    fname: str
        full path of the notebook which is cleared of output
    
    """
    
    nb = nbformat.read(fname, nbformat.NO_CONVERT)
    
    for cell in nb.cells:
        if hasattr(cell, "outputs"):
            cell.outputs = []
        if hasattr(cell, "execution_count"):
            cell["execution_count"] = None
            
    nbformat.write(nb, fname)
    print('cleared output --> {}'.format(os.path.split(fname)[-1]))
    
    
def check_notebook(active_processes, max_processes=3):
    """ When there are as many or more processes activate than max_processes
    this function will wait for the first process to finish. It then logs the
    result of this process.
    
    Parameters
    ----------
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
    max_processes : int
        number of notebooks that can run simultaneously
        
    Returns
    -------
    active_processes : list of SubprocessPopen
        active processes where each process is running one jupyter notebook
    """
    
    if len(active_processes) >= max_processes:
        p = active_processes.pop(0)
        output, error = p.communicate()
        
        if p.returncode == 0:
            print('succesfully finished {}'.format(p.args.split('output ')[-1]))
            logging.info('succesfully finished {}'.format(p.args.split('output ')[-1]))
        else:
            print('could not run {}'.format(p.args.split('output ')[-1]))
            #print('error message:\n\n{}\n\n'.format(error))
            logging.error('could not run {}'.format(p.args.split('output ')[-1]))
            logging.error('error message:\n\n{}\n\n'.format(error))
    return active_processes
    

    
def test_notebooks():
    """ Run all notebooks in the Basic and On_topic directory
    
    Parameters
    ----------
    
    Returns
    -------
    
    """
    # run notebooks Basic 
    notebook_lst = get_notebooks(r'Exercise_notebooks/Basic')
    print('testing {} notebooks'.format(len(notebook_lst)))
    assert len(notebook_lst)!=0, 'No notebooks to be tested'
    
    
    active_processes = []
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _exclude_nb_list:
            active_processes = run_notebook(fname, active_processes)
            active_processes = check_notebook(active_processes)

    # wait for last process to finish
    for p in range(len(active_processes)):
        active_processes = check_notebook(active_processes, max_processes=0)
    
    # clear output
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _keep_output_list:
            clear_output(fname)
    
    # run notebooks On Topic       
    notebook_lst = get_notebooks(r'Exercise_notebooks/On_topic')
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _exclude_nb_list:
            active_processes = run_notebook(fname, active_processes)
            active_processes = check_notebook(active_processes)
            
    # wait for last process to finish
    for p in range(len(active_processes)):
        active_processes = check_notebook(active_processes, max_processes=0)
       
    # clear output
    for fname in notebook_lst:
        if os.path.split(fname)[-1] not in _keep_output_list:
            clear_output(fname)

#if __name__ == '__main__':
#    test_notebooks()