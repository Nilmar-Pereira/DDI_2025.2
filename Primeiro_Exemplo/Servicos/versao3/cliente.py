import urllib.request, json, time

URL_JOGATINA = "http://127.0.0.1:7001/"
JOGATINA_IS_ALIVE = f"{URL_JOGATINA}alive"
JOGATINA_NOTICIAS = f"{URL_JOGATINA}noticias"

URL_SISTEMAS = "http://127.0.0.1:7002/"
SISTEMAS_IS_ALIVE = f"{URL_SISTEMAS}alive"
SISTEMAS_NOTICIAS = f"{URL_SISTEMAS}noticias"


def acessar(url):
    sucesso, resposta = False, urllib.request.urlopen(url)

    if resposta.code == 200:
        try:
            sucesso, resposta = True, resposta.read().decode("utf-8")
        except Exception as e:
            print(f"erro acessando {url}: {str(e)}")

    return sucesso, resposta

def jogatina_is_alive():
    sucesso, resposta = acessar(JOGATINA_IS_ALIVE)

    return sucesso and resposta == "sim"

def sistemas_is_alive():
    sucesso, resposta = acessar(SISTEMAS_IS_ALIVE)

    return sucesso and resposta == "sim"

def get_jogatina():
    noticias = []
    
    sucesso, resposta = acessar(JOGATINA_NOTICIAS)
    if sucesso:
        noticias = json.loads(resposta)

    return sucesso, noticias

def get_sistemas():
    noticias = []

    sucesso, resposta = acessar(SISTEMAS_NOTICIAS)
    if sucesso:
        noticias = json.loads(resposta)

    return sucesso, noticias

def imprimir_noticias(tipo, noticias):
    print(f"imprimindo notícias de {tipo}")
    for noticia in noticias:
        print(noticia)

if __name__ == "__main__":
    while True:
        if jogatina_is_alive():
            sucesso, noticias = get_jogatina()
            if sucesso:
                imprimir_noticias("jogos eletrônicos", noticias)
            else:
                print("não foi possível acessar notícias sobre jogos")
        else:
            print("serviço de jogatina desligado")

        if sistemas_is_alive():
            sucesso, noticias = get_sistemas()
            if sucesso:
                imprimir_noticias("sistemas operacionais", noticias)
            else:
                print("não foi possível acessar notícias sobre sistemas operacionais")
        else:
            print("serviço de sistemas desligado")

        time.sleep(2)