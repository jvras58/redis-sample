import streamlit as st
from config.redis_conect import get_redis_connection


# Conectando ao Redis
redis_connect = get_redis_connection()


def incr_value(chave):
    """
    Incrementa o valor da chave fornecida no Redis.

    Parâmetros:
    - chave (str): A chave para incrementar o valor.


    Example:
    incr_value("mychave")
    """
    valor = redis_connect.incr(chave)
    st.success(f"Valor da chave '{chave}' incrementado para {valor}.")

'''
Equivalente no cli: INCR <chave>
Exemplo: INCR mychave
'''
