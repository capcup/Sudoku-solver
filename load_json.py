import urllib.request, json
import os

sudoku_data = 'sudoku_puzzle.json'

def get_puzzle():

    if os.stat(sudoku_data).st_size == 0:
        url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=3&size=9"

        req = urllib.request.Request(url)

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))


        f = open(sudoku_data, "w+")
        json.dump(cont, f)
        f.close()
    else:
        with open(sudoku_data) as json_file:
            cont = json.load(json_file)
    return cont