from flask import Flask, Response, request
from pymemcache.client import base
import json

VERSAO = "0.0.3"

INFO = {
    "versao": VERSAO,
    "autor": "Luis Paulo da Silva Carvalho",
    "email": "luispscarvalho@gmail.com"
}

BANCO = "banco_sistemas"
PORTA_BANCO = 11211

servico = Flask("noticias")

ALIVE = "sim"

@servico.get("/")
def get_info():
    return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/alive")
def is_alive():
    return Response(ALIVE, status=200, mimetype="text/plain")

@servico.get("/noticias")
def get_noticias():
    sucesso, noticias = False, []

    try:
        conexao = base.Client((BANCO, PORTA_BANCO))
        noticias = conexao.get("noticias")
        if noticias == None:
            noticias = []
        else:
            sucesso = True
        conexao.close()

    except Exception as e:
        print(f"ocorreu um erro recuperando notícias: {str(e)}")
    
    return Response(noticias, status=200 if sucesso else 204, mimetype="application/json")

@servico.post("/gravar")
def gravar_noticias():
    sucesso, noticias = False, request.get_json()

    if noticias:
        try:
            conexao = base.Client((BANCO, PORTA_BANCO))
            conexao.set("noticias", noticias)
            conexao.close()

            sucesso = True
        except Exception as e:
            print(f"ocorreu um erro gravando notícias: {str(e)}")

    return Response(status=201 if sucesso else 422)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=7001, debug=True)