import urllib.request, json, time

URL_SERVICO = "http://127.0.0.1:7001/"
IS_ALIVE = f"{URL_SERVICO}alive"
JOGATINA = f"{URL_SERVICO}jogatina"
SISTEMAS = f"{URL_SERVICO}sistemas"

def acessar(url):
    sucesso, resposta = False, urllib.request.urlopen(url)

    if resposta.code == 200:
        try:
            sucesso, resposta = True, resposta.read().decode("utf-8")
        except Exception as e:
            print(f"erro acessando {url}: {str(e)}")

    return sucesso, resposta

def is_alive():
    sucesso, resposta = acessar(IS_ALIVE)

    return sucesso and resposta == "sim"

def get_jogatina():
    noticias = []
    
    sucesso, resposta = acessar(JOGATINA)
    if sucesso:
        noticias = json.loads(resposta)

    return sucesso, noticias

def get_sistemas():
    noticias = []

    sucesso, resposta = acessar(SISTEMAS)
    if sucesso:
        noticias = json.loads(resposta)

    return sucesso, noticias

def imprimir_noticias(tipo, noticias):
    print(f"imprimindo notícias de {tipo}")
    for noticia in noticias:
        print(noticia)

if __name__ == "__main__":
    while True:
        if is_alive():
            sucesso, noticias = get_jogatina()
            if sucesso:
                imprimir_noticias("jogos eletrônicos", noticias)
            else:
                print("não foi possível acessar notícias sobre jogos")

            sucesso, noticias = get_sistemas()
            if sucesso:
                imprimir_noticias("sistemas operacionais", noticias)
            else:
                print("não foi possível acessar notícias sobre sistemas operacionais")
        else:
            print("serviço não está disponível")

        time.sleep(2)