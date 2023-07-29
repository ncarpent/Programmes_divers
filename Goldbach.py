# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:48:51 2015

@author: Natanaël Carpentier
"""

# 'Prélude' :

import pylab as py # pour la question 6

def creerdossier(nomdossier):
    from os import mkdir
    try:
        mkdir(nomdossier)
        print('Information : création du fichier',nomdossier)
    except OSError: 
        print('Information : le dossier',nomdossier,'existe déjà')
        pass

def pickle_r(chemin):
    from pickle import load as lire
    with open(chemin,'rb') as fd:
        return lire(fd)

def est_premier(m):
    if m>2:
        p=2
        while p**2<=m:
            if m%p==0:
                return False
            else:
                if p!=2:
                    p+=2
                else:
                    p=3
    elif m==2:
        return True
    else:
        return False
    return True

# Question 2 :

dossier='nb_prem'
fichier='prem-10^5.pick'
chemin=dossier+'/'+fichier
dico=pickle_r(chemin)
liste_prem=dico['nb_prems']

# Question 3 :

def test_som_prem(n):
    if n<0:
        return 'Il faut entrer un nombre positif.'
    i=0
    while liste_prem[i]<=n/2:
        p=liste_prem[i]
        q=n-p
        if est_premier(q):
            return True
        i+=1
    return False

def test_goldbach(m):
    for i in range(4,m+1,2):
        if not test_som_prem(i):
            return 'conjecture erronée à '+str(i)
    return 'conjecture approuvée jusqu\'à '+str(m)

#print(test_goldbach(100000))

"""
La conjecture de Goldbach est vérifiée grâce à cette fonction.
"""

# Question 4 :

def nb_goldbach(m):
    if m<0 or m%2!=0 or m>100000:
        return 'Il faut entrer un nombre pair positif inférieur à 100 000.'
    nb=0
    i=0
    while liste_prem[i]<=m/2:
        p=liste_prem[i]
        q=m-p
        if est_premier(q):
            nb+=1
        i+=1
    return nb

print(nb_goldbach(1000))


# Question 5 :

def liste_goldbach(m):
    liste_pairs=range(4,m+1,2)
    liste_gold=[]
    for i in liste_pairs:
        liste_gold.append(nb_goldbach(i))
    return liste_gold

#print(liste_goldbach(50000))

# Question 6 :

def graph(m):
    liste_x=range(4,m+1,2)
    t_x=py.array(liste_x)
    try:
        liste_y=list()
        for i in range(len(liste_x)):
            liste_y.append(nb_goldbach(liste_x[i]))
        t_y=py.array(liste_y)
    except:
        return 'Il faut entrer un nombre pair positif inférieur à 100 000.'
    py.plot(t_x,t_y,'x')
    py.xlabel('nombres X')
    py.ylabel('nombres de goldbach de X')
    py.axis([0,m,0,1700])
    dossier='Courbe'
    creerdossier(dossier)
    image='Comete_de_Goldbach'
    chemin=dossier+'/'+image
    py.savefig(chemin)
    py.show()

#graph(100000)

# Question 7 :

def nb_goldbach_speed(m):
    if m<0 or m%2!=0 or m>100000:
        return 'Il faut entrer un nombre pair positif inférieur à 100 000.'
    nb=0
    i=0
    sup=0
    while liste_prem[sup]<m:
        sup+=1
    j=sup
    mil=int(sup/2)-1
    while liste_prem[i] <= m/2:
        som=m
        j+=1
        while som>=m and j>=mil:
            som=liste_prem[j]+liste_prem[i]
            if som==m:
                nb+=1
            j-=1
        i+=1
    return nb

def graph_speed(m):
    liste_x=range(4,m+1,2)
    t_x=py.array(liste_x)
    try:
        liste_y=list()
        for i in range(len(liste_x)):
            liste_y.append(nb_goldbach_speed(liste_x[i]))
        t_y=py.array(liste_y)
    except:
        return 'Il faut entrer un nombre pair positif inférieur à 100 000.'
    py.plot(t_x,t_y,'x')
    py.xlabel('nombres X')
    py.ylabel('nombres de goldbach de X')
    py.axis([0,m,0,1700])
    dossier='Courbe'
    creerdossier(dossier)
    image='Comete_de_Goldbach'
    chemin=dossier+'/'+image
    py.savefig(chemin)
    py.show()

#graph_speed(100000)