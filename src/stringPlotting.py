#!/usr/bin/python
import sys
import pylab
import numpy
from numpy import sin,cos,tan,sinh,cosh,tanh,arccos,arcsin,arctan,arcsinh,arccosh,arctanh,e,log,log10,sqrt
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot as plt
class Calculus:
    def __init__(self):
        self.color = ['blue','black','red','green','orange','yellow','brown','gray','purple']
        self.maxI = len(self.color) - 1
        self.i = 0
    def plot(self,eq, xAxis):
        if ('=' in eq):
            temp, eq = eq.split('=')
        if('ln' in eq):
            eq = eq.replace('ln','log')
        elif('log' in eq):
            eq = eq.replace('log','log10')

        if('^' in eq):
            eq = eq.replace('^','**')
        xi,xf = xAxis.split('to')
        xf = xf.strip()
        xi = xi.replace('x from', '').strip()
        x = numpy.linspace(int(xi),int(xf),200) # 100 linearly spaced numbers
        y = eval(eq) 

        # compose plot
        #pylab.plot(x,y) # sin(x)/x
        #pylab.plot(x,y,'co') # same function with cyan dots
        #pylab.show() # show the plot
        if self.i > self.maxI:
            self.i = 0
        plt.plot(x, y,color=self.color[self.i],linewidth=1.0)
        self.i =self.i +1
        #plt.plot(x, y,'co')
        #center_spines()
        #plt.axis('equal')
        pylab.grid(True)
        plt.show()

        
