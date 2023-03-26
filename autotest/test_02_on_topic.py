import os
import test_func as tf

# make projectdir accessible inside this script
tst_dir = os.path.dirname(os.path.realpath(__file__))
nb_dir = os.path.join(tst_dir, "..", *('Exercise_notebooks', 'On_topic'))


def test_03_pandas_methods_vs_functions():
    fpath_rel = ['01_Pandas', '03_pandas_methods_vs_functions.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_04_py_exploratory_comp_8():
    fpath_rel = ['01_Pandas', '04_py_exploratory_comp_8.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_matplotlib():
    fpath_rel = ['02_matplotlib', '01_matplotlib.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_py_exploratory_comp_1():
    fpath_rel = ['02_matplotlib', '02_py_exploratory_comp_1.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_for_loops_basic():
    fpath_rel = ['03_for_loops', '01_for-loops_basic.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_for_loops():
    fpath_rel = ['03_for_loops', '02_for_loops.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_conditionals():
    fpath_rel = ['04_if_statements', '01_conditionals.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_numpy():
    fpath_rel = ['05_Numpy', '01-numpy.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_linear_equations_mb6():
    fpath_rel = ['05_Numpy', '02-linear_equations_mb6.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_functions():
    fpath_rel = ['06_Functions', '02_functions.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_py_exploratory_comp_12_sol():
    fpath_rel = ['07_Object_oriented', '01_py_exploratory_comp_12_sol.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_classes():
    fpath_rel = ['07_Object_oriented', '02_classes.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_03___theorievoorbeeld():
    fpath_rel = ['07_Object_oriented', '03 - theorievoorbeeld.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_Geopandas():
    fpath_rel = ['08_GIS', 'Geopandas.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_GIS_pyshp():
    fpath_rel = ['08_GIS', 'GIS_pyshp.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

# def test_introduction_raster_IO():
#     fpath_rel = ['08_GIS', 'introduction_raster_IO.ipynb']
#     fname = os.path.join(nb_dir, *fpath_rel)
#     tf.run_notebook(fname, clearoutput=False)
#     return 0


def test_01_best_practices():
    fpath_rel = ['09_Code_Quality', '01_best_practices.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_03_Quality_ZEN_of_Python():
    fpath_rel = ['09_Code_Quality', '03_Quality_ZEN_of_Python.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_idiomatic_dicts():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_dicts.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_idiomatic_loops():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_loops.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_idiomatic_misc1():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_misc1.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_idiomatic_misc2():
    fpath_rel = ['09_Code_Quality', '04_idiomatic', 'idiomatic_misc2.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_idiomatic_python_exercise():
    fpath_rel = [
        '09_Code_Quality', '04_idiomatic',
        'idiomatic_python_exercise.ipynb'
        ]
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_03_lists():
    fpath_rel = ['10_data_types', 'collections', '03_lists.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_04_dictionaries():
    fpath_rel = ['10_data_types', 'collections', '04_dictionaries.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_numbers():
    fpath_rel = ['10_data_types', 'numbers', '01_numbers.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_strings():
    fpath_rel = ['10_data_types', 'strings', '02_strings.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_file_io():
    fpath_rel = ['11_read_write_text_files', '02_file_io.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_03_files():
    fpath_rel = ['11_read_write_text_files', '03-files.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_05_input_output():
    fpath_rel = ['11_read_write_text_files', '05-input-output.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_IntroSQLJoins():
    fpath_rel = ['12_Databases', '02-IntroSQLJoins.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_scipy_optimize_mb5():
    fpath_rel = ['13_scipy_optimize', 'scipy_optimize_mb5.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_scipy_optimize_mb5_sol():
    fpath_rel = ['13_scipy_optimize', 'scipy_optimize_mb5_sol.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_05_exceptions():
    fpath_rel = ['14_warnings_and_errors', '05_exceptions.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_datetime():
    fpath_rel = ['15_datetime', '01_datetime.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_debugging():
    fpath_rel = ['16_debugging', '01-debugging.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_debugging():
    fpath_rel = ['16_debugging', '02-debugging.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_01_testing_dutch():
    fpath_rel = ['18_testing', '01_testing_dutch.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_testing2():
    fpath_rel = ['18_testing', '02-testing2.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_03_testing3():
    fpath_rel = ['18_testing', '03-testing3.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_1_basic_pastas_model():
    fpath_rel = ['19_pastas', '1_basic_pastas_model.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_2_external_stresses():
    fpath_rel = ['19_pastas', '2_external_stresses.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_3_stressmodels():
    fpath_rel = ['19_pastas', '3_stressmodels.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_4_pastastore():
    fpath_rel = ['19_pastas', '4_pastastore.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0


def test_02_modules_and_packages():
    fpath_rel = ['20_modules_and_packages', '02_modules_and_packages.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0
