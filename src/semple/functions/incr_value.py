import streamlit as st
from config.redis_conect import get_redis_connection


redis_connect = get_redis_connection()


def incr_value(chave):
    """
    Incrementa o valor da chave fornecida no Redis.
    
    Parâmetros:
    - chave (str): A chave para incrementar o valor.

    Equivalencia ao Redis CLI: INCR <chave>
    Exemplo: INCR mychave
    """
    valor = redis_connect.incr(chave)
    st.success(f"Valor da chave '{chave}' incrementado para {valor}.")
