import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = r"exercise_notebooks/basic"
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir, nb_dir))
sys.path.insert(0, PROJECT_DIR)



def test_Notebook_Basics():
    fpath_rel = r"/basic1_use_jupyter/sources/Notebook Basics.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Running_code():
    fpath_rel = r"/basic1_use_jupyter/sources/Running code.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_py_exploratory_comp_2():
    fpath_rel = r"/basic2_basics_plotting/py_exploratory_comp_2.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Untitled():
    fpath_rel = r"/basic2_basics_plotting/Untitled.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_py_exploratory_comp_3():
    fpath_rel = r"/basic3_arrays/py_exploratory_comp_3.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Notebook_Basics_():
    fpath_rel = r"/zz_alternative_basic/basic1_use_jupyter/sources/Notebook Basics.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Running_code_():
    fpath_rel = r"/zz_alternative_basic/basic1_use_jupyter/sources/Running code.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_numbers():
    fpath_rel = r"/zz_alternative_basic/basic2_numbers/01_numbers.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_strings():
    fpath_rel = r"/zz_alternative_basic/basic3_strings/02_strings.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_lists():
    fpath_rel = r"/zz_alternative_basic/basic4_collections/03_lists.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_04_dictionaries():
    fpath_rel = r"/zz_alternative_basic/basic4_collections/04_dictionaries.ipynb"
    subdir, fname = os.path.split(fpath_rel)
    fdir = os.path.join(PROJECT_DIR, os.path.join(*tuple(subdir.split("/"))))
    return tf.run_notebook(fdir, fname, clearoutput=True)
