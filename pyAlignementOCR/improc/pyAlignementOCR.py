import argparse
import glob
from PIL import Image
import affichage as af
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description="Script qui génère la segmentation correcte des mots (en forme d'image brute) en fonction de la transcription correspondante")
parser.add_argument('imgfolder', help='Nom du fichier d\'entrée ou chemin d\'accès d\'images')
parser.add_argument('transcriptfolder', help='Nom du fichier d\'entrée ou chemin d\'accès de transcripts')
parser.add_argument('--stdout', action='store_true', default=False, help='Détermine le type de sortie (pdf ou écran)')
args = parser.parse_args()

#img = Image.open('hwb.jpg').convert('L')
#transcript = 'emimmin levinnyt'

imglist = []
for filename in glob.glob(args.imgfolder + '/*.jpg'):
    img = Image.open(filename).convert('L')
    imglist.append(img)
transcriptlist = []
for filename in glob.glob(args.transcriptfolder + '/*.txt'):
    file = open(filename, "r") 
    t = file.readline()
    transcriptlist.append(t)
#for i in imglist:
#    i.show()
#for t in transcriptlist:
#    print(t)
f = plt.figure()
if not args.stdout:
    for i in range(len(imglist)):
        plt.subplot(len(imglist),1,i+1)
        af.screen1(imglist[i], transcriptlist[i])
        plt.axis('off')
    f.savefig("resultats.pdf")
else:
    for i in range(len(imglist)):
        plt.subplot(len(imglist),1,i+1)
        af.screen1(imglist[i], transcriptlist[i])
        plt.axis('off')
    plt.show()
