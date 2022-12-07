#Exercice 4
#Ecrire une fonction en Python pour convertir le nombre décimal en nombre binaire. 

n =int(input("Veuillez entrer un nombre décimal : ")) #savoir le nombre décimal
b = 0
ordre = 0
while n != 0 :
    reste = n%2
    p = 10**ordre
    b= b+ reste * p
    ordre = ordre + 1
    n = n//2
print (b)