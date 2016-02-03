
# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n<0:
        raise ValueError()
               
    tot=1
    for i in range(1,n+1):
        tot=tot*i
    return tot


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """

    determinant=b**2-4*a*c

    if determinant<0:
        return (None)
    elif determinant==0:
        return (-b/(2*a))
    else:
        return ((-b+sqrt(determinant))/(2*a),(-b-sqrt(determinant))/(2*a))
    

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """

    #Fonction eval('  ') pour extraire une fonction mathématique d'un string
    #x=3   eval(2x+3) -> 9

    total=0
    pas=0.001
    while lower<=upper:
        x=lower
        total+=pas*eval(function)
        lower+=pas
    return total

if __name__ == '__main__':
    print(fact(3))
    print(roots(1,0,1))
    print(integrate('x ** 2 - 1', -1, 1))
    print(integrate('x+1',1,2))



