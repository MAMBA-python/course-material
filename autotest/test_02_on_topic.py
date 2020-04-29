import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = r"Exercise_notebooks\On_topic"
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir, nb_dir))
sys.path.insert(0, PROJECT_DIR)



def test_02_py_exploratory_comp_8():
    fpath_rel = r"\01_Pandas\02_py_exploratory_comp_8.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_pandas_methods_vs_functions():
    fpath_rel = r"\01_Pandas\03_pandas_methods_vs_functions.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_matplotlib():
    fpath_rel = r"\02_matplotlib\01_matplotlib.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_py_exploratory_comp_1():
    fpath_rel = r"\02_matplotlib\02_py_exploratory_comp_1.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_numpy():
    fpath_rel = r"\03_Numpy\01-numpy.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_linear_equations_mb6():
    fpath_rel = r"\03_Numpy\02-linear_equations_mb6.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_functions():
    fpath_rel = r"\04_Functions\01_functions.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_00___theorievoorbeeld():
    fpath_rel = r"\05_Object_oriented\00 - theorievoorbeeld.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_py_exploratory_comp_12_sol():
    fpath_rel = r"\05_Object_oriented\01_py_exploratory_comp_12_sol.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_classes():
    fpath_rel = r"\05_Object_oriented\02_classes.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Geopandas():
    fpath_rel = r"\06_GIS\Geopandas.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_GIS_pyshp():
    fpath_rel = r"\06_GIS\GIS_pyshp.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_introduction_raster_IO():
    fpath_rel = r"\06_GIS\introduction_raster_IO.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_file_io():
    fpath_rel = r"\07_read_write_text_files\01_file_io.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_files():
    fpath_rel = r"\07_read_write_text_files\03-files.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_IntroSQLJoins():
    fpath_rel = r"\08_Databases\02-IntroSQLJoins.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_best_practices():
    fpath_rel = r"\09_Code_Quality\01_best_practices.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_Quality_ZEN_of_Python():
    fpath_rel = r"\09_Code_Quality\03_Quality_ZEN_of_Python.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_idiomatic_dicts():
    fpath_rel = r"\09_Code_Quality\04_idiomatic\idiomatic_dicts.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_idiomatic_loops():
    fpath_rel = r"\09_Code_Quality\04_idiomatic\idiomatic_loops.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_idiomatic_misc1():
    fpath_rel = r"\09_Code_Quality\04_idiomatic\idiomatic_misc1.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_idiomatic_misc2():
    fpath_rel = r"\09_Code_Quality\04_idiomatic\idiomatic_misc2.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_idiomatic_python_exercise():
    fpath_rel = r"\09_Code_Quality\04_idiomatic\idiomatic_python_exercise.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_lists():
    fpath_rel = r"\10_data_types\collections\03_lists.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_04_dictionaries():
    fpath_rel = r"\10_data_types\collections\04_dictionaries.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_numbers():
    fpath_rel = r"\10_data_types\numbers\01_numbers.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_strings():
    fpath_rel = r"\10_data_types\strings\02_strings.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_exceptions():
    fpath_rel = r"\11_Errors\02_exceptions.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_scipy_optimize_mb5():
    fpath_rel = r"\12_Optimize\scipy_optimize_mb5.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_scipy_optimize_mb5_sol():
    fpath_rel = r"\12_Optimize\scipy_optimize_mb5_sol.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_testing():
    fpath_rel = r"\13_testing\01-testing.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_testing2():
    fpath_rel = r"\13_testing\02-testing2.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_datetime():
    fpath_rel = r"\14_datetime\01_datetime.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_conditionals():
    fpath_rel = r"\15_loops_and_statements\01_conditionals.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03_for_loops():
    fpath_rel = r"\15_loops_and_statements\03_for_loops.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_cmdline():
    fpath_rel = r"\16_creating_programs\01-cmdline.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_debugging():
    fpath_rel = r"\17_debugging\01-debugging.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02_debugging():
    fpath_rel = r"\17_debugging\02-debugging.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01_modules_and_packages():
    fpath_rel = r"\18_modules_and_packages\01_modules_and_packages.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_00___Introduction_and_Setup():
    fpath_rel = r"\19_bokeh\00 - Introduction and Setup.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_01___Basic_Plotting():
    fpath_rel = r"\19_bokeh\01 - Basic Plotting.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_02___Styling_and_Theming():
    fpath_rel = r"\19_bokeh\02 - Styling and Theming.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_03___Data_Sources_and_Transformations():
    fpath_rel = r"\19_bokeh\03 - Data Sources and Transformations.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_04___Adding_Annotations():
    fpath_rel = r"\19_bokeh\04 - Adding Annotations.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_05___Presentation_Layouts():
    fpath_rel = r"\19_bokeh\05 - Presentation Layouts.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_06___Linking_and_Interactions():
    fpath_rel = r"\19_bokeh\06 - Linking and Interactions.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_07___Bar_and_Categorical_Data_Plots():
    fpath_rel = r"\19_bokeh\07 - Bar and Categorical Data Plots.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_08___Graph_and_Network_Plots():
    fpath_rel = r"\19_bokeh\08 - Graph and Network Plots.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_10___Exporting_and_Embedding():
    fpath_rel = r"\19_bokeh\10 - Exporting and Embedding.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_11___Running_Bokeh_Applications():
    fpath_rel = r"\19_bokeh\11 - Running Bokeh Applications.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_A1___Models_and_Primitives():
    fpath_rel = r"\19_bokeh\A1 - Models and Primitives.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_A2___Visualizing_Big_Data_with_Datashader():
    fpath_rel = r"\19_bokeh\A2 - Visualizing Big Data with Datashader.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_A3___High_Level_Charting_with_Holoviews():
    fpath_rel = r"\19_bokeh\A3 - High-Level Charting with Holoviews.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_A4___Additional_Resources():
    fpath_rel = r"\19_bokeh\A4 - Additional Resources.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium01_and_mplleaflet():
    fpath_rel = r"\20_folium\Folium01_and_mplleaflet.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium02_CheckZorder():
    fpath_rel = r"\20_folium\Folium02_CheckZorder.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium03_Colormaps():
    fpath_rel = r"\20_folium\Folium03_Colormaps.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium04_ContinuousWorld():
    fpath_rel = r"\20_folium\Folium04_ContinuousWorld.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium05_ControlScale():
    fpath_rel = r"\20_folium\Folium05_ControlScale.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium06_FloatImage():
    fpath_rel = r"\20_folium\Folium06_FloatImage.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Folium07_WMS_and_WMTS():
    fpath_rel = r"\20_folium\Folium07_WMS_and_WMTS.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_how_to_run_executables_in_python():
    fpath_rel = r"\21_run_external_programs_from_cmd\how to run executables in python.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_Webscraping_BeautifulSoup():
    fpath_rel = r"\23_webscraping\Webscraping-BeautifulSoup.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_1_basic_pastas_model():
    fpath_rel = r"\24_pastas\1_basic_pastas_model.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_2_external_stresses():
    fpath_rel = r"\24_pastas\2_external_stresses.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_3_stressmodels():
    fpath_rel = r"\24_pastas\3_stressmodels.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)

def test_4_pastas_project():
    fpath_rel = r"\24_pastas\4_pastas_project.ipynb"
    fname = os.path.split(fpath_rel)[-1]
    fdir = PROJECT_DIR + os.path.split(fpath_rel)[0]
    return tf.run_notebook(fdir, fname, clearoutput=True)
