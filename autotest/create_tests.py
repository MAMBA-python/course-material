# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:04:21 2020

@author: onno_
"""

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
                    '10 - Exporting and Embedding.ipynb',
                    'how to run executables in python.ipynb',
                    'Webscraping-BeautifulSoup.ipynb',
                    ]

_keep_output_list = ['02_py_exploratory_comp_4_sol.ipynb']

#make projectdir accessible inside this script
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)
os.chdir(TEST_DIR)


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
            if file.endswith(".ipynb") and (not '.ipynb_checkpoints' in os.path.join(root, file)):
                if file not in _exclude_nb_list:
                    notebook_path = os.path.join(root, file)
                    notebook_rel_path = notebook_path.split(exercise_nb_dir)[-1]
                    notebook_list.append(notebook_rel_path)
    
    return notebook_list

def create_test_modules(nbdir, name):
    """ create python script test_{name}.py with test functions for all
    notebooks that are in the nbdir and not in the _exclude_nb_list
    

    Parameters
    ----------
    nbdir : str
        relative path to the notebook directory.
    name : str
        name of the python script test.

    """
    
    notebook_lst = get_notebooks(nbdir)
    
    with open(f'test_{name}.py', 'w') as f:
        f.write(_create_test_module_heading(nbdir))
    
    nb_names = []
    for nb_path in notebook_lst:
        # check if output has to be cleared
        if os.path.split(nb_path)[-1] in _keep_output_list:
            clearoutput=False
        else:
            clearoutput=True
        
        # get proper name for function
        nb_name = os.path.splitext(os.path.split(nb_path)[-1])[0]
        nb_name = nb_name.replace(' ','_').replace('-','_')
        while nb_name in nb_names:
            nb_name += '_'
        nb_names.append(nb_name)
        
        # write function
        with open(f'test_{name}.py', 'a') as f:
            f.write(_create_test_func(nb_name, nb_path, clearoutput))

    

def _create_test_module_heading(nbdir):
    """ create str with header of the test module
    

    Parameters
    ----------
    nbdir : str
        relative path to the notebook directory.

    Returns
    -------
    heading : str
        header of the test module

    """
    heading = 'import os\n'\
              'import sys\n'\
              'import test_func as tf\n\n'\
              '#make projectdir accessible inside this script\n'\
               f'nb_dir = {os.path.split(nbdir)}\n'\
              
    return heading

def _create_test_func(nb_name, nb_path, clearoutput=True):
    """ create str with test function to write to the test module

    Parameters
    ----------
    nb_name : str
        name of the notebook.
    nb_path : str
        relative path to the notebook.
    clearoutput : bool, optional
        if True the output is cleared after the notebook is ran. The default 
        is True.

    Returns
    -------
    nb_func : str
        str with a function.

    """
    
    nb_func = f'\ndef test_{nb_name}():\n'\
              f'    fpath_rel = {nb_path.split(os.sep)[1:]}\n'\
              '    subdir = fpath_rel[:-1]\n'\
              '    fname = fpath_rel[-1]\n'\
              '    fdir = os.path.join(*nb_dir, *subdir)\n'\
              '    cwd = os.getcwd()\n'\
              '    os.chdir(fdir)\n'\
              '    try:\n'\
              '        out = tf.run_notebook(fname, clearoutput=True)\n'\
              '        os.chdir(cwd)\n'\
              '    except Exception as e:\n'\
              '        os.chdir(cwd)\n'\
              '        raise(e)\n'\
              '    assert out == 0\n'\
              f'    return 1\n'
                  
    return nb_func

create_test_modules(r'Exercise_notebooks\Basic',    '01_basic')
create_test_modules(r'Exercise_notebooks\On_topic', '02_on_topic')
