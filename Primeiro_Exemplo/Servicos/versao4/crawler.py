import requests
import json
from time import sleep

NOTICIAS_JOGATINA = "D:\\GitHub\\DDI_2025.2\\Primeiro_Exemplo\\Servicos\\versao4\\noticias\\jogatina.json"
NOTICIAS_SISTEMAS = "D:\\GitHub\\DDI_2025.2\\Primeiro_Exemplo\\Servicos\\versao4\\noticias\\sistemas.json"

URL_JOGATINA = "http://localhost:7001/gravar"
URL_SISTEMAS = "http://localhost:7002/gravar"

def enviar(url, arquivo_noticias):
    sucesso = False

    with open(arquivo_noticias, "r") as arquivo:
        conteudo = json.load(arquivo)
        noticias = conteudo["noticias"]

        arquivo.close()

        resposta = requests.post(url, json=json.dumps(noticias))
        sucesso = resposta.status_code == 201

    return sucesso

if __name__ == "__main__":
    while True:
        sucesso = enviar(URL_JOGATINA, NOTICIAS_JOGATINA)
        if sucesso:
            print("notícias sobre Jogos Eletrônicos enviadas")
        else:
            print("erro enviando notícias sobre Jogos Eletrônicos")

        sucesso = enviar(URL_SISTEMAS, NOTICIAS_SISTEMAS)
        if sucesso:
            print("notícias sobre Sistemas Operacionais enviadas")
        else:
            print("erro enviando notícias sobre Sistemas Operacionais")

        sleep(10)