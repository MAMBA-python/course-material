import os
import sys
import test_func as tf

#make projectdir accessible inside this script
nb_dir = ('', 'practical_examples')

def test_AHN_downloader():
    fpath_rel = ['01_GIS', '01_AHN_downloader', 'AHN downloader.ipynb']
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
    return out

def test_Presentatie_samen_programmeren_done():
    fpath_rel = ['01_GIS', '04_Delfland_waterways', 'Delfland_waterways.ipynb']
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
    return out

def test_wms_plot():
    fpath_rel = ['01_GIS', 'plot_wms_data', 'wms_plot.ipynb']
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
    return out

def test_geboortes_nl():
    fpath_rel = ['02_data_analysis', '02_cbs_data', 'geboortes_nl.ipynb']
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
    return out

def test_CO2_emissions_map():
    fpath_rel = ['02_data_analysis', '03_CO2_emissions', 'CO2_emissions_map.ipynb']
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
    return out

def test_congress_twitter_analysis():
    fpath_rel = ['02_data_analysis', '05_congress_twitter_analysis', 'congress_twitter_analysis.ipynb']
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
    return out

def test_00___Introduction_and_Setup():
    fpath_rel = ['03_bokeh', '00 - Introduction and Setup.ipynb']
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
    return out

def test_01___Basic_Plotting():
    fpath_rel = ['03_bokeh', '01 - Basic Plotting.ipynb']
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
    return out

def test_02___Styling_and_Theming():
    fpath_rel = ['03_bokeh', '02 - Styling and Theming.ipynb']
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
    return out

def test_03___Data_Sources_and_Transformations():
    fpath_rel = ['03_bokeh', '03 - Data Sources and Transformations.ipynb']
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
    return out

def test_04___Adding_Annotations():
    fpath_rel = ['03_bokeh', '04 - Adding Annotations.ipynb']
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
    return out

def test_05___Presentation_Layouts():
    fpath_rel = ['03_bokeh', '05 - Presentation Layouts.ipynb']
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
    return out

def test_06___Linking_and_Interactions():
    fpath_rel = ['03_bokeh', '06 - Linking and Interactions.ipynb']
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
    return out

def test_07___Bar_and_Categorical_Data_Plots():
    fpath_rel = ['03_bokeh', '07 - Bar and Categorical Data Plots.ipynb']
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
    return out

def test_08___Graph_and_Network_Plots():
    fpath_rel = ['03_bokeh', '08 - Graph and Network Plots.ipynb']
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
    return out

def test_11___Running_Bokeh_Applications():
    fpath_rel = ['03_bokeh', '11 - Running Bokeh Applications.ipynb']
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
    return out

def test_Folium01_and_mplleaflet():
    fpath_rel = ['04_folium', 'Folium01_and_mplleaflet.ipynb']
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
    return out

def test_Folium02_CheckZorder():
    fpath_rel = ['04_folium', 'Folium02_CheckZorder.ipynb']
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
    return out

def test_Folium03_Colormaps():
    fpath_rel = ['04_folium', 'Folium03_Colormaps.ipynb']
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
    return out

def test_Folium04_ContinuousWorld():
    fpath_rel = ['04_folium', 'Folium04_ContinuousWorld.ipynb']
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
    return out

def test_Folium05_ControlScale():
    fpath_rel = ['04_folium', 'Folium05_ControlScale.ipynb']
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
    return out

def test_Folium06_FloatImage():
    fpath_rel = ['04_folium', 'Folium06_FloatImage.ipynb']
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
    return out

def test_Folium07_WMS_and_WMTS():
    fpath_rel = ['04_folium', 'Folium07_WMS_and_WMTS.ipynb']
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
    return out

def test_Parallel_processing():
    fpath_rel = ['04_ParallelProcessing', 'Parallel processing.ipynb']
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
    return out

def test_groundwater_model():
    fpath_rel = ['05_flopy_groundwater_model', 'groundwater_model.ipynb']
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
    return out

def test_example_notebook_pylizard():
    fpath_rel = ['05_pylizard', 'example_notebook_pylizard.ipynb']
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
    return out

def test_01_modules_and_packages():
    fpath_rel = ['08_modules_and_packages', '01_modules_and_packages.ipynb']
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
    return out

def test_01_cmdline():
    fpath_rel = ['10_creating_programs', '01-cmdline.ipynb']
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
    return out
