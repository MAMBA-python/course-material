import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import matplotlib.animation as animation
import matplotlib
import os
import pastas as ps
import pandas as pd
import datetime as dt
import numpy as np
import flopy
import flopy.utils.binaryfile as bf
import requests


def create_mf_model(workspace, modelname,
                    nlay, nrow, ncol, delc, delr,
                    top, botm,
                    start_date, end_date, steady_start_period=True,
                    xul=0, yul=0,
                    strt=0, fixed_head_bound_layers=[],
                    tran=[], vcont=[],
                    hy=1, laycon=[], sf1=0.15,
                    ):
    # construct model with flopy
    ml = flopy.modflow.Modflow(modelname=modelname, model_ws=workspace)

    # time discretization
    nper = (end_date - start_date).days
    steady = [False] * nper

    if steady_start_period:
        nper += 1
        steady = [True] + steady

    # create discretization package
    dis = flopy.modflow.ModflowDis(ml, nlay=nlay, nrow=nrow, ncol=ncol,
                                   delr=delr, delc=delc, top=top, botm=botm,
                                   xul=xul, yul=yul,
                                   nper=nper, steady=steady, start_datetime=start_date
                                   )

    # create start and boundary conditions package
    ibound = np.ones_like(dis.botm.array)
    for lay in fixed_head_bound_layers:
        ibound[lay, 0, 0] = -1
        ibound[lay, 0, -1] = -1

    flopy.modflow.ModflowBas(ml, ibound=ibound, strt=strt)

    # create soil characteristics package
    flopy.modflow.ModflowBcf(ml, vcont=vcont, tran=tran, hy=hy, laycon=laycon, sf1=sf1)

    # create output control package
    flopy.modflow.ModflowOc(ml, stress_period_data=None)

    # create solver package
    flopy.modflow.ModflowPcg(ml)

    return ml


def add_recharge_knmi(ml, start_date=None, end_date=None, recharge_stn=344,
                      start_step=1, steady_start_recharge=0.0007, steady_start_period=True,
                      create_daily_average_rch=False,
                      average_rch_start=None, average_rch_end=None):

    # create recharge (evaporation and precipitation) package
    if create_daily_average_rch:
        knmi_meteo = ps.read.KnmiStation.download(start=average_rch_start - dt.timedelta(1), end=average_rch_end,
                                                  stns=recharge_stn)
        recharge_all = knmi_meteo.data.RH - knmi_meteo.data.EV24
        recharge = recharge_all.groupby([recharge_all.index.month, recharge_all.index.day]).mean()
    else:
        knmi_meteo = ps.read.KnmiStation.download(start=start_date - dt.timedelta(1), end=end_date, stns=recharge_stn)
        recharge = knmi_meteo.data.RH - knmi_meteo.data.EV24

    rch_spd = recharge_to_spd(recharge, start_step=start_step)
    if steady_start_period:
        rch_spd[0] = steady_start_recharge

    flopy.modflow.ModflowRch(ml, rech=rch_spd)

    return ml

def plot_2d_transmissivity(ml):
    """

    Parameters
    ----------
    ml: floyp.modflow.mf.Modflow
        handle for the modflow model

    Returns
    -------
    fig: matplotlib.figure.Figure

    ax: matplotlib.axes._subplots.AxesSubplot
    """
    dis = ml.get_package('DIS')
    bcf = ml.get_package('BCF6')

    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(111)
    # plt.imshow(dis.botm.array[:,0,:], aspect=100)

    im = ax.imshow(bcf.tran.array[:, 0, :], aspect=100, cmap='nipy_spectral',
                   extent=[dis.sr.xll, dis.delc.array[0] * dis.sr.ncol, dis.botm.array[-1, 0, 0], dis.top.array[0, 0]])

    values = np.unique(bcf.tran.array)
    colors = [im.cmap(im.norm(value)) for value in values]
    patches = [mpatches.Patch(color=colors[i], label="{lab}".format(lab=values[i])) for i in range(len(values))]
    leg = ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., edgecolor='black')
    leg.get_frame().set_edgecolor('b')
    leg.get_frame().set_linewidth(100)

    frame = leg.get_frame()
    frame.set_facecolor('none')
    # leg.get_frame().set_edgecolor('b')
    # leg.get_frame().set_linewidth(100)
    font = {'family': 'normal',
            'size': 30}

    matplotlib.rc('font', **font)
    leg.set_title('transmissivity', prop={'size': 14})

    return fig, ax


