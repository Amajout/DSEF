# import des bilbio

import math 

print(" resoudre equation a x^2 + bx + c  = 0")

a = float(input("entrez la valeur de a : "))
b = float(input("entrez la valeur de b : "))
c = float(input("entrez la valeur de c : "))



# calculer le delta 

delta = b * b - 4 * a * c

print("le Delta :" ,delta )

if( delta > 0 ):
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)

    print( " deux solutions x1 et x2")
    print(" x1 = " , x1)
    print("x2 = " , x2)

if(delta == 0 ):
    x0 = -b/(2 * a)
    print( " une seule solution x 0")
    print("x0 = " , x0 )
   

if( delta <  0 ):
    print(" deux solution x1 et x2 complexes  ")

    x1_reel = -b/(2 * a)
    x1_imaginaire = math.sqrt(-delta)/(2*a)
    print("x1 = %f + %f i"  % (x1_reel , x1_imaginaire))

    print("x2 = %f - %f i"  % (x1_reel , x1_imaginaire))








