import streamlit as st
from config.redis_conect import check_redis_connection, get_redis_connection
from quiz.functions import (
    add_question, delete_all_questions, delete_all_users, get_random_question, 
    get_ranking, list_all_questions, register_user, submit_answer
)

# Conexão com Redis
redis_client = get_redis_connection()

# Verificação de Conexão com Redis
if check_redis_connection():
    st.sidebar.success("Conexão com Redis bem-sucedida!")
else:
    st.sidebar.error("Erro ao conectar ao Redis. Verifique a conexão.")

# Título da aplicação
st.title("🎉 Quiz com Redis 🎉")

# Registro de usuário
if "user_id" not in st.session_state:
    st.header("📝 Registre-se para começar o Quiz")
    username = st.text_input("Digite seu nome de usuário:")
    if st.button("Registrar"):
        if username:
            st.session_state["user_id"] = register_user(username)
            st.success(f"Bem-vindo(a), {username}!")
            # Rerun simulation by setting a state variable
            st.session_state["registered"] = True
else:
    # Mostrar pergunta
    st.header("🤔 Responda à pergunta:")
    question, correct_answer = get_random_question()

    if question:
        st.write(f"**Pergunta:** {question}")
        answer = st.text_input("Sua resposta:")

        if st.button("Enviar Resposta"):
            submit_answer(st.session_state["user_id"], answer, correct_answer)
            if answer.lower() == correct_answer.lower():
                st.success("✔️ Resposta correta!")
            else:
                st.error(f"❌ Resposta errada! A resposta correta era: {correct_answer}")

            if st.button("Próxima Pergunta"):
                st.session_state["next_question"] = True
    else:
        st.write("Nenhuma pergunta disponível. Por favor, adicione perguntas no painel de administração.")

    # Exibir ranking
    st.header("🏆 Ranking")
    ranking = get_ranking()
    if ranking:
        for idx, user in enumerate(ranking, 1):
            st.write(f"{idx}. {user['username']} - {user['score']} pontos")
    else:
        st.write("O ranking ainda está vazio. Seja o primeiro a jogar!")

# Painel de Administração
st.sidebar.header("⚙️ Administração")
if st.sidebar.checkbox("Mostrar opções de administração"):
    st.sidebar.subheader("Adicionar nova pergunta")
    question_input = st.sidebar.text_input("Digite a pergunta:")
    answer_input = st.sidebar.text_input("Digite a resposta correta:")
    if st.sidebar.button("Adicionar Pergunta"):
        if question_input and answer_input:
            add_question(question_input, answer_input)
            st.sidebar.success("Pergunta adicionada com sucesso!")
        else:
            st.sidebar.error("Por favor, preencha tanto a pergunta quanto a resposta.")

    st.sidebar.subheader("Cadastrar novo usuário")
    admin_username_input = st.sidebar.text_input("Digite o nome do novo usuário:")
    if st.sidebar.button("Cadastrar Usuário"):
        if admin_username_input:
            register_user(admin_username_input)
            st.sidebar.success(f"Usuário '{admin_username_input}' cadastrado com sucesso!")
        else:
            st.sidebar.error("Por favor, digite um nome de usuário válido.")
    
    # Listar todas as perguntas disponíveis
    st.sidebar.subheader("Perguntas Disponíveis")
    questions = list_all_questions()
    if questions:
        for idx, (q, a) in enumerate(questions, 1):
            st.sidebar.write(f"{idx}. Pergunta: {q} | Resposta: {a}")
    else:
        st.sidebar.write("Nenhuma pergunta disponível.")

    st.sidebar.subheader("Gerenciamento de Dados")
    if st.sidebar.button("Apagar Todas as Perguntas"):
        delete_all_questions()
        st.sidebar.success("Todas as perguntas foram apagadas.")
        
    if st.sidebar.button("Apagar Todos os Usuários"):
        delete_all_users()
        st.sidebar.success("Todos os usuários foram apagados.")
