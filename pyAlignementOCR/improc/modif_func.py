import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PIL import Image


def lissage(intensite, N):
    """Fonction calculant la distance entre la colonne de pixels et le
    caractere courant.
    :param intensite : le vecteur des intesites sur la colonne
    :param N : parametre de reglage
    :return : sortielisse
        sortielisse : fonction apres le lissage
    """
    iintensite = intensite.reshape(-1, 1)
    fenetre = np.ones((N, 1))
    longeur, hauteur = iintensite.shape[0], iintensite.shape[1]
    sortie = np.zeros((longeur, 1))
    debut = intensite[0:np.floor(N/2).astype(np.int)]
    fin = intensite[N-np.floor(N/2).astype(np.int)-1:N]
    # to be seen
    if N > 3:
        debut = np.flip(debut)
        fin = np.flip(fin)
    entree = np.concatenate((debut, intensite, fin))
    # to be seen
    M = N - 1
    for j in range(0, longeur):
        sortie[j] = np.dot(entree[j:j+M+1], fenetre)
    return sortie


# TEST DE MODULE
if __name__ == "__main__":
    # test lissage
    img = Image.open('hw.jpg').convert('L')
    hauteur, largeur = img.size
    cimgarray = np.asarray(img, dtype='uint8')
    intensite = np.sum(cimgarray, axis=0)
    srt = lissage(intensite, 3)
    print(srt)
    plt.subplot(211)
    plt.plot(intensite)
    plt.subplot(212)
    plt.plot(srt, color='red')
    plt.show()
