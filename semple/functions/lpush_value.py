import streamlit as st
from config.redis_conect import get_redis_connection


# Conectando ao Redis
redis_connect = get_redis_connection()


def lpush_value(lista, valor):
    """
    Envia um valor para a extremidade esquerda de uma lista Redis.

    Args:
    - lista (str): O nome da lista Redis.
    - valor (str): O valor a ser adicionado à lista.

    Example:
    lpush_value("mylist", "hello")
    """
    redis_connect.lpush(lista, valor)
    st.success(f"Valor '{valor}' adicionado à lista '{lista}'.")