def recharge_to_spd(recharge, start_step=0):
    """
    converts the recharge to stress period data for modflow

    Parameters
    ----------
    recharge: pandas.Series

    start_step: int
        first timestep in the spd. Can be used if a steady state start up period is used

    Returns
    -------

    """

    recharge.index = range(start_step, len(recharge) + start_step)
    rch_spd = recharge.to_dict()

    return rch_spd


def create_plot_series(ml, output_loc=(0, 0, 0), animation_frequency='H', yearless=False):
    """
    create series from model results that can be used to plot

    Parameters
    ----------
    ml: floyp.modflow.mf.Modflow
        handle for the modflow model

    output_loc: tuple of ints
        location of the (layer, row, column) of which output is desired

    animation_frequency: str
        frequency of the animated video

    yearless: bool
        if True series are returned with a date range in the year 1900

    Returns
    -------
    plot_ts: pandas.Series
        timeseries with groundwater heads with the frequency defined by animation frequency

    recharge_sr: pandas.Series
        timeseries with recharge

    """
    # create series
    rch = ml.get_package('RCH')
    dis = ml.get_package('DIS')

    start_date = dis.start_datetime
    end_date = dis.start_datetime + dt.timedelta(int((~dis.steady.array).sum()))

    if yearless:
        start_date = start_date.replace(year=1900)
        end_date = end_date.replace(year=1900)

    headobj = bf.HeadFile(os.path.join(ml.model_ws, ml.name + '.hds'))

    ts = headobj.get_ts(output_loc)
    dates_ts = pd.date_range(start_date, end_date)
    ts_sr = pd.Series(data=ts[:, 1], index=dates_ts, name=ml.name)

    recharge_sr = pd.Series(data=rch.rech.array[:, 0, 0, 0], index=dates_ts)
    plot_range = pd.date_range(start=start_date, end=dates_ts[-1], freq=animation_frequency)
    plot_ts = ts_sr.reindex(plot_range).interpolate(method="time")

    return plot_ts, recharge_sr


def create_figure_multiple_gw_rch(plot_ts_list, recharge_sr_list, recharge_bounds):
    """

    Parameters
    ----------
    plot_ts_list: list of pandas.Series
        list with groundwater heads from multiple models

    recharge_sr_list: list of pandas.Series
        list with rehcarge timeseries from multiple models

    recharge_bounds: tuple of loat
        the minimum and maximum of the y-axis of the recharge plots


    Returns
    -------
    fig:

    line_gw_list,

    line_rch_list


    """

    no_subplots = len(plot_ts_list) + 1

    # create figure
    fig = plt.figure(figsize=(16, 8))

    # groundwater head plot
    ax1 = fig.add_subplot(no_subplots, 1, 1)
    ax1.set_ylim(np.floor(np.min(plot_ts_list)), np.ceil(np.max(plot_ts_list)))

    line_gw_list = []
    for plot_ts in plot_ts_list:
        line_gw, = ax1.plot([], [], lw=2, label=plot_ts.name)
        line_gw_list.append(line_gw)
        # line_gw.xaxis.set_major_formatter(mdates.DateFormatter('%m'))

    ax1.legend(loc=3)
    ax1.grid(True)
    ax1.set_ylabel('groundwater (m+ref)')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    # recharge plot
    recharge_min = recharge_bounds[0]
    recharge_max = recharge_bounds[1]

    ax_rch_list = []
    line_rch_list = []
    counter = 0
    for recharge_sr in recharge_sr_list:
        ax_rch_list.append(fig.add_subplot(no_subplots, 1, counter + 2, sharex=ax1))
        ax_rch_list[counter].set_ylim(recharge_min, recharge_max)

        ax_rch_list[counter].bar(recharge_sr.index - dt.timedelta(0.5), recharge_sr.values * 1000,
                                 color=plt.rcParams['axes.prop_cycle'].by_key()['color'][counter])

        line_rch, = ax_rch_list[counter].plot([plot_ts_list[0].index[0], plot_ts_list[0].index[0]],
                                              [recharge_max, recharge_min], color='black')
        line_rch_list.append(line_rch)

        ax_rch_list[counter].xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        ax_rch_list[counter].set_ylabel('recharge (mm/day)')
        counter += 1

    return fig, line_gw_list, line_rch_list


def animate_multiple_gw_rch(ml_list, animation_name, output_loc=(0, 0, 0), animation_frequency='H'):
    """
    create an animation from the results of multiple groundwater models.

    Parameters
    ----------
    ml_list: list of floyp.modflow.mf.Modflow
        list of modflow models to be animated

    animation_name: str
        name of the output file including extension. For now .mp4 and .html are supported

    output_loc: tuple of ints
        location of the (layer, row, column) of which output is desired

    animation_frequency: str (optional default is 'H')
        frequency of the animation. Warning, when the frequency is too high the animation may become too big

    Returns
    -------
    ani: matplotlib.animation.FuncAnimation
        animation object
    """

    # create groundwater en recharge time series from models
    plot_ts_list, recharge_sr_list = [], []
    for ml in ml_list:
        plot_ts, recharge_sr = create_plot_series(ml, output_loc=output_loc, yearless=True,
                                                  animation_frequency=animation_frequency)
        plot_ts_list.append(plot_ts)
        recharge_sr_list.append(recharge_sr)

    # this could be easier, I just don't know how
    len_plot_ts_list = []
    len_plot_ts_cum = 0
    for plot_ts in plot_ts_list:
        len_plot_ts_cum += len(plot_ts)
        len_plot_ts_list.append(len_plot_ts_cum)

    # create basic figure for animation
    recharge_min = np.floor(np.min(recharge_sr_list) * 900)
    recharge_max = np.ceil(np.max(recharge_sr_list) * 1100)
    recharge_bounds = (recharge_min, recharge_max)

    fig, line_gw_list, line_rch_list = create_figure_multiple_gw_rch(plot_ts_list, recharge_sr_list, recharge_bounds)

    # create initial state of the animation
    xdata, ydata = [], []

    def init():
        del xdata[:]
        del ydata[:]

        for line_gw in line_gw_list:
            line_gw.set_data(xdata, ydata)

        counter = 0
        for line_rch in line_rch_list:
            line_rch.set_data([plot_ts.index[0], plot_ts.index[0]],
                              [recharge_max, recharge_min])
            counter += 1

        line_list = [line_gw_list] + [line_rch_list]

        return line_list

    # set change for each frame

    def run(i, plot_ts_list, len_plot_ts_list):

        no_subplot = np.argmax(np.array(len_plot_ts_list) > i)

        for len_plot_ts in len_plot_ts_list:
            if i == len_plot_ts:
                del xdata[:]
                del ydata[:]

        if no_subplot > 0:
            i = i - len_plot_ts_list[no_subplot - 1]

        # update the data
        t = plot_ts_list[no_subplot].index[i]
        y = plot_ts_list[no_subplot].values[i]
        xdata.append(t)
        ydata.append(y)
        line_gw_list[no_subplot].set_data(xdata, ydata)

        line_rch_list[no_subplot].set_data([t, t],
                                           [recharge_max, recharge_min])
        line_list = [line_gw_list] + [line_rch_list]

        return line_list

    # create animation
    ani = animation.FuncAnimation(fig, run, len_plot_ts_cum, blit=False, interval=100,
                                  repeat=False, fargs=(plot_ts_list, len_plot_ts_list), init_func=init)

    # save animation
    if os.path.splitext(animation_name)[-1] == '.mp4':
        mywriter = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        ani.save(animation_name, writer=mywriter)

    elif os.path.splitext(animation_name)[-1] == '.html':
        ani.save(animation_name, writer=matplotlib.animation.HTMLWriter())

    elif os.path.splitext(animation_name)[-1] == '.gif':
        ani.save(animation_name, writer='imagemagick', fps=15)

    return ani
