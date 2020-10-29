import requests
from retry import retry

@retry(exceptions=Exception)
def getUrl():
    url = 'http://127.0.0.1:5000/'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.text

    raise Exception


print(getUrl())
