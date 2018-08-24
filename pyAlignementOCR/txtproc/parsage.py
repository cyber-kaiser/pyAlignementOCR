import json
from urllib.request import urlopen

j = urlopen('http://panewsarchive.psu.edu/lccn/sn83032041/1878-05-24/ed-1.json')
j_obj = json.load(j)


