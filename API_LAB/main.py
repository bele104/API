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



def criarTabela(controleData):

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
   
def inserirData(controleData, data, dataRick):
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



def abrirEfechar (dataRick):
    dataRick.commit()
    print("Ricks inseridos no banco com sucesso!")

    # Fecha conexão
    dataRick.close()



def bancoConecta(banco="DataRick.db"):
    dataRick=sqlite3.connect(banco)
    controleData=dataRick.cursor()
    return dataRick, controleData


def main():

    print("LABA LABA DOOOOOO!!!!!!!!!!!!!!!!!!!!!!!" )
    data=fetch_data("character",{'name':'Beth'})
    if data:
         dataRick, controleData =bancoConecta()
         criarTabela(controleData)
         inserirData(controleData,data,dataRick)
         abrirEfechar (dataRick)
         print(data)
    else: 
        print("erro")  


# Executa o código
if __name__ == "__main__":
    main()

    