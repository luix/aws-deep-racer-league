'''
    Self-Driving Cars Lab
    Nikolay Falaleev

    https://nikolasent.github.io/mathematics/algorithms/2017/05/02/Approximate-equidistant-curve-for-polynomials.html

    Approximate equidistant curve for polynomials
'''
import numpy as np
import matplotlib.pyplot as plt

# Calculate a polinomial value in a given point x
def pol_calc(pol, x):
    pol_f = np.poly1d(pol)
    return(pol_f(x))

# Create original line text equation for a plot legend
def text_eq(pol):
    str_eq = 'Original line\ny = ' 
    j = 1
    for i,p in enumerate(pol):
        print(p)
        str_eq += str(p)
        order = len(pol)-j
        if order > 1:
            str_eq += ('x^'+str(order))
            if pol[i+1] > 0:
                str_eq += '+'
        elif order > 0:
            str_eq += ('x')
            if pol[i+1] > 0:
                str_eq += '+'
        j += 1
    return str_eq

#Calculate approximated equidistant to a parabola
EQUID_POINTS = 20 # Number of points to use for the equidistant approximation

def equidistant(pol, d, max_l = 1, plot = False):
    x_pol = np.linspace(0, max_l, num=EQUID_POINTS) # Reference curve points
    y_pol = pol_calc(pol, x_pol)
    x_m = [] # Mid points
    y_m = []
    k_m = []
    # Calculate polints position between given points
    for i in range(len(x_pol)-1):
        y_m.append((y_pol[i+1]-y_pol[i])/2.0+y_pol[i])
        x_m.append((x_pol[i+1]-x_pol[i])/2.0+x_pol[i])
        # Slope of perpendicular lines
        if y_pol[i+1] == y_pol[i]: #Avoid division by 0
            k_m.append(1e8) # A vary big number
        else:
            k_m.append(-(x_pol[i+1]-x_pol[i])/(y_pol[i+1]-y_pol[i])) # Slope of a perpendicular
    # Convert arrays into np.arrays
    x_m = np.array(x_m)
    y_m = np.array(y_m)
    k_m = np.array(k_m)
    # Calculate equidistant points
    x_eq = d*np.sqrt(1.0/(1+k_m**2)) # Calculate reference shift dx of the equidistant points
    y_eq = np.zeros_like(x_eq) # Create np.array for y_eq
    if d >= 0: # x positions of the equidistant depends on direction
        for i in range(len(y_m)):
            if k_m[i] < 0: 
                x_eq[i] = x_m[i]-abs(x_eq[i])
            else:
                x_eq[i] = x_m[i]+abs(x_eq[i])
            y_eq[i] = (y_m[i]-k_m[i]*x_m[i])+k_m[i]*x_eq[i]
    else:
        for i in range(len(y_m)):
            if k_m[i] < 0:
                x_eq[i] = x_m[i]+abs(x_eq[i])
            else:
                x_eq[i] = x_m[i]-abs(x_eq[i])
            y_eq[i] = (y_m[i]-k_m[i]*x_m[i])+k_m[i]*x_eq[i]
    # Fit a polinomial of order which is the same to the given one to the equidistant points 
    pol_eq = np.polyfit(x_eq, y_eq, len(pol)-1)
    # Visualize results
    if plot:
        # Original line
        plt.plot(x_pol, y_pol, color='red', linewidth=1, label = text_eq(pol)) 
        # Equidistant
        plt.plot(x_eq, y_eq, color='green', linewidth=1, label = 'Equidistant, d = '+ str(d))
        #Approximation
        plt.plot(x_pol, pol_calc(pol_eq, x_pol), color='blue',
                 linewidth=1, label = 'Approximation') 
        plt.legend() # Add legend
        plt.axis('equal')
        # Draw black connection lines
        for i in range(len(x_m)):
            plt.plot([x_m[i],x_eq[i]], [y_m[i],y_eq[i]], color='black', linewidth=1) 
        plt.show()
        #plt.savefig('./equid.jpg')
    return pol_eq

# Use example
pol = np.array([-4.0, 5.5,  -2.5,  0.2])
print(equidistant(pol, -0.1, plot=True))




