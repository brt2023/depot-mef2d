#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:22:51 2023

@author: barret
"""
import numpy as np


def surfaceTriangle(a,b):
    aire = np.cross(a,b)
    aire = 0.5*aire
    return aire

def MatRaideurElementaire(a,b):
    aire = surfaceTriangle(a,b)
    Kel = np.zeros((3,3))
    Kel = np.dot(a, b)
    Kel = Kel/(4*aire)
    return Kel

def MatMasseElementaire(aire):
    Mel = np.ones((3,3))
    m = len(Mel)
    for i in range(m):
        Mel[i,i] = 2.;
    Mel = Mel/12
    Mel = Mel*aire
    return Mel