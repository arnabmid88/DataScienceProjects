# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def linechart(series, **kwargs):
    fig = plt.figure()
    ax = plt.subplot(111)
    for line in series:
        line = list(line)
        xvals = [v[0] for v in line]
        yvals = [v[1] for v in line]
        ax.plot(xvals, yvals)
    if 'ylabel' in kwargs:
        ax.set_ylabel(kwargs['ylabel'])
    if 'title' in kwargs:
        plt.title(kwargs['title'])
    if 'labels' in kwargs:
        ax.legend(kwargs.get('labels'))
    return fig

def stackedarea(series, **kwargs):
    fig = plt.figure()
    axe = fig.add_subplot(111)
    fnx = lambda s: np.array(list(v[1] for v in s), dtype="f8")
    yax = np.row_stack(fnx(s) for s in series)
    xax = np.arange(1917, 2008)
    polys = axe.stackplot(xax, yax)
    axe.margins(0,0)
    if 'ylabel' in kwargs:
        axe.set_ylabel(kwargs['ylabel'])
    if 'labels' in kwargs:
        legendProxies = []
        for poly in polys:
            legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=poly.get_facecolor()[0]))
        axe.legend(legendProxies, kwargs.get('labels'))
    if 'title' in kwargs:
        plt.title(kwargs['title'])
    return fig
