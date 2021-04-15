import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = ('Exercise_notebooks', 'On_topic')

def test_04_py_exploratory_comp_8():
    fpath_rel = ['01_Pandas', '04_py_exploratory_comp_8.ipynb']
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

def test_03_pandas_methods_vs_functions():
    fpath_rel = ['01_Pandas', '03_pandas_methods_vs_functions.ipynb']
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


def test_01_matplotlib():
    fpath_rel = ['02_matplotlib', '01_matplotlib.ipynb']
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

def test_02_py_exploratory_comp_1():
    fpath_rel = ['02_matplotlib', '02_py_exploratory_comp_1.ipynb']
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

def test_01_for_loops_basic():
    fpath_rel = ['03_for_loops', '01_for-loops_basic.ipynb']
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

def test_02_for_loops():
    fpath_rel = ['03_for_loops', '02_for_loops.ipynb']
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

def test_01_conditionals():
    fpath_rel = ['04_if_statements', '01_conditionals.ipynb']
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

def test_01_numpy():
    fpath_rel = ['05_Numpy', '01-numpy.ipynb']
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

def test_02_linear_equations_mb6():
    fpath_rel = ['05_Numpy', '02-linear_equations_mb6.ipynb']
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

def test_01_functions():
    fpath_rel = ['06_Functions', '01_py_exploratory_comp_4.ipynb']
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

def test_00___theorievoorbeeld():
    fpath_rel = ['07_Object_oriented', '03 - theorievoorbeeld.ipynb']
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

def test_01_py_exploratory_comp_12_sol():
    fpath_rel = ['07_Object_oriented', '01_py_exploratory_comp_12_sol.ipynb']
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

def test_02_classes():
    fpath_rel = ['07_Object_oriented', '02_classes.ipynb']
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

def test_Geopandas():
    fpath_rel = ['08_GIS', 'Geopandas.ipynb']
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

def test_GIS_pyshp():
    fpath_rel = ['08_GIS', 'GIS_pyshp.ipynb']
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

def test_introduction_raster_IO():
    fpath_rel = ['08_GIS', 'introduction_raster_IO.ipynb']
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

def test_01_best_practices():
    fpath_rel = ['09_Code_Quality', '01_best_practices.ipynb']
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

def test_03_Quality_ZEN_of_Python():
    fpath_rel = ['09_Code_Quality', '03_Quality_ZEN_of_Python.ipynb']
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    cwd = os.getcwd()
    os.chdir(fdir)
    try:
        out = tf.run_notebook(fname, clearoutput=False)
        os.chdir(cwd)
    except Exception as e:
        os.chdir(cwd)
        raise(e)
    assert out == 0
    return 1

def test_idiomatic_dicts():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_dicts.ipynb']
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

def test_idiomatic_loops():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_loops.ipynb']
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

def test_idiomatic_misc1():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_misc1.ipynb']
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

def test_idiomatic_misc2():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_misc2.ipynb']
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

def test_idiomatic_python_exercise():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_python_exercise.ipynb']
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
    fpath_rel = ['10_data_types', 'collections', '03_lists.ipynb']
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
    fpath_rel = ['10_data_types', 'collections', '04_dictionaries.ipynb']
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
    fpath_rel = ['10_data_types', 'numbers', '01_numbers.ipynb']
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
    fpath_rel = ['10_data_types', 'strings', '02_strings.ipynb']
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


def test_02_file_io():
    fpath_rel = ['11_read_write_text_files', '02_file_io.ipynb']
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

def test_03_files():
    fpath_rel = ['11_read_write_text_files', '03-files.ipynb']
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

def test_05_input_output():
    fpath_rel = ['11_read_write_text_files', '05-input-output.ipynb']
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

def test_02_IntroSQLJoins():
    fpath_rel = ['12_Databases', '02-IntroSQLJoins.ipynb']
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

def test_scipy_optimize_mb5():
    fpath_rel = ['13_scipy_optimize', 'scipy_optimize_mb5.ipynb']
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

def test_scipy_optimize_mb5_sol():
    fpath_rel = ['13_scipy_optimize', 'scipy_optimize_mb5_sol.ipynb']
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

def test_02_exceptions():
    fpath_rel = ['14_warnings_and_errors', '05_exceptions.ipynb']
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

def test_01_datetime():
    fpath_rel = ['15_datetime', '01_datetime.ipynb']
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

def test_01_debugging():
    fpath_rel = ['16_debugging', '01-debugging.ipynb']
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

def test_02_debugging():
    fpath_rel = ['16_debugging', '02-debugging.ipynb']
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

def test_01_testing():
    fpath_rel = ['18_testing', '02-testing2.ipynb']
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

def test_02_testing2():
    fpath_rel = ['18_testing', '03-testing3.ipynb']
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


def test_1_basic_pastas_model():
    fpath_rel = ['19_pastas', '1_basic_pastas_model.ipynb']
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

def test_2_external_stresses():
    fpath_rel = ['19_pastas', '2_external_stresses.ipynb']
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

def test_3_stressmodels():
    fpath_rel = ['19_pastas', '3_stressmodels.ipynb']
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
