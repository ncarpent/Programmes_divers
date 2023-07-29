# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 17:10:28 2014

@author: Natanaël Carpentier
"""

from pylab import sqrt
import time


# I- Version brute

# Question 1

"""
divisible=(m%p==0)
"""

# Question 2

def est_premier(m):
    for p in range(2,m):
        if m%p==0:
            return False
    return True

# Question 3

"""
Soit n entier naturel tel que : sqrt(m) < n < m

Si n est composé (non premier), alors il existe p et t entiers naturels tel que
n=p*t

    Si p > sqrt(m) et t > sqrt(m), alors n = p*t > m
    IMPOSSIBLE car contradictoire.
    
    Si p <= sqrt(m) ou t <= sqrt(m), alors il y a deux possibilités :
    
        Soit p*t > m et il y a contradiction, ce qui rend ce cas IMPOSSIBLE
        
        Soit p*t <= m ce qui est le seul cas possible.

Donc si n est composé, l'un des facteurs au moins est inférieurs à sqrt(m).

Ainsi, si tous les entiers inférieurs à sqrt(m) sont testés, tous ceux
supérieurs à sqrt(m) qui ne sont multiple d'aucun nombre déjà testé sont tous
premiers !

On peut donc s'arrêter à l'entier p=int(sqrt(m))
"""

# Question 4

def est_premier2(m):
    for p in range(2,int(sqrt(m)+1)):
        if m%p==0:
            return False
    return True

# Question 5

"""
La complexité asymptotique maximale de la fonction est_premier_bis est
en O(m^(1/2)).
"""

# Question 6

def liste_premiers(n):
    liste=[]
    for i in range(n+1):
        test=est_premier2(i)
        if test:
            liste.append(i)
    return liste

# Question 7





# II- Crible d'Eratosthène

def crible0(n):
    liste_totale=list(range(2,n+1))
    premiers=[]
    while len(liste_totale)>0:
        nb_base=liste_totale[0]
        premiers.append(nb_base) 
        for nb_test in range(nb_base,n+1,nb_base):
            try:
                liste_totale.remove(nb_test) 
            except: 
                pass
    return premiers


# Question 1 : Généralités

# a)

"""
Récurrence totale :

_ On définit P(n):"l_totale[0], à l'étape n,(que l'on notera q(n)) est un
  nombre premier".

_ Initialisation :

    A l'étape 0, l_totale[0]=2 qui est un nombre premier.

_ Hérédité : Soit n entier naturel. On suppose P(0), P(1), ..., P(n).
             Montrons P(n+1).

    A chaque étape de 0 à n, q est premier et l'on supprime tous les multiples
    de q de la liste.
    Donc q(n+1) n'est pas multiple de q(0 à n).
    
    Sachant que, pour tout n, q(n)<q(n+1) (car la liste est rangée en ordre
    croissant), q(n+1) n'est multiple d'aucun entier entre 2 et lui-même.
    
    Donc q(n+1) est un nombre premier.
    
Ainsi, pour tout n entier naturel, P(n) est vrai.

_ Conclusion :

    On a montré par récurrence que l_totale[0] est toujours un nombre premier.

"""

# b)

"""
p(k) : l_totale[0] à l'étape k.
l(k) : l_premiers à la fin de l'étape k.

Soit n un élément de l_totale, inférieur à p(k).

n est soit premier, soit composé (donc multiple d'un nombre premier plus petit
que lui).

_ Si n est composé, n est multiple de p(k-x), x<k.

    Et n est supprimé à l'étape k-x.

_ Si n est premier, l_totale[0]=n à un moment donné.

    Comme n<p(k), n=l_totale[0] à une étape inférieur à k
    (donc n appartient à l_premiers à partir de cette étape).

On a ainsi montré l'invariant de boucle suivant :

l_premiers contiens tous les nombres premiers inférieurs ou égaux à p(k).

"""

# Question 2 : Version naïve

# a)

"""
Cette fonction considére la liste totale des entiers de 2 à n.
Tant que cette liste est non-vide:
Il supprime le premier terme de la liste et le met dans la liste premiers
Puis :

_ l.10: nb_test parcourt la liste des multiples de ce premier terme
    (de nb_base à n+1(exclu) avec un saut de nb_base)

_ l.11 à 14: ¤ le programme supprime nb_test de liste_totale s'il le peut
               (si nb_test appartient à liste_totale)
             ¤ le programme ne fait rien sinon

Au final, ce programme calcule le temps que met la fonction crible pour
s'executer.
"""

#b)

"""
Tant que n est petit (<100), le crible est préférable.
Mais dès que n devient grand(>500), on perd plus de temps avec le crible.
"""

# Question 3 : Version améliorée

# a)

"""
Le crible parcourt la liste avec la boucle for. Et dans cette boucle, il
reparcourt la liste à chaque fois qu'il utilise la fonction remove.
Ceci augmente énormément la complexité.

Le nouveau crible sera moins gourmand car il ne parcourt "qu'une seule fois"
la liste.
(Dans la première boucle, le while devient for ce qui est approximativement
équivalent ici.)
"""

# b)

def crible1(n):
    liste_totale=list(range(2,n+1))
    premiers=[]
    for k in liste_totale:
        if k!=0:
            premiers.append(k)
            for i in range(k,n+1,k):
                liste_totale[i-2]=0      # car index(i)=i-2
    return premiers


# c)

"""
Pour n=50:
_ crible1 : (1.4)*10^-4 s
_ crible0 : (2.0)*10^-4 s
_ liste_premier : (5.9)*10^-4 s

Pour n=500:
_ crible1 : (6.5)*10^-4 s
_ liste_premier : (37.6)*10^-4 s
_ crible0 : (44.2)*10^-4 s

Pour n=10000:
_ crible1 : (7.5)*10^-3 s
_ liste_premier : (95.1)*10^-3 s
_ crible0 : (1729)*10^-3 s

On peut désormais affirmer que, en terme de complexité, crible1 est
l'algorithme le plus léger, tandis que crible0 devient rapidement le plus
lourd !
"""


n=10000

debut=time.clock() 
print('crible1 :\r',crible1(n),'\r')
fin=time.clock()
print('\rProgramme crible1 exécuté en',fin-debut,'secondes\r')


debut=time.clock() 
print('crible0 :\r',crible0(n),'\r')
fin=time.clock()
print('\rProgramme crible0 exécuté en',fin-debut,'secondes\r')


debut=time.clock() 
print('listeprem :\r',liste_premiers(n),'\r')
fin=time.clock()
print('\rProgramme listeprem exécuté en',fin-debut,'secondes\r')




