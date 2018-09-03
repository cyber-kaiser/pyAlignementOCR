import json
from PIL import Image
from urllib.request import urlopen

def loadjson(url):
    j = urlopen(url)
    data = json.load(j)
    return data

def loadimagelist(url):
    imglist = []
    data = loadjson(url)
    canvasnode = data["sequences"][0]["canvases"]
    for page in canvasnode:
        imagenodes = page["images"]
        for image in imagenodes:
            imglist.append(image["rendering"][1]["@id"])
    return imglist

def loadocrxmllist(url):
    ocrxmllist = []
    data = loadjson(url)
    canvasnode = data["sequences"][0]["canvases"]
    for page in canvasnode:
        imagenodes = page["images"]
        for image in imagenodes:
            ocrxmllist.append(image["seeAlso"][0]["@id"])
    return ocrxmllist

def loadocrtxtlist(url):
    ocrtxtlist = []
    data = loadjson(url)
    canvasnode = data["sequences"][0]["canvases"]
    for page in canvasnode:
        imagenodes = page["images"]
        for image in imagenodes:
            ocrtxtlist.append(image["rendering"][2]["@id"]+'ocr.txt')
    return ocrtxtlist




# TEST DE MODULE
if __name__ == "__main__":
    # test de chargement du fichier json
    d = loadjson('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
    # test de chargement d'image
    l = loadimagelist('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
    #for entry in l:
    #    im = Image.open(urlopen(entry))
    #    im.show()
    # test de chargement de fichier xml d'ocr
    #l = loadocrxmllist('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
    l = loadocrtxtlist('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
    for entry in l:
        print(entry)
