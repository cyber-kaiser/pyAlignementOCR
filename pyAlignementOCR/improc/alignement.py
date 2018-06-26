import numpy as np
import scipy as sp
import matplotlib as mpl
from PIL import Image


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

