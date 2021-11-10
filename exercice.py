#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import pandas as pd


# TODO: Définissez vos fonctions ici
def lire_fichier():
    return pd.read_csv(r'C:\Users\selam\Documents\GitHub\c04-ch10-2-exercices-Selamet53\data\winequality-white.csv', delimiter=";")


def trouver_attribut_cible():
    df = lire_fichier()
    return df["quality"], df[df.columns.difference(["quality"])]


#def ...


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #print(lire_fichier())
    print(trouver_attribut_cible())
