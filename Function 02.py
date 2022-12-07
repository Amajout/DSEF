#Exercice 02
#Ecrire une fonction python qui calcul la factorielle d’un nombre donné n!

n = int(input("Veuillez entrer la valeur de n: "))#Pour savoir la valeur de n
factoriel = 1
if n < 0: #Si n est négatif
   print("On peut pas calculer la factorielle d'un nombré négatif")
elif n == 0: #Si n est nul
   print("La factorielle de 0 est 1")
else:
   for i in range(1,n + 1):
       factoriel = factoriel*i
   print("La factorielle",n,"est",factoriel)

