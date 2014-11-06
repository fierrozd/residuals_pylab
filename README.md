self explainatory: 

it makes a classical residual plot, with the residuals at the bottm and the data in the top panel. 
each plot can be scatter plot, line plot and the data can be errorbars

try it as follows




import numpy as np

import pylab as pl

from residplot import plotwresids

#get 100 random numbers b/w 0 and 10
x=np.random.rand(100)*10

#get the y as sine(x) plus some linear function of x with some scatter
y=np.sin(x)+0.3*(np.random.rand(100)-0.5)*np.sqrt(x)

#get another array of 100 random numbers b/w 0 and 10
x1=np.random.rand(100)*10

#get the y for the second set as sine(x) plus some linear function, steeper this time, of x, with some scatter
y1=np.sin(x1)+(np.random.rand(100)-0.5)*np.sqrt(x1)

#get the residuals of a simple sine fit function (not a fit, just the sin(x))
res=(y-np.sin(x))/y

res1=(y1-np.sin(x1))/y1

#and finally plot it
plotwresids(x,y,res,xlabel= "fake data",ylabel="sin-ish", legend="made up stuff")

plotwresids([x,x1],[y,y1],[res,res1],err=[None,np.sqrt(np.sin(x1))],xlabel= "fake data",ylabel="sin-ish",scatter=[True,True], color=['SteelBlue','DarkOrange'], legend=["madeup stuff","more madeup stuff"])

pl.show()


