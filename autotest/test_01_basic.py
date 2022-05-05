import os
import test_func as tf

#make projectdir accessible inside this script
nb_dir = ('Exercise_notebooks', 'Basic')

def test_Notebook_Basics():
    fpath_rel = ['basic1_use_jupyter', 'sources', 'Notebook Basics.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_Running_code():
    fpath_rel = ['basic1_use_jupyter', 'sources', 'Running code.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_py_exploratory_comp_2():
    fpath_rel = ['basic2_basics_plotting', 'py_exploratory_comp_2.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_py_exploratory_comp_3():
    fpath_rel = ['basic3_arrays', 'py_exploratory_comp_3.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_Notebook_Basics_():
    fpath_rel = ['zz_alternative_basic', 'basic1_use_jupyter', 'sources', 'Notebook Basics.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_Running_code_():
    fpath_rel = ['zz_alternative_basic', 'basic1_use_jupyter', 'sources', 'Running code.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_01_numbers():
    fpath_rel = ['zz_alternative_basic', 'basic2_numbers', '01_numbers.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_02_strings():
    fpath_rel = ['zz_alternative_basic', 'basic3_strings', '02_strings.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_03_lists():
    fpath_rel = ['zz_alternative_basic', 'basic4_collections', '03_lists.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_04_dictionaries():
    fpath_rel = ['zz_alternative_basic', 'basic4_collections', '04_dictionaries.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=True)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1
