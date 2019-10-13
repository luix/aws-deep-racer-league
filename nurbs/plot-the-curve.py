from geomdl import BSpline
from geomdl import knotvector

# Create the curve instance
crv = BSpline.Curve()

# Set degree
crv.degree = 2

# Set control points
crv.ctrlpts = [[1, 0, 0], [1, 1, 0], [0, 1, 0]]

# Generate a uniform knot vector
crv.knotvector = knotvector.generate(crv.degree, crv.ctrlpts_size)

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
