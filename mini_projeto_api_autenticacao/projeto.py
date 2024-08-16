import requests
from pprint import pprint
import dotenv
import os
import streamlit as st


def fazer_request(url,params=None):
    resposta = requests.get(url=url,params=None)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resposta = None
    else:
        resultado = resposta.json()
    return resultado


def pegar_tempo_para_local(local):
    dotenv.load_dotenv()
    token = os.environ['CHAVE_API_OPENWEATHER']

    url = "https://api.openweathermap.org/data/2.5/weather"

    params ={
        'appid': token,
        'q': local,
        'units': 'metric',
        'lang': 'pt_br',
    }
    dados_tempo = fazer_request(url=url,params=params)
    return dados_tempo

def main():
    st.title("Meu App de consulta de tempera po localidade")
    st.write("Dados do OpenWeather")
    local = st.text_input('Busque uma cidade: ')
    if not local:
        st.stop()

    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:
        st.warning(f'Dados não encontrados para a cidade {local}')
        st.stop()
    clima_atual = dados_tempo['weather'][0]['description']
    temperatura = dados_tempo['main'],['temp']
    sensacao_termica = dados_tempo['main'],['feels_like']
    umidade = dados_tempo['main']['humidity']
    cobertura_nuvens = dados_tempo['clouds']['all']

    st.metric(label="Tempo Atual", valeu=clima_atual) 

if __name__ == "__main__":
    main()


