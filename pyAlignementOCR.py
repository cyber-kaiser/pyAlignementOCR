import argparse
from pyAlignementOCR.improc import affichage as af


img = Image.open('hwb.jpg').convert('L')
transcript = 'emimmin levinnyt'
af.screen1(img, transcript)

