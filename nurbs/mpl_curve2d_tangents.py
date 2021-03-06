# -*- coding: utf-8 -*-

'''
    Visualization example for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018
    Typed by Luix @ UNLV Rebels Cafeteria October 11, 2019 
    while waiting for Soleil from the Make-A-Thon 2.0

    Creates a 2-dimensional curve and plots tangent vectors
'''

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations

import numpy as np 
import matplotlib.pyplot as plt 


# Fix file path 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# Curve Evaluation
#

# Create a BSpline curve instance
curve = BSpline.Curve()

# Set degree
curve.degree = 3

# Set control points 
curve.ctrlpts = exchange.import_txt("ex_curve03.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta 
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# 
# Tangent Vector Evaluation
#

# Store tangent vectors in a list for plotting 
curvetan = []

# Evaluate curve tangent at u = 0.0
ct1 = operations.tangent(curve, 0.0, normalize=True)
curvetan.append(ct1)

# Evaluate curve tangent at u = 0.2
ct2 = operations.tangent(curve, 0.2, normalize=True)
curvetan.append(ct2)

# Evaluate curve tangent at u = 0.5
ct3 = operations.tangent(curve, 0.5, normalize=True)
curvetan.append(ct3)

# Evaluate curve tangent at u = 0.6
ct4 = operations.tangent(curve, 0.6, normalize=True)
curvetan.append(ct4)

# Evaluate curve tangent at u = 0.8
ct5 = operations.tangent(curve, 0.8, normalize=True)
curvetan.append(ct5)

# Evaluate curve tangent at u = 1.0
ct6 = operations.tangent(curve, 1.0, normalize=True)
curvetan.append(ct6)

#
# Control Points, Curve and Tangent Vector Plotting 
# 

# Arrange control points and evaluated curve points for plotting 
ctrlpts = np.array(curve.ctrlpts)
curvepts = np.array(curve.evalpts)

# Convert tangent list into a NumPy array
ctarr = np.array(curvetan)

# Plot using Matplotlib
plt.figure(figsize=(10.67, 8), dpi=96)

# Y-axis line
yaxis = plt.plot((-1, 25), (0, 0), "k-")   

# Control points polygon 
cppolygon, = plt.plot(ctrlpts[:, 0], ctrlpts[:, 1], color='sandybrown', linestyle='-.', marker='o', markersize='3', zorder=0)  

# Evaluated curve points
curveplt, = plt.plot(curvepts[:, 0], curvepts[:, 1], color='lawngreen', linestyle='-', zorder=0)

# Tangents
tanline = plt.quiver(ctarr[:, 0, 0], ctarr[:, 0, 1], ctarr[:, 1, 0], ctarr[:, 1, 1], color='red', angles='xy', scale_units='xy', scale=1, width=0.003, zorder=1)
tanlinekey = plt.quiverkey(tanline, 23.75, -14.5, 35, "Tangent Vectors", coordinates='data', labelpos='W', zorder=1)

# Add legends
plt.legend([cppolygon, curveplt], ["Control Points", "Evaluated Curve"])

# Axis
plt.axis([-1, 25, -15, 15])

# Show Plot 
plt.show()

