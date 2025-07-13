import requests
import sqlite3

def fetch_data(topicos,filtros={}):

    URL=f"https://rickandmortyapi.com/api/{topicos}"
   
    try:   
        resposta=requests.get(URL,params=filtros)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.HTTPError as erro_http:
            print("Erro HTTP:", erro_http)
            return None
    except Exception as e:
            print("Erro inesperado:", e)
            return None

 
data=fetch_data("character",{'name':'Rick'})
print("LABA LABA DOOOOOO!!!!!!!!!!!!!!!!!!!!!!!" )
dataRick=sqlite3.connect("DataRick.db")
controleData=dataRick.cursor()
# Cria a tabela
controleData.execute("""
         CREATE TABLE IF NOT EXISTS ricks (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        status TEXT,
        especie TEXT,
        origem TEXT,
        imagem TEXT
    )
""")
if data:
    for personagem in data["results"]:
        id_ = personagem["id"]
        nome = personagem["name"]
        status = personagem["status"]
        especie = personagem["species"]
        origem = personagem["origin"]["name"]
        imagem = personagem["image"]
            

        controleData.execute("""
                INSERT OR IGNORE INTO ricks (id, nome, status, especie, origem, imagem)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id_, nome, status, especie, origem, imagem))

    dataRick.commit()
    print("Ricks inseridos no banco com sucesso!")

    # Fecha conexão
    dataRick.close()