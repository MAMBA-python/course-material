# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:18:44 2020

@author: onno_
"""


# Remove the temp directory and then create a fresh one
import os
import sys
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# these notebooks are excluded because they contain errors on purpose
_exclude_nb_list = [
    'use_Jupyter.ipynb', 'py_exploratory_comp_4.ipynb',
    '01_numbers_exercise.ipynb',
    '02_strings_exercise.ipynb', '03_lists_exercise.ipynb',
    '04_dictionaries_exercise.ipynb', '01_recap1_exercise.ipynb',
    '01_pandas_basis_dutch.ipynb',
    '02_exercise_whatsapp.ipynb',
    '02_functions_exercise.ipynb',
    '04-riddles_and_functions_group_exercises',
    '01_py_exploratory_comp_4.ipynb',
    '03-func.ipynb',
    '02_classes_exercise.ipynb',
    '02_file_io_exercise.ipynb',
    '01-IntroDBWorkshop.ipynb',
    '02_common_pitfalls.ipynb',
    '01_warnings_dutch',
    '02_errors_dutch',
    '04-errors.ipynb',
    '05_exceptions_exercise.ipynb',
    '03_py_exploratory_comp_7.ipynb',
    '03_py_exploratory_comp_7_sol.ipynb',
    '01-testing1_exercise.ipynb',
    '02-testing2_exercise.ipynb',
    '03-testing3_exercise.ipynb',
    '04-defensive.ipynb',
    '01_datetime_exercise.ipynb',
    '01_conditionals_exercise.ipynb',
    '02-cond.ipynb',
    '02_for_loops_exercise.ipynb',
    '03-loop.ipynb',
    '01-debugging_exercise.ipynb',
    '09 - Geographic Plots.ipynb',
    '10 - Exporting and Embedding.ipynb',
    '01_modules_and_packages_dutch',
    '01_logging_dutch.ipynb',
    'how to run executables in python.ipynb',
    'Webscraping-BeautifulSoup.ipynb',
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
    for root, dirs, files in os.walk(os.path.join(sys.path[0], 
                                                  exercise_nb_dir)):
        for file in files:
            if file.endswith(".ipynb") and (
                    '.ipynb_checkpoints' not in os.path.join(root, file)):
                if file not in _exclude_nb_list:
                    notebook_path = os.path.join(root, file)
                    notebook_rel_path = notebook_path.split(exercise_nb_dir)[-1]  # noqa E501
                    notebook_list.append(notebook_rel_path)

    return notebook_list


def run_notebook(fname, clearoutput=False, timeout=120):
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
    """

    print('running --> {}'.format(fname))

    with open(fname) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    out = ep.preprocess(nb, {"metadata": {"path": os.path.split(fname)[0]}})

    if clearoutput:
        clear_output(fname)

    return out


def clear_output(fname):
    """ clear the output of a notebook. This should be done to reduce size
    and improve the speed of the git stuff.

    Parameters
    ----------
    fname: str
        full path of the notebook which is cleared of output

    """
    nb = nbformat.read(fname, nbformat.NO_CONVERT)
    nb['metadata'] = {}

    for cell in nb.cells:
        if hasattr(cell, "outputs"):
            cell.outputs = []
        if hasattr(cell, "execution_count"):
            cell["execution_count"] = None

    nbformat.write(nb, fname)
    print('cleared output --> {}'.format(os.path.split(fname)[-1]))