#Réalisé par: Junior Kossivi le 12/05/2025 à 12:44:23 à Port-Bouet, Abidjan, Côte d'Ivoire, Université Félix Houphouët-Boigny
#Version 1.0


#Bibliothèque de codes utiles (Procédures)en Python

import math
import random

# Procédure Mot de passe
"""mot = "lic2mi"
n=3
while(n != 0):
    print("Vous avez",n,"chance")
    temp = input("Entrez votre mot de passe: ")
    if (mot == temp):
        print("Mot de passe Correct!!!")
        break
    if n==0:
        print("Vous êtes bloqué !!!")
        break
    if (mot != temp):
        print("Mot de passe Incorrect,Réessayer!!!")
        n-=1"""

#Calculatrice de nombre complexe
"""print("CALCULATRICE DE NOMBRE COMPLEXE")
a_r = float(input("La partie réelle de a : "))
a_i = float(input("La partie imaginaire de a  : "))
b_r = float(input("La partie réelle de b : "))
b_i = float(input("La partie imaginaire de b : "))

print("1.Addition, 2.Soustraction, 3.Division ,4.Multiplication ,5.module, 6.Carré")
operation = int(input("Quelle Opération vous souhaitez ? : "))

if operation == 1:
    resultat = complex(a_r + b_r,b_i + a_i)
    print(resultat)
elif operation == 2:
    resultat = complex(a_r - b_r,b_i - a_i)
    print(resultat)
elif operation == 4:
    resultat = complex(a_r*b_r - a_i*b_i,a_r * b_i + a_i*b_r)
    print(resultat)
elif operation == 3:
    resultat = complex((a_r*b_r + a_i*b_i)/(b_r**2 + b_i**2) , (a_i * b_r - a_r*b_i)/(b_r**2 + b_i**2))
    print(resultat)
elif operation == 5:
    resultat = math.sqrt(a**2 + b**2)
    print(resultat)
elif operation == 6 :
    resultat = complex(a**2 - b**2, 2*a_r*b_r)
    print(resultat) """
    
"""#procédures base de données
n = int(input("Le nombre de valeur à saisir : "))

contact = []
for i in range(n):
    index = i+1
    nom = str(input("Nom et prenoms : "))
    numero = str(input("Numero de téléphone : "))
    contact.append({"Index":index,
                    "Nom":nom,
                    "Numero":numero})
#pour enregistrer dans un txt

with open("repertoire.txt",'w',encoding="utf-8") as f:
    f.write("Les contacts saisies")
    for c in contact:
        ligne = f"{c['Index']}. {c['Nom']} - {c['Numero']}\n"
        f.write(ligne)
print("Les contacts ont été enregistrés dans le fichier repertoire.txt")

#pour lister les éléments
for c in contact:
    print(c)
#pour rechercher un contact
search = str(input("'l'element à cherché : "))
ok = False
for c in(contact):
    if search in c["Nom"] or search in c["Numero"] :
        ok = True
        print("Contact trouvé : ", c)
if c == False:
    print("Contact Non trouvé")"""

 #pour supprimer un élément
"""suppr = str(input("Elément à supprimer: "))
for c in(contact):
    if suppr in c["Nom"] or suppr in c["Numero"] :
        contact.remove(c)
#pour modifier un contact
move = str(input("Elément à modifier: "))
modif = str(input("Elément à ajouter: "))
for c in(contact):
    if move in c["Nom"]:
        c["Nom"] = modif
    if move in c["Numero"]:
        c["Numero"] = modif
"""
    


#procédures de calculs le montant des heures supplémentaires d’un employé

"""nb = int(input("Le nombre d'heures travaillées : "))
prix = float(input("prix unitaire"))
total = 0
if nb<40:
    total = (39*prix)
elif nb>=40 and nb<44:
    total = (39*prix) + (nb-39)*(1.5*prix)
elif nb>=45 and nb<49:
    total = (39*prix) + 5*prix*1.5 +(nb-44)*1.75*prix
elif nb>=50:
    total = (39*prix)+(5*prix*1.5)+(5*prix*1.5)+(nb-49)*prix*2
    
print(total)"""

#procedure heure

"""heure = int(input("L'heure :"))
minutes = int(input("Minutes"))

if heure<23:
    if minutes<59:
        minutes +=1
        heure +=0
    else :
        heure +=1
        minutes = 00
else:
    if minutes <59:
        minutes +=1
        heure +=00
    else :
        minutes = 00
        heure = 00

print("Il est",heure,"h :",minutes,"minutes")"""

#Suite Un avec 3<U0<40, Un = Un-1/2 si Un-1 paire, Un = 3Un-1 +1 sinon
"""def calculRang():
    u0 = random.randrange(3, 40)
    pos = 1
    Un=0
    print(u0)
    while u0!=4:
        if u0%2==0:
            Un = u0//2
        else :
            u0=Un
            Un=(3*u0)+1
        pos +=1
    return pos
    
print(calculRang())"""

#suite U0=2, Un+1 = Un +2/Un, n>0
"""def calcSuite(epsilon):
    u0=2
    Un=0
    while abs(Un-u0)>epsilon:
        u0=Un
        Un=(u0+2)/u0
    return Un"""

#Suite F0=1, F1=2, Fn= 4Fn-1 + 3Fn-2, n>=2

"""def Calcsuit(n):
    u0,u1 = 1,2
    for i in range(2,n):
        Un = 4*u1+3*u0
        u0=u1
        u1=Un
    return Un

print(Calcsuit(5))"""

#suites Un= 1 si n<2 sinon Un=3Un-1 + Un-2

"""def Un(n):
    if n<2:
        return 1
    else :
        return 3*Un(n-1)+Un(n-2)

print(Un(5))"""

#suites composé de système u0=a v0=b et pour tout n>0 Un = (Un-1)² + 2Vn-1 et Vn = Vn-1 + 3Un-1
"""def Un(a,b,n):
    if n==0:
        return a
    else:
        return (Un(a,b,n-1))**2 + 2*Vn(a,b,n-1)
    
def Vn(a,b,n):
    if n==0:
        return b
    else:
        return Vn(a,b,n-1) + 3*Un(a,b,n-1)

print(Un(1, 3, 2))"""


#procédure examen
"""notes =[]
somme = 0
for i in range(3):
    a = float(input(f"Notes{i+1} : "))
    notes.append(a)

for j in range(3):
    somme += notes[j]
moyenne = somme/3

if notes[0]>=9 and notes[1]>=9 and notes[2]>=9:
    print("Admis")
elif moyenne>=0 and min(notes)>=8:
    print("admis")
else:
    print("Refusé")"""
    
#Procédure division

"""a = int(input("Valeur 1 : "))
b = int(input("Valeur 2 : "))

if b == 0:
    raise ValueError("Erreur division par Zéro")
else:
    print("Le quotient est : ",a/b)
    print("le reste est : ", a%b)"""
    

#Procédure absolu
"""a = int(input("Valeur 1 : "))
b = int(input("Valeur 2 : "))

if abs(a)>abs(b):
    print(abs(a))
else :
    print(abs(b))"""