'''
    https://gis.stackexchange.com/questions/250784/splitting-a-line-shapefile-into-segments-of-equal-length-in-python

    Splitting a line shapefile into segments of equal length in python
'''


from osgeo import ogr
import math


def _distance(a, b):

    """ Return the distance separating points a and b.

    a and b should each be an (x, y) tuple.

    Warning: This function uses the flat surface formulae, so the output may be
    inaccurate for unprojected coordinates, especially over large distances.

    """

    dx = abs(b[0] - a[0])
    dy = abs(b[1] - a[1])
    return (dx ** 2 + dy ** 2) ** 0.5


def _get_split_point(a, b, dist):

    """ Returns the point that is <<dist>> length along the line a b.

    a and b should each be an (x, y) tuple.
    dist should be an integer or float, not longer than the line a b.

    """

    dx = b[0] - a[0]
    dy = b[1] - a[1]

    m = dy / dx
    c = a[1] - (m * a[0])

    x = a[0] + (dist**2 / (1 
