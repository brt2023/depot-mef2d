#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:28:21 2023

@author: barret
"""

import matricesElementaires as me


a = [1, 2,-1]
b = [0, 1, 1]
aire = me.surfaceTriangle(a,b)
print("Aire=",aire)

Kel = me.MatRaideurElementaire(aire)
print("Matrice Raideur elementaire (Kel)=",Kel)

Mel = me.MatMasseElementaire(aire)
print("Matrice Masse elementaire (Mel)=",Mel)