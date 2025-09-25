# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 19:56:55 2025

@author: Petra Izeboud
"""

import xlwings as xw
import pandas as pd

# Door @xw.func boven de functie te zetten kun je functie aanroepen
# vanuit een cel in excel met de functie naam
# dus in excel: =add_one(Kolommen selectie)
@xw.func
def add_one(data):
    """
    Functie die voor elke cel in de range de cellen +1 teruggeeft. 
    
    Voorbeeld; in excel type je in cel D1 de tekst:  =add_one(A1:B4)
    Dit vult dan de cellen D1:E4 met de waardes van A1:B4 met 1 erbij 
    opgeteld.

    Parameters
    ----------
    data : Excel cellen range 
        Moet bestaan uit minstens twee rijen en minstens 2 kolommen,
        die gevuld zijn met numerieke waarden.

    Returns
    -------
    list
        Waardes die in de cellen range worden ingevoerd.
        Hierbij is de cel waarin de functie wordt aangeroepen de meest
        linker-boven cel.

    """
    return [[cell + 1 for cell in row] for row in data]

@xw.func
def double_sum(x, y):
    """
    Berekent twee keer de waarde van de som van x en y.
    
    Aan te roepen zowel binnen een python script als vanuit een Excel cel.
    Importeer de functies via de xlwings add-in. Type vervolgens de functie
    =double_sum(3,4) in een cel. Geeft output 14. 

    Parameters
    ----------
    x : int, float
        input getal
    y : int, float
        input getal

    Returns
    -------
    int of float
        2 * (x+y)

    """
    return 2 * (x + y)

    
    
    
    