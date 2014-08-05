self explainatory: 

it makes a classical residual plot, with the residuals at the bottm and the data in the top panel. 
each plot can be scatter plot, line plot and the data can be errorbars

try it as follows




import numpy as np

import pylab as pl

from residplot import plotwresids

x=np.random.rand(100)

y=np.sin(x)+(np.random.rand(100)-0.5)*np.sqrt(x)

x1=np.random.rand(100)

y1=np.sin(x1)+3*(np.random.rand(100)-0.5)*np.sqrt(x1)

res=(y-np.sin(x))/y

res1=(y1-np.sin(x1))/y1

plotwresids(x,y,res,xlabel= "fake data",ylabel="sinish")

plotwresids([x,x1],[y,y1],[res,res1],err=[None,3*np.sqrt(x1)],xlabel= "fake data",ylabel="sinish",scatter=[True,True], color=['k','r'])

pl.show()


