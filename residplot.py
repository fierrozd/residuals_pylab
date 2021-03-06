import sys,os
from matplotlib.ticker import *

import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

import pylab as pl
def plotwresids(x,y,res,err=None,xlabel="",ylabel="",reslabel="residuals",xlim=None,ylim=None,color=['k'],alpha=[1], marker=['o'], scatter=True,LIVE=False, fig=None, legend=None):

    if LIVE:
        pl.ion()
    if not (fig==None):
        fig=pl.figure(fig)
    else:
        fig=pl.figure()
    mpl.rcParams['font.size'] = 18.
    mpl.rcParams['font.family'] = 'Times New Roman'
    #    mpl.rcParams['font.serif'] = 'Times'                                                                                                       
    mpl.rcParams['axes.labelsize'] = 18
    mpl.rcParams['xtick.labelsize'] = 18.
    mpl.rcParams['ytick.labelsize'] = 18.
    majorLocatorx   = MultipleLocator(1.0)
    majorFormattery = FormatStrFormatter('%d')
    majorFormatterx = FormatStrFormatter('%d')
    majorFormatterresy = FormatStrFormatter('%.1f')    
    top_offset = .07
    left_offset = .15
    right_offset = .2
    bottom_offset = .13
    hgap = 0
    ax_width = 1-left_offset - right_offset
    ax_height = (1-top_offset - bottom_offset - hgap)/2
    
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width 
    
    rect_scatter = [left, bottom+0.2, width, height]
    rect_histx = [left, bottom, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    
    pl.subplots_adjust(hspace=0.,wspace=0.1 )
    ax1 = pl.axes(rect_scatter)          
    axres = pl.axes(rect_histx)
    ax1.minorticks_on()
    axres.minorticks_on()    
    pl.setp(ax1.get_xticklabels(),
            visible=False)    
    import numpy as np
    if not isinstance(x, list) and not isinstance(x, np.ndarray):
        x=  [[x]]
        y=  [[y]]
        res=[[res]]
        scatter=[[scatter]]
        if err:
            err=[[err]]
    elif not isinstance(x[0], list) and not isinstance(x[0], np.ndarray ):
            x=  [x]
            y=  [y]
            res=[res]
            scatter=[scatter]
            if err:
                err=[err]

    if len(alpha)<len(x):
        alpha=alpha*len(x)
    if len(color)<len(x):
        color=color*len(x)
    if len(marker)<len(x):
        marker=marker*len(x)
        
    print x,len(x)
    for i in range(len(x)):
        label=''
        if isinstance(legend,str):
            label=legend
        elif ( isinstance(legend, np.ndarray ) or isinstance(legend, list)):
            try: label=legend[i]
            except:label=''                 

        if err and not (err[i]==None):
            if scatter[i]:
                   ax1.errorbar(x[i],y[i],yerr=err[i],color=color[i],alpha=alpha[i], marker=marker[i], fmt='.', label=label)            
            else:
                   ax1.errorbar(x[i],y[i],yerr=err[i],color=color[i],alpha=alpha[i], marker=marker[i], label=label)                            
                                                                
        elif scatter:
            ax1.scatter(x[i],y[i],color=color[i],alpha=alpha[i], marker=marker[i], label=label)
        else:
            ax1.plot(x[i],y[i],color=color[i],alpha=alpha[i], marker=marker[i], label=label) 
        if LIVE:
            pl.draw()
    
        try: 
            res[i].all()==None
            axres.scatter(x[i],res[i],color=color[i],alpha=alpha[i], label=legend)
        except:
            pass
        if legend:
            ax1.legend(fontsize=12)
    
    majorLocatory   = MultipleLocator((axres.get_ylim()[1]-axres.get_ylim()[0])/3)  
    axres.yaxis.set_major_locator(majorLocatory)
    axres.set_xlim(ax1.get_xlim()[0],ax1.get_xlim()[1])
    axres.plot([axres.get_xlim()[0],axres.get_xlim()[1]],[0,0],'k--')
    
    
    axres.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    axres.set_yticks(axres.get_yticks()[:-2])
    axres.set_ylabel(reslabel)
    axres.yaxis.set_major_formatter(majorFormatterresy)

#    pl.show()
    return(fig)
