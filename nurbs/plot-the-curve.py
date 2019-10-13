from geomdl import BSpline

# Create the curve instance
crv = BSpline.Curve()

# Set degree
crv.degree = 2

# Set control points
crv.ctrlpts = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]

# Set knot vector
crv.knotvector = [0, 0, 0, 1, 1, 1]

# Import Matplotlib visualization module
from geomdl.visualization import VisMPL

# Set the visualization component of the curve
crv.vis = VisMPL.VisCurve3D()

# Plot the curve
crv.render()

'''
    Convert non-rational to rational curve
    
    Generates a B-Spline (non-rational) curve and converts it 
    into a NURBS (rational) curve.
'''
from geomdl import convert      # Import convert module

# B-Spline to NURBS
crv_rat = convert.bspline_to_nurbs(crv)
