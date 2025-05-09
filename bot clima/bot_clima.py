import requests
import pandas as pd
from datetime import datetime

# Substitua pela sua chave de API
API_KEY = 'f94417e9d0994718891160046250905'  # Sua chave da API
CIDADE = 'Fortaleza'  # Alterado para Fortaleza
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CIDADE}&lang=pt"

resposta = requests.get(URL)

if resposta.status_code == 200:
    dados = resposta.json()

    clima = {
        'Data': [datetime.now().strftime('%d/%m/%Y')],
        'Cidade': [CIDADE],
        'Temperatura (°C)': [dados['current']['temp_c']],
        'Descrição': [dados['current']['condition']['text']],
        'Sensação térmica (°C)': [dados['current']['feelslike_c']],
        'Umidade (%)': [dados['current']['humidity']],
        'Vento (km/h)': [dados['current']['wind_kph']]
    }

    df = pd.DataFrame(clima)
    df.to_csv('clima_hoje.csv', index=False)
    print("✅ Arquivo 'clima_hoje.csv' gerado com sucesso.")
else:
    print("⚠️ Erro ao acessar a API. Verifique a chave ou a cidade.")
