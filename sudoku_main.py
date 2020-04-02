
import urllib.request, json

#url = "http://www.cs.utep.edu/cheon/ws/sudoku/info/?size=4"

url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=3"

req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))



print(cont)
