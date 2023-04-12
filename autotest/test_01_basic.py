import os
import test_func as tf

# make projectdir accessible inside this script
tst_dir = os.path.dirname(os.path.realpath(__file__))
nb_dir = os.path.join(tst_dir, "..", *('Exercise_notebooks', 'Basic'))


def test_Notebook_Basics():
    fpath_rel = ['basic1_use_jupyter', 'sources', 'Notebook Basics.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_Running_code():
    fpath_rel = ['basic1_use_jupyter', 'sources', 'Running code.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_py_exploratory_comp_2():
    fpath_rel = ['basic2_basics_plotting', 'py_exploratory_comp_2.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_py_exploratory_comp_3():
    fpath_rel = ['basic3_arrays', 'py_exploratory_comp_3.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_Notebook_Basics_():
    fpath_rel = [
        'zz_alternative_basic', 'basic1_use_jupyter', 
        'sources', 'Notebook Basics.ipynb'
        ]
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_Running_code_():
    fpath_rel = [
        'zz_alternative_basic', 'basic1_use_jupyter',
        'sources', 'Running code.ipynb'
        ]
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_01_numbers():
    fpath_rel = ['zz_alternative_basic', 'basic2_numbers', '01_numbers.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_02_strings():
    fpath_rel = ['zz_alternative_basic', 'basic3_strings', '02_strings.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_03_lists():
    fpath_rel = [
        'zz_alternative_basic', 'basic4_collections', '03_lists.ipynb'
        ]
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_04_dictionaries():
    fpath_rel = [
        'zz_alternative_basic', 'basic4_collections', '04_dictionaries.ipynb'
        ]
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_Oefeningen_extra_basis_I():
    fpath_rel = ['zz_back_to_basic', 'Oefeningen_extra_basis_I.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)


def test_Oefeningen_extra_basis_II():
    fpath_rel = ['zz_back_to_basic', 'Oefeningen_extra_basis_II.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
