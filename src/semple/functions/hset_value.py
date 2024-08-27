import streamlit as st
from config.redis_conect import get_redis_connection

# Conectando ao Redis
redis_connect = get_redis_connection()


def hset_value(hashname, campo, valor):
    """
    Define o valor de um campo em um hash no Redis.

    Parameters:
    - hashname (str): O nome do hash.
    - campo (str): O nome do campo.
    - valor (str): O valor a ser definido.


    Example:
    >>> hset_value("meu_hash", "campo1", "valor1")
    >>> hset_value("meu_hash", "campo2", "valor2")

    """
    redis_connect.hset(hashname, campo, valor)
    st.success(f"Campo '{campo}' no hash '{hashname}' definido com valor '{valor}'.")
