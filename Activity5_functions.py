"""

name: Activity5_functions.py

This program calculates interatomic potential repulsion

ToDo: Create one or more user-defined functions that increase the 
usability and readability of this code. 


author: M.P. Kuchera
date created: 2/7/2021

"""

# imports
import numpy as np

# user-defined functions

    
    
# main function
def main():
    a0 = 0.529e-10 # Bohr radius in m
    eps = 8.854E-12 # permittivity of free space
    q = 1.602e-19 # 
    Z1 = 2 # charge of atom 1
    Z2 = 4 # charge of atom 2
    
    Rs = np.linspace(1e-15,1e-10,100)
    Vs = np.zeros(len(Rs))
    
    # calculate interatomic potentials across a range of distances
    for r in Rs:
        a = 0.8854*a0/(Z1**0.23 + Z2**0.23)
        x = r/a
        phi = 0.1818*np.e**(-3.2*x) + 0.5099*np.e**(-0.9423*x)+ 0.2802*np.e**(-0.4028*x) + 0.02817*np.e**(-0.2016*x)

        V = 1/(4*np.pi*eps)*Z1*Z2*q**2*phi/r
        print("Potential at r =", str.format('{0:.3e}',r), "is", str.format('{0:.3e}',V), "Joules.")

        

# call main IFF we are executing *this* file
if __name__ == "__main__":
    main()