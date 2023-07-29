# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 18:46:17 2014

@author: Natanaël Carpentier
"""

from random import choice
liste_mots=['bonjour','serpent','demain','jambon','fraise','anticonstitutionnellement','technicien','chocolat','chantilly','velociraptor','anthropologie','periple','rapiere','syndicalisme','vampire','necromancien','dragon','canalisation','regicide','fratricide','incandescence','parallelepipede','arachnophile','dodecalogie','compagnon','aquaphobie','drosophile']
mot=choice(liste_mots)
Mot=mot
                               # Question 1:
nb_lettre=0
for i in mot:
    nb_lettre+=1
reponse=nb_lettre*'_ '
mot=list(mot)
Lettre=(True,reponse)
                               # Question 2:
def validation(p,b):
    if b==True:
        return p
    else:
        return p+1
                               # Question 3:
def demandelettre(reponse,mot):
    nb_caract=0
    lettre=input('choisissez une lettre : ')
    for i in lettre:
        nb_caract+=1
    if nb_caract!=1:
        return False 
    Reponse=reponse.split(' ')
    while lettre in mot:
        ind=mot.index(lettre)
        Reponse[ind]=lettre
        mot[ind]='.'
    reponse=''
    for i in Reponse:
        reponse=reponse+i+' '
    if lettre in reponse:
        return [True,reponse]
    else:
        return [False,reponse]
                                # Question 4:
point=0
while point<10:
    print('reponse :',Lettre[1])
    try:
        Lettre=demandelettre(Lettre[1],mot)
        point=validation(point,Lettre[0])
    except:
        point=point+1
    print('fautes :',point)
    if '_' not in Lettre[1]:
        print(Lettre[1])
        print('Gagné')
        break
if point>=10:
    print('Perdu\rLe mot était : ',Mot)