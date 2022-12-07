#Exercice 5
#Ecrire une fonction en Python pour calculer la somme des nombres de 1 à n. 
s= 0
n =int(input("Veuillez entrer un nombre décimal : ")) 
for i in range(0,n+1):
    s = s+i
print("La somme des nombres demandés est : ", s)