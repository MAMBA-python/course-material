import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = ('Exercise_notebooks', 'On_topic')

def test_02_py_exploratory_comp_8():
    fpath_rel = ['01_Pandas', '02_py_exploratory_comp_8.ipynb']
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

def test_01_numpy():
    fpath_rel = ['03_Numpy', '01-numpy.ipynb']
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
    fpath_rel = ['03_Numpy', '02-linear_equations_mb6.ipynb']
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
    fpath_rel = ['04_Functions', '01_functions.ipynb']
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
    fpath_rel = ['05_Object_oriented', '00 - theorievoorbeeld.ipynb']
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
    fpath_rel = ['05_Object_oriented', '01_py_exploratory_comp_12_sol.ipynb']
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
    fpath_rel = ['05_Object_oriented', '02_classes.ipynb']
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
    fpath_rel = ['06_GIS', 'Geopandas.ipynb']
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
    fpath_rel = ['06_GIS', 'GIS_pyshp.ipynb']
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
    fpath_rel = ['06_GIS', 'introduction_raster_IO.ipynb']
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

def test_01_file_io():
    fpath_rel = ['07_read_write_text_files', '01_file_io.ipynb']
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
    fpath_rel = ['07_read_write_text_files', '03-files.ipynb']
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
    fpath_rel = ['08_Databases', '02-IntroSQLJoins.ipynb']
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
        out = tf.run_notebook(fname, clearoutput=True)
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

def test_02_exceptions():
    fpath_rel = ['11_Errors', '02_exceptions.ipynb']
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
    fpath_rel = ['12_Optimize', 'scipy_optimize_mb5.ipynb']
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
    fpath_rel = ['12_Optimize', 'scipy_optimize_mb5_sol.ipynb']
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
    fpath_rel = ['13_testing', '01-testing.ipynb']
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
    fpath_rel = ['13_testing', '02-testing2.ipynb']
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
    fpath_rel = ['14_datetime', '01_datetime.ipynb']
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
    fpath_rel = ['15_loops_and_statements', '01_conditionals.ipynb']
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

def test_03_for_loops():
    fpath_rel = ['15_loops_and_statements', '03_for_loops.ipynb']
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

def test_01_cmdline():
    fpath_rel = ['16_creating_programs', '01-cmdline.ipynb']
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
    fpath_rel = ['17_debugging', '01-debugging.ipynb']
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
    fpath_rel = ['17_debugging', '02-debugging.ipynb']
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

def test_01_modules_and_packages():
    fpath_rel = ['18_modules_and_packages', '01_modules_and_packages.ipynb']
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

def test_00___Introduction_and_Setup():
    fpath_rel = ['19_bokeh', '00 - Introduction and Setup.ipynb']
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

def test_01___Basic_Plotting():
    fpath_rel = ['19_bokeh', '01 - Basic Plotting.ipynb']
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

def test_02___Styling_and_Theming():
    fpath_rel = ['19_bokeh', '02 - Styling and Theming.ipynb']
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

def test_03___Data_Sources_and_Transformations():
    fpath_rel = ['19_bokeh', '03 - Data Sources and Transformations.ipynb']
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

def test_04___Adding_Annotations():
    fpath_rel = ['19_bokeh', '04 - Adding Annotations.ipynb']
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

def test_05___Presentation_Layouts():
    fpath_rel = ['19_bokeh', '05 - Presentation Layouts.ipynb']
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

def test_06___Linking_and_Interactions():
    fpath_rel = ['19_bokeh', '06 - Linking and Interactions.ipynb']
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

def test_07___Bar_and_Categorical_Data_Plots():
    fpath_rel = ['19_bokeh', '07 - Bar and Categorical Data Plots.ipynb']
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

def test_08___Graph_and_Network_Plots():
    fpath_rel = ['19_bokeh', '08 - Graph and Network Plots.ipynb']
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

def test_11___Running_Bokeh_Applications():
    fpath_rel = ['19_bokeh', '11 - Running Bokeh Applications.ipynb']
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

def test_A1___Models_and_Primitives():
    fpath_rel = ['19_bokeh', 'A1 - Models and Primitives.ipynb']
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

def test_A2___Visualizing_Big_Data_with_Datashader():
    fpath_rel = ['19_bokeh', 'A2 - Visualizing Big Data with Datashader.ipynb']
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

def test_A3___High_Level_Charting_with_Holoviews():
    fpath_rel = ['19_bokeh', 'A3 - High-Level Charting with Holoviews.ipynb']
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

def test_A4___Additional_Resources():
    fpath_rel = ['19_bokeh', 'A4 - Additional Resources.ipynb']
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

def test_Folium01_and_mplleaflet():
    fpath_rel = ['20_folium', 'Folium01_and_mplleaflet.ipynb']
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

def test_Folium02_CheckZorder():
    fpath_rel = ['20_folium', 'Folium02_CheckZorder.ipynb']
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

def test_Folium03_Colormaps():
    fpath_rel = ['20_folium', 'Folium03_Colormaps.ipynb']
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

def test_Folium04_ContinuousWorld():
    fpath_rel = ['20_folium', 'Folium04_ContinuousWorld.ipynb']
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

def test_Folium05_ControlScale():
    fpath_rel = ['20_folium', 'Folium05_ControlScale.ipynb']
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

def test_Folium06_FloatImage():
    fpath_rel = ['20_folium', 'Folium06_FloatImage.ipynb']
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

def test_Folium07_WMS_and_WMTS():
    fpath_rel = ['20_folium', 'Folium07_WMS_and_WMTS.ipynb']
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
    fpath_rel = ['24_pastas', '1_basic_pastas_model.ipynb']
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
    fpath_rel = ['24_pastas', '2_external_stresses.ipynb']
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
    fpath_rel = ['24_pastas', '3_stressmodels.ipynb']
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

def test_4_pastas_project():
    fpath_rel = ['24_pastas', '4_pastas_project.ipynb']
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
