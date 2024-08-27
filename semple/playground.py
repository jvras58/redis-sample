import streamlit as st
from functions.set import set_value
from functions.get import get_value
from functions.incr_value import incr_value
from functions.lpush_value import lpush_value
from functions.lrange_values import lrange_values
from functions.hset_value import hset_value
from functions.hgetall_values import hgetall_values
from tests.tests import (
    test_get_value, 
    test_hgetall_values, 
    test_hset_value, 
    test_incr_value, 
    test_lpush_value, 
    test_lrange_values, 
    test_set_value
)

st.title("Redis Playground")

st.sidebar.header("Escolha uma operação Redis")

opcao = st.sidebar.selectbox(
    "Operação",
    ("SET", "GET", "INCR", "LPUSH", "LRANGE", "HSET", "HGETALL", "Testes")
)

if opcao == "Testes":
    st.subheader("Testes Automáticos")
    st.write(test_set_value())
    st.write(test_get_value())
    st.write(test_incr_value())
    st.write(test_lpush_value())
    st.write(test_lrange_values())
    st.write(test_hset_value())
    st.write(test_hgetall_values())

elif opcao == "SET":
    st.subheader("Definir um par chave-valor")
    chave = st.text_input("Chave", value="minha_chave")
    valor = st.text_input("Valor", value="meu_valor")
    if st.button("Definir"):
        set_value(chave, valor)

elif opcao == "GET":
    st.subheader("Recuperar o valor de uma chave")
    chave = st.text_input("Chave", value="minha_chave")
    if st.button("Recuperar"):
        valor = get_value(chave)
        if valor:
            st.success(f"Valor para a chave '{chave}': {valor}")
        else:
            st.warning(f"A chave '{chave}' não existe.")

elif opcao == "INCR":
    st.subheader("Incrementar o valor de uma chave numérica")
    chave = st.text_input("Chave", value="meu_contador")
    if st.button("Incrementar"):
        incr_value(chave)

elif opcao == "LPUSH":
    st.subheader("Adicionar um valor ao início de uma lista")
    lista = st.text_input("Nome da Lista", value="minha_lista")
    valor = st.text_input("Valor", value="meu_valor")
    if st.button("Adicionar"):
        lpush_value(lista, valor)

elif opcao == "LRANGE":
    st.subheader("Recuperar elementos de uma lista")
    lista = st.text_input("Nome da Lista", value="minha_lista")
    inicio = st.number_input("Início", min_value=0, step=1, value=0)
    fim = st.number_input("Fim", min_value=0, step=1, value=0)
    if st.button("Recuperar"):
        # Permite -1 para indicar todos os elementos
        if fim == 0 and st.checkbox("Recuperar até o fim da lista"):
            fim = -1
        valores = lrange_values(lista, int(inicio), fim)
        st.write(f"Elementos na lista '{lista}' entre {inicio} e {fim}: {valores}")

elif opcao == "HSET":
    st.subheader("Definir um campo em um hash")
    hashname = st.text_input("Nome do Hash", value="meu_hash")
    campo = st.text_input("Campo", value="meu_campo")
    valor = st.text_input("Valor", value="meu_valor")
    if st.button("Definir"):
        hset_value(hashname, campo, valor)

elif opcao == "HGETALL":
    st.subheader("Recuperar todos os campos e valores de um hash")
    hashname = st.text_input("Nome do Hash", value="meu_hash")
    if st.button("Recuperar"):
        valores = hgetall_values(hashname)
        st.write(f"Valores no hash '{hashname}': {valores}")
