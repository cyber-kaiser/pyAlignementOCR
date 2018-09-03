from xml.dom import minidom
from urllib.request import urlopen

def loadxml(url):
    x = urlopen(url)
    xmldoc = minidom.parse(x)
    return xmldoc

data = loadxml('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
print(data)
