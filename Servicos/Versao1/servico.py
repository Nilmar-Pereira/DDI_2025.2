from flask import Flask, Response
import json

VERSAO = "0.0.1"
INFO = {
    "versão": VERSAO,
    "author": "Nilmar Pereira Sousa",
    "email": "nilmar.pereira16@outlook.com"
}

JOGATINA = [
    {
        "id": 1,
        "data": "15/10/2019",
        "titulo": "Stadia, serviço de games na nuvem do Google, será lançado em 19 de Novembro",
        "endereco": "https://g1.globo.com/pop-arte/games/noticia/2019/10/15/stadia-servico-de-games-na-nuvem-do-google-sera-lancado-em-19-de-novembro.ghtml",
    },
    {
        "id": 2,
        "data": "26/04/2019",
        "titulo": "Mortal Kombat: Como fazer todos os fatalities?",
        "endereco": "https://www.uol.com.br/start/ultimas-noticias/2019/04/26/mortal-kombat-11-como-fazer-todas-as-fatalities.htm",
    },
    {
        "id": 3,
        "data": "21/10/2016",
        "titulo": "Conheça 5 distribuições GNU/Linux voltadas para jogos",
        "endereco": "https://sempreupdate.com.br/conheca-5-distribuicoes-gnu-linux-voltadas-para-jogos/",
    }
]

SISTEMAS = [
    {
        "id": 1,
        "data": "22/05/2019",
        "titulo": "Estes são os 12 problemas já encontrados na atualização do Windows 10",
        "endereco": "https://olhardigital.com.br/noticia/microsoft-lista-todos-os-problemas-da-nova-atualizacao-do-windows-10/86052",
    },
    {
        "id": 2,
        "data": "10/05/2015",
        "titulo": "Atualização do Windows 10 está causando problemas para alguns usuários",
        "endereco": "https://canaltech.com.br/windows/atualizacao-do-windows-10-esta-causando-problemas-para-alguns-usuarios-46921/",
    },
    {
        "id": 3,
        "data": "04/05/2016",
        "titulo": "Top 5 distribuições Linux que podem substituir o Windows 10",
        "endereco": "https://pplware.sapo.pt/linux/top-5-distribuies-gnulinux-que-podem-substituir-o-windows-10/",
    }
]

servico = Flask("noticias")

ALIVE = "sim"

@servico.get("/")
def get_info():
    return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/alive")
def is_alive():
    return Response(ALIVE, status=200, mimetype="text/plain")

@servico.get("/jogatina")
def get_jogatina():
    return Response(json.dumps(JOGATINA), status=200, mimetype="application/json")

@servico.get("/sistemas")
def get_sistema():
    return Response(json.dumps(SISTEMAS), status=200, mimetype="application/json")

if __name__== "__main__":
    servico.run(host="0.0.0.0", debug=True)