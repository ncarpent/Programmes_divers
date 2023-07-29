# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:26:23 2015

@author: Natanaël Carpentier
"""

import numpy as np
from pylab import *





"""
Exercice 1 : création des fonctions utiles pour la suite.
"""
print('               ***  Exercice 1  ***\r\r')





# Question 1 : fonction 'valeur'

def valeur(fichier,debut,longueur):
    fichier.seek(debut)
    val=0
    i=0
    for p in fichier.read(longueur):
        val+=p*256**i
        i+=1
    return val



# Question 2 : fonction 'creer_liste'

def creer_liste(fichier,debut,longueur):
    fichier.seek(debut)
    liste=[]
    for i in fichier.read(longueur):
        liste.append(i)
    return liste



# Question 3 : vérification de 'valeur' et de 'creer_liste'

with open('test.bmp','rb') as fichier:
    print(fichier.read(),'\r\r')
    print('Question 3 :\r\r','taille du fichier : ',valeur(fichier,2,4))
    print('liste taille fichier : ',creer_liste(fichier,2,4))
    print('liste entete fichier : ',creer_liste(fichier,0,14),'\r\r')



# Question 4 : quelques données

    offset=valeur(fichier,10,4)
    nb_lignes=valeur(fichier,22,4)
    nb_colonnes=valeur(fichier,18,4)
    taille=valeur(fichier,34,4)
    liste_pixels=creer_liste(fichier,offset,taille)
    print('Question 4 :\r\r','offset : ',offset)
    print('nb_lignes : ',nb_lignes)
    print('nb_colonnes : ',nb_colonnes)
    print('taille : ',taille)
    print('pixels : ',liste_pixels,'\r\r')


    
# Question 6 : fonction 'sup4' (premier entier supérieur divisible par 4)
    
def sup4(n):
    while n%4!=0:
        n+=1
    return n



# Question 7 : fonction 'matrice_pixels'

def matrice_pixels(fichier):
    offset=valeur(fichier,10,4)
    taille=valeur(fichier,34,4)
    liste_pixels=creer_liste(fichier,offset,taille)
    nb_ligne=valeur(fichier,22,4)
    nl=sup4(nb_ligne)
    nb_colonne=valeur(fichier,18,4)
    nc=sup4(nb_colonne)
    M=np.zeros([nl,nc],int)
    for (m,n) in enumerate(liste_pixels):
        i=m//nc
        j=m%nc
        M[nl-i-1,j]=n
    return M

with open('test.bmp','rb') as fichier:
    M=matrice_pixels(fichier)
    print('Question 7 :\r\rMatrice de pixels :\r\r',M,'\r\r')



# Question 8 : fonction 'liste_entete'

def liste_entete(fichier):
    offset=valeur(fichier,10,4)
    entete=creer_liste(fichier,0,offset)
    return entete

with open('test.bmp','rb') as fichier:
    print('Question 8 :\r\rEntete globale :\r\r',liste_entete(fichier),'\r\r')





"""
Exercice 2 : création d'une image à partir d'un masque simple.
"""
print('             ***  Exercice 2  ***\r\r')





# Question 1 :

def creer_liste_pixels(M):
    liste_pixels=[]
    for i in M:
        liste_pixels=list(i)+liste_pixels
    return liste_pixels

print('Question 1 :\r\rListe de pixels :\r\r',creer_liste_pixels(M),'\r\r')



# Question 2 :

"""
with open('test.bmp','rb') as fichier:
    entete=liste_entete(fichier)
    pixels=creer_liste_pixels(M)
    liste_bmp=entete+pixels

with open('mon_image.bmp','wb') as file:
    file.write(bytearray(liste_bmp))
"""



# Question 3 :

def contour(n,M):
    for j in range(16):
        M[0,j]=n
        M[7,j]=n
    for i in range(8):
        M[i,0]=n
        M[i,15]=n
    return M

def fond(n,M):
    for i in range(1,7):
        for j in range(1,15):
            M[i,j]=n
    return M

def symbole(n,M):
    for i in range(2,6):
        k=i+1
        M[i,2]=n
        M[i,7]=n
        M[i,k]=n
        if i!=2 and i!=5:
            M[i,9]=n
    for j in range(10,14):
        M[2,j]=n
        M[5,j]=n
    return M

def dessin(cadre,bg,wr):
    M2=zeros(shape(M),int)
    M2=contour(cadre,M2)
    M2=fond(bg,M2)
    M2=symbole(wr,M2)
    return M2

M2=dessin(79,0,210)

print('Question 3 :\r\rNouvelle matrice :\r\r',M2)

with open('test.bmp','rb') as fichier:
    entete=liste_entete(fichier)
    pixels=creer_liste_pixels(M2)
    liste_bmp=entete+pixels

with open('mon_image.bmp','wb') as file:
    file.write(bytearray(liste_bmp))






"""
Exercice 3 : Manipulation basique d'image.
"""




"""
# Question 1 :

def extraction(M):
    nb_lignes=valeur(fichier,22,4)
    nl=sup4(nb_lignes)
    nb_colonnes=valeur(fichier,18,4)
    nc=sup4(nb_colonnes)
    SM=M[0:nl-1,0:nc-1]
    return SM

with open('test.bmp','rb') as fichier:
    SM=extraction(fichier)

def mirroir_vertical(M):
"""    









