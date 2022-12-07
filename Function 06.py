#Exercice 6
#Ecrire une fonction en Python pour compter les chiffres d'un nombre donné. 
n =int(input("Veuillez entrer un nombre: ")) 
chiffre = 0
while n != 0 :
    n = n//10
    chiffre = chiffre+1
print("Le nombre que vous avez entré contient", chiffre , "chiffres" )