import numpy as np
import scipy as sp
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import modif_func as mf
import alignement as al


def screen1(image, transcript):
    largeur, hauteur = image.size
    plt.imshow(image)
    sgm = al.segmenter(image, transcript, 3, 0.1, 0.9, 0)
    for x in range(0, largeur-1):
        if sgm[x] == 2:
            plt.plot([x, x], [1, hauteur], color='red')
        elif sgm[x] == 1:
            plt.plot([x, x], [1, hauteur], color='blue')
    #plt.show()

def afficherprofile(image, transcript, noir, gris, blanc):
    largeur, hauteur = image.size
    profil = creermasque(transcript, largeur, noir, gris, blanc)
    masqueimg = Image.fromarray(np.uint8(profil))
    masqueimg.show()

def affichercontour(image, transcript):
    largeur, hauteur = image.size
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(image)
    sgm = al.segmenter(image, transcript, 3, 0.1, 0.9, 0)
    for x in range(0, largeur-1):
        if sgm[x] == 2:
            ax.plot([x, x], [1, hauteur], color='red')
            first = x
            i = first - 1
    rect = patches.Rectangle((i,1),x-first,hauteur,linewidth=2,edgecolor='b',facecolor='none')
    ax.add_patch(rect)
    plt.show()
# TEST DE MODULE
if __name__ == "__main__":
    # test d'affichage
    img = Image.open('hwb.jpg').convert('L')
    transcript = 'emimmin levinnyt'
    #screen1(img, transcript)
    affichercontour(img, transcript)
