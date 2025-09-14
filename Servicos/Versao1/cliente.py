import urllib.request, json, time

URL_SERVICO = "http://127.0.0.1:500/"
IS_ALIVE = f"{URL_SERVICO}alive"
JOGATINA = f"{URL_SERVICO}jogatina"
SISTEMAS = f"{URL_SERVICO}sistemas"

def acessar(url):
    sucesso, resposta = False, urllib.request.urlopen(url)
    
    if resposta.code == 200:
        try:
            sucesso, resposta = True, resposta.read().decode("utf-8")
        except Exception as e:
            print(f"erro acessando (url): {str(e)}")
            
    return sucesso, resposta