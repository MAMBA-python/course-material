import os
import sys
import test_func as tf

#make projectdir accessible inside this script
tst_dir = os.path.dirname(os.path.realpath(__file__))
nb_dir = os.path.join(tst_dir, "..", *('', 'practical_examples'))

# def test_AHN_downloader():
#     fpath_rel = ['01_GIS', '01_AHN_downloader', 'AHN downloader.ipynb']
#     fname = os.path.join(nb_dir, *fpath_rel)
#     tf.run_notebook(fname, clearoutput=False)
#     return 0

def test_Delfland_waterways():
    fpath_rel = ['01_GIS', '02_Delfland_waterways', 'Delfland_waterways.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

# def test_wms_plot():
#     fpath_rel = ['01_GIS', '03_plot_wms_data', 'wms_plot.ipynb']
#     fname = os.path.join(nb_dir, *fpath_rel)
#     tf.run_notebook(fname, clearoutput=False)
#     return 0

def test_geboortes_nl():
    fpath_rel = ['02_data_analysis', '01_cbs_data', 'geboortes_nl.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_CO2_emissions_map():
    fpath_rel = ['02_data_analysis', '02_CO2_emissions', 'CO2_emissions_map.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_congress_twitter_analysis():
    fpath_rel = ['02_data_analysis', '03_congress_twitter_analysis', 'congress_twitter_analysis.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_00___Introduction_and_Setup():
    fpath_rel = ['03_bokeh', '00 - Introduction and Setup.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_01___Basic_Plotting():
    fpath_rel = ['03_bokeh', '01 - Basic Plotting.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_02___Styling_and_Theming():
    fpath_rel = ['03_bokeh', '02 - Styling and Theming.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_03___Data_Sources_and_Transformations():
    fpath_rel = ['03_bokeh', '03 - Data Sources and Transformations.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_04___Adding_Annotations():
    fpath_rel = ['03_bokeh', '04 - Adding Annotations.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_05___Presentation_Layouts():
    fpath_rel = ['03_bokeh', '05 - Presentation Layouts.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_06___Linking_and_Interactions():
    fpath_rel = ['03_bokeh', '06 - Linking and Interactions.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_07___Bar_and_Categorical_Data_Plots():
    fpath_rel = ['03_bokeh', '07 - Bar and Categorical Data Plots.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_08___Graph_and_Network_Plots():
    fpath_rel = ['03_bokeh', '08 - Graph and Network Plots.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_11___Running_Bokeh_Applications():
    fpath_rel = ['03_bokeh', '11 - Running Bokeh Applications.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium02_CheckZorder():
    fpath_rel = ['04_folium', 'Folium02_CheckZorder.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium03_Colormaps():
    fpath_rel = ['04_folium', 'Folium03_Colormaps.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium04_ContinuousWorld():
    fpath_rel = ['04_folium', 'Folium04_ContinuousWorld.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium05_ControlScale():
    fpath_rel = ['04_folium', 'Folium05_ControlScale.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium06_FloatImage():
    fpath_rel = ['04_folium', 'Folium06_FloatImage.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Folium07_WMS_and_WMTS():
    fpath_rel = ['04_folium', 'Folium07_WMS_and_WMTS.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_01_cmdline():
    fpath_rel = ['09_creating_programs', '01-cmdline.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0

def test_Parallel_processing():
    fpath_rel = ['11_ParallelProcessing', 'Parallel processing.ipynb']
    fname = os.path.join(nb_dir, *fpath_rel)
    tf.run_notebook(fname, clearoutput=False)
    return 0
