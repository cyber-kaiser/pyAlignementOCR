import numpy as np
import scipy as sp
import matplotlib as mpl
from PIL import Image

options = {1: 'sub',
           2: 'ins',
           3: 'des'}


def segmenter(image, transcript, lissage, limitesup, limiteinf, affichage):
    """Fonction responsable pour la segmentation d'image.
    :param image : l'image a segmenter
    :param transcript : le transcript qui correspond a l'image en question
    :param lissage : le parametre de lissage voulu
    :param limitesup : une limite qui sera utilise afin de couper l'image
    :param limiteinf : une limite qui sera utilise afin de couper l'image
    :param affichage : controle le type d'affichage
    """
    #  on convertit en niveaux de gris l'image et on le reduit ensuite
    img = image.convert('gray')
    hauteur, largeur = img.size
    cimg = reduire(img, limitesup, limiteinf)
    hauteur, largeur = cimg.size
    longeurtext = len(transcript)
    # on convertit l'image dans un tableau avec des valeurs
    # d'intensite dans [0,255]
    cimarray = np.asarray(cimg, dtype='uint8')
    # on calcule les intensites moyennes sur les colones de pixels sur
    # l'image et le profil(masque) d'image
    intensite = np.sum(cimarray, axis=1)
    intensitemax = np.amax(cimarray, axis=1)
    indexmax = np.argmax(cimarray, axis=1)
    intensitemin = np.amin(cimarray, axis=1)
    indexmin = np.argmin(cimarray, axis=1)
    intensitelisse = mf.lissage(intensite, lissage)
    # on definie les couleurs de notre masque
    blanc = np.floor(np.sum(intensitemax)/largeur)
    noir = np.floor(np.sum(intensitemin)/largeur)
    gris = (blanc + noir) / 2
    # creation de la masque/profil d'intensite de la ligne
    profil = creermasque(longeurtext, hauteur, largeur, noir, gris, blanc)
    profil = np.sum(profil, axis=1) / hauteur
    # on seuil les valeurs basses de l'intensit? lisse pour les ramener
    # a la valeur moyenne des noirs
    for i in range(1, largeur):
        if intensitelisse[i] < noir:
            intensitelisse[i] = noir
    intensite = intensitelisse
    x = largeur
    y = largeurprofil
    # tbc
    appariement = np.zeros((x, y))
    precedent = np.zeros((x, y))
    segmentation = np.zeros((x, 1))

    # initialisation de la premiere ligne
    appariement[1, 1] = np.abs(intensite[1] - profil[1])
    precedent[1, 1] = 0

    for i in range(2, x):
        appariement[x, 1] = appariement[x-1, 1] + np.abs(intensite[i]
                                                         - profil[1])
        precedent[i, 1] = insertion
    # tbc
    for i in range(2, y):
        appariement[1, y] = appariement[1, y-1] + np.abs(intensite[1]
                                                         - profil[i])
        precedent[1, y] = destruction
    # on boucle sur toute l'image et toute la sequence des caracteres
    for i in range(2, x):
        for j in range(2, y):
            operations[substitution] = appariement[x-1, y-1] + np.abs(
                                                               intensite[i]
                                                               - profil[j])
            operatios[insertion] = appariement[x-1, y] + 2*np.abs(
                                                         intensite[i]
                                                         - profil[j])
            operations[destruction] = appariement[x, y-1] + 2*np.abs(
                                                            intensite[i]
                                                            - profil[j])
            appariement[i, j] = np.min(operations)
            precedent[i, j] = np.min(operations)
    # on est arrive a la fin, on backtrack afin de choisir le meilleur
    # chemin et marquer les espaces entre les mots
    x = X
    y = Y
    while (precedent[x, y] != 0):
        x, y, precedent, segmentation = options[sub](x, y, precedent,
                                                     segmentation)
        x, y, precedent, segmentation = options[ins](x, y, precedent,
                                                     segmentation)
        x, y, precedent, segmentation = options[des](x, y, precedent,
                                                     segmentation)


def creermasque(longeurtranscript, hauteurimg, largeurimg, carclr, wsclr,
                boxclr):
    """Fonction qui cree une masque/profil pour compare avec l'image donne
    :param transcript : le transcript qu'on utilise pour creer la masque
    :param hauteurimg : hauteur de l'image a comparer
    :param largeurimg : largeur de l'image a comparer
    :param carclr : couleur de la masque d'un caractere
    :param wsclr : couleur des espaces blanches
    :param boxclr : couleur de la phrase/mot entiere
    :return profil
        profil : la masque derive du transcript correspondant aux niveaux
        d'intensite de l'image
    """
    largeurcaractere = np.floor(largeur/longeurtext)
    profilcaractere = np.ones((hauteur, largeucaractere)) * carclr
    largeurprofil = largeurcaractere * longeurtext
    profil = np.ones((hauteur, largeurprofil)) * boxclr
    # ici on genere l'allure de la masque
    debut = 1
    fin = largeurcaractere
    for i in range(debut, longeurtext):
        if transcript[i] != ' ':
            profil[:, debut:fin] = profilcaractere[:, :]
        debut = debut + largeurcaractere
        fin = fin + largeurcaractere
    # profilimg = Image.fromarray(np.uint8(profil))
    return profil


def reduire(image, limitesup, limiteinf):
    """reduit l'image par un limite donne
    :param image : l'image a reduire
    :param limitesup : une limite qui sera utilise afin de couper l'image
    :param limiteinf : une limite qui sera utilise afin de couper l'image
    """
    hauteur, largeur = image.size
    img = image.crop(0, np.floor(limitesup*hauteur)+1,
                     largeur, hauteur - floor(limiteinf*hauteur))
    return img


def sub(x, y, precedent, segmentation):
    if precedent[x, y] == 1:
        x = x - 1
        y = y - 1
        if (profil[y] == blanc):
            segmentation[x] = 2
        elif profil[y] == gris:
            segmentation[x] = 1
    return x, y, precedent, segmentation


def ins(x, y, precedent, segmentation):
    if precedent[x, y] == 2:
        x = x - 1
        if profil[y] == blanc:
            segmentation[x] = 2
        elif profil[y] == gris:
            segmentation[x] = 1
    return x, y, precedent, segmentation


def des(x, y, precedent, segmentation):
    if precedent[x, y] == 3:
        y = y - 1
    return x, y, precedent, segmentation


# TEST DE MODULE
if __name__ == "__main__":
    print('hello world')
