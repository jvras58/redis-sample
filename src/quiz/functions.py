import uuid
import streamlit as st
from config.redis_conect import get_redis_connection
import random

# Conexão com Redis
redis_client = get_redis_connection()

def register_user(username: str) -> str:
    """Registra um novo usuário com um ID único."""
    user_id = str(uuid.uuid4())
    redis_client.hset(f"user:{user_id}", mapping={"username": username, "score": 0})
    return user_id

def add_question(question: str, answer: str):
    """Adiciona uma nova pergunta ao Redis."""
    question_id = str(uuid.uuid4())
    redis_client.hset(f"question:{question_id}", mapping={"question": question, "answer": answer})

    # Verifica se a pergunta foi salva corretamente
    saved_question = redis_client.hgetall(f"question:{question_id}")
    
    # Decodificação dos valores de bytes para strings
    saved_question = {k.decode('utf-8'): v.decode('utf-8') for k, v in saved_question.items()}

    # Log para depuração
    st.sidebar.write(f"Conteúdo salvo em Redis: {saved_question}")

    # Verificação da existência das chaves
    if "question" in saved_question and "answer" in saved_question:
        st.sidebar.success(f"Pergunta salva com sucesso: {saved_question['question']}")
    else:
        st.sidebar.error("Erro ao salvar a pergunta. Os dados estão incompletos.")

def get_random_question() -> tuple:
    """Retorna uma pergunta aleatória do Redis."""
    question_keys = redis_client.keys("question:*")
    if not question_keys:
        return None, None
    
    random.shuffle(question_keys)  # Embaralha as chaves para obter uma aleatória
    for key in question_keys:
        question_data = redis_client.hgetall(key)
        question_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in question_data.items()}
        if "question" in question_data and "answer" in question_data:
            return question_data["question"], question_data["answer"]
    
    return None, None

def submit_answer(user_id: str, answer: str, correct_answer: str):
    """Verifica a resposta e atualiza a pontuação do usuário."""
    if answer.lower() == correct_answer.lower():
        redis_client.hincrby(f"user:{user_id}", "score", 10)

def get_ranking() -> list:
    """Retorna o ranking dos jogadores baseado na pontuação."""
    keys = redis_client.keys("user:*")
    users = [redis_client.hgetall(key) for key in keys]
    decoded_users = []
    for user in users:
        decoded_user = {k.decode('utf-8'): v.decode('utf-8') for k, v in user.items()}
        decoded_users.append(decoded_user)
    sorted_users = sorted(decoded_users, key=lambda x: int(x["score"]), reverse=True)
    return sorted_users

def list_all_questions() -> list:
    """Lista todas as perguntas disponíveis no Redis."""
    question_keys = redis_client.keys("question:*")
    questions = []
    for key in question_keys:
        question_data = redis_client.hgetall(key)
        question_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in question_data.items()}
        if "question" in question_data and "answer" in question_data:
            questions.append((question_data["question"], question_data["answer"]))
    return questions

def delete_all_questions():
    """Apaga todas as perguntas do Redis."""
    question_keys = redis_client.keys("question:*")
    if question_keys:
        redis_client.delete(*question_keys)
        st.sidebar.success("Todas as perguntas foram apagadas.")

def delete_all_users():
    """Apaga todos os usuários do Redis."""
    user_keys = redis_client.keys("user:*")
    if user_keys:
        redis_client.delete(*user_keys)
        st.sidebar.success("Todos os usuários foram apagados.")
