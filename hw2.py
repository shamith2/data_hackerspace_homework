import requests
import re
import matplotlib.pyplot as plt
import numpy as np

x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.]) 
y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])


def visualize():
    # Line Graph
    plt.subplot(2,2,1)
    plt.title("Line Graph")
    plt.plot(x,y, color = "blue")
    
    # Histogram
    plt.subplot(2,2,3)
    plt.title("Histogram")
    plt.hist([x,y], color = ["blue","orange"] , bins = None, rwidth = 0.6)
    
    # Scatter Plot
    plt.subplot(2,2,4)
    plt.title("Scatter Plot")
    plt.scatter(x,y, color = "blue")
    
    # plot
    plt.show()

visualize()