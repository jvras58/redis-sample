
import streamlit as st

from api.functions import create_session, end_session, get_active_users, list_active_sessions


st.title("Sistema de Sessões com Redis")
user_id = st.text_input("Digite seu ID de usuário:")

if st.button("Logar"):
    if user_id:
        session_id = create_session(user_id)
        st.success(f"Usuário {user_id} logado com sucesso! ID da sessão: {session_id}")
    else:
        st.error("Por favor, insira um ID de usuário válido.")

session_id = st.text_input("Digite o ID da sessão para deslogar:")

if st.button("Deslogar"):
    if session_id:
        end_session(session_id)
        st.success("Usuário deslogado com sucesso!")
    else:
        st.error("Por favor, insira um ID de sessão válido.")


active_users = get_active_users()
st.metric(label="Usuários Ativos", value=active_users)

st.subheader("Sessões Ativas")
sessions_info = list_active_sessions()

if sessions_info:
    for session_key, owner in sessions_info.items():
        st.write(f"ID da Sessão: {session_key.split(':')[1]} | Usuário: {owner}")
else:
    st.write("Nenhuma sessão ativa no momento.")
