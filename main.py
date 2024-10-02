import requests
import pandas as pd

API_KEY = "6PE3pSPCo3srpppnRGK8SM"
url = f"https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo"

dados_gerais = []

 
response = requests.get(url)

data = response.json()


dados = {
    "data": None,
    "valor" : None,
}

for i in range(7):

    dados = {
        "data": data['data'][i]['date'],
        "valor": int(round(float(data['data'][i]['value'])))
    }
    
    dados_gerais.append(dados)


df = pd.DataFrame(dados_gerais)

