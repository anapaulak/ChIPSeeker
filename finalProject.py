#!/usr/bin/env python3



"""Pseudocode:

import sequenceAnalysis as fastAreader
class elegansEnrichment:
	input start, end and summit of gene into program
	read C. elegans genome to find microRNA enrichment 


	def __init__(self):
		self.sequence = sequence






	functions:
	input of chromosone coordinates/summits OR filereader to read coordinates/summits

	potentially make a filereader for C elegans/fastAreader/excel file

	!!! we need to find microRNAs for c elegans
		>create filereader for microRNA distribution

	Plot distribution on chromosome and microRNA distribution on the same graph
	>>smooth curve

		"""

"""
#import matplotlib libary
import matplotlib.pyplot as plt

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
#plot data
plt.plot(x, y, linestyle="solid", marker="o", color="green")
#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

plt.show()
		
"""

import matplotlib.pyplot as plt 
from scipy.ndimage.filters import gaussian_filter1d
import numpy as np 
x = np.arange(65,150,365)
y = np.sin(2*np.pi*x) 

plt.plot(x,y, linestyle = "solid", marker = "o", color = "green")

plt.xlim(0,100)
plt.xticks([0,65,365])

plt.ylim(0,300)
plt.yticks([0,215,0])
#ysmoothed = gaussian_filter1d(y,sigma=2)
plt.plot(x,y)

plt.show()