#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:08:24 2023

@author: barret

   *****************************
   * RESOLUTION  de l'EQUATION:
     Pb de Dirichlet homogene
     
    -u''(x) + alpha(x)*u(x) = f(x)      qq x in [a,b]
    u(a) = u(b) = 0                     CL
    
    par la MEF 1D
   ***************************** 


"""



import numpy as np


def matriceRaideurElementaire(h):
    Kel = -np.ones((2,2))
    #Kel = np.diag([-1,-1])
    for i in range(2):
        Kel[i,i] = 1.0
    Kel = Kel/h
    return Kel


def matriceMasseElementaire(h):
    Mel = np.ones((2,2))
    for i in range(2):
        Mel[i,i] = 2.0
    Mel = Mel/6
    Mel = h*Mel
    return Mel

def f(x):
    return x**2 #np.cos(x)

def secondMembre(h, f, xi, i):
    x0 = xi
    x1 = xi + h
    Fel = (h/2)*(f(x0) + f(x1)) # methode des trapezes pour les polynomes de degre 1
    return Fel


# pas d'espace
a = 0.0;b = 1.0
nx = 50   #nbre de pts
h = (b-a)/(nx-1)

x = np.linspace(a, b, nx)






# matrice Raideur elementaire
Kel = matriceRaideurElementaire(h)
# matrice Masse   elementaire
Mel = matriceMasseElementaire(h)

# vecteur Second Membre
F = np.zeros((nx,1))
for i in range(nx):
    xi = x[i]
    Fel = secondMembre(h, f, xi, i)
    F[i,0] = Fel

A = np.zeros((nx,nx))
for K in range(nx):
    for II in range(2):
        for JJ in range(2):
            I = K + II-2
            J = K + JJ-2
            A[I,J] += Kel[II,JJ] + Mel[II,JJ]


# RESOLUTION du systeme lineaire A*U = F
U = np.linalg.solve(A, F)

import matplotlib.pyplot as plt
plt.plot(x,U,label='U',c='r')
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('U(x)')
print(U)





