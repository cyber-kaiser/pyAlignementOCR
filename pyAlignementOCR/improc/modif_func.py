import numpy as np
import matplotlib as mpl
from PIL import Image


def lissage(intensite, N):
    """Fonction calculant la distance entre la colonne de pixels et le
    caractere courant.
    :param intensite : le vecteur des intesites sur la colonne
    :param N : parametre de reglage
    :return : sortielisse
        sortielisse : fonction apres le lissage
    """
    fenetre = np.ones((N, 1))
    hauteur, longeur = size(intensite)
    sortie = np.zeros((N, 1))
    debut = intensitex[1:np.floor(N/2)]
    fin = intensite[N-np.floor(N/2)+1:N]
    # to be seen
    if N > 3:
        debut = np.flip(debut)
        fin = np.flip(fin)
    entree = np.concatenate(debut, intensite, fin)
    # to be seen
    M = N - 1
    for j in range(1, longeur):
        sortie[j] = entree[j:j+m] * fenetre

