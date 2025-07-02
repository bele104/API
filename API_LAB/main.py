import requests


def feth_data(endpoint):
    data=requests.get(f"https://rickandmortyapi.com/api/{endpoint}")

    if data.status_code == 200:
        return data.json()
    else :
        return print("deu pau")

print(feth_data("episode"))