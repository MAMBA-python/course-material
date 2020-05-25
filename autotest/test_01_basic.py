import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = ["Exercise_notebooks", "Basic"]



def test_Notebook_Basics():
    fpath_rel = ("basic1_use_jupyter", "sources", "Notebook Basics.ipynb")
    subdir = fpath_rel[:-1]
    fname = fpath_rel[-1]
    fdir = os.path.join(*nb_dir, *subdir)
    print(os.getcwd())
    print(fdir)
    print(nb_dir)
    print(os.listdir(os.getcwd()))
    print(os.listdir(fdir))


    return tf.run_notebook(fdir, fname, clearoutput=True)


