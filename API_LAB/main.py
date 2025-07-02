import requests


def feth_data(topicos,filtros={}):

    URL=f"https://rickandmortyapi.com/api/{topicos}"
    data=requests.get(URL, params=filtros)

    if data.status_code == 200:
        return data.json()
    else :
        return print("LABA LABA DOOOOOO!!!!!!!!!!!!!!!!!!!!!!!")

print(feth_data("character",{'name':'Rick'}))