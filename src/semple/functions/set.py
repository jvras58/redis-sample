import streamlit as st
from config.redis_conect import get_redis_connection

redis_connect = get_redis_connection()

def set_value(chave, valor):
    """
    Define o valor de uma chave no Redis.

    Parameters:
        chave (str): A chave a ser definida.
        valor (str): O valor a ser definido para a chave.
    """
    redis_connect.set(chave, valor)
    st.success(f"Chave '{chave}' definida com valor '{valor}'.")


'''
Equivalente no cli: SET <chave> <valor>
Exemplo: SET meu_valor 123
'''
