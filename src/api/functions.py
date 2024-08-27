import uuid
from datetime import timedelta
from config.redis_conect import get_redis_connection

SESSION_TIMEOUT = timedelta(minutes=5)
redis_client = get_redis_connection()



def create_session(user_id: str) -> str:
    """Cria uma nova sessão para um usuário e retorna o ID da sessão."""
    session_id = str(uuid.uuid4())
    session_key = f"session:{session_id}"
    
    redis_client.setex(session_key, SESSION_TIMEOUT, user_id)

    redis_client.sadd("active_users", user_id)
    
    return session_id

def end_session(session_id: str):
    """Encerra uma sessão e remove o usuário dos ativos se não tiver outras sessões."""
    session_key = f"session:{session_id}"
    user_id = redis_client.get(session_key)
    
    if user_id:
        user_id = user_id.decode("utf-8")
        
        redis_client.delete(session_key)

        active_sessions = redis_client.keys(f"session:*")
        user_sessions = [key for key in active_sessions if redis_client.get(key).decode("utf-8") == user_id]
        
        if not user_sessions:
            redis_client.srem("active_users", user_id)

def get_active_users() -> int:
    """Retorna a contagem de usuários ativos."""
    return redis_client.scard("active_users")

def list_active_sessions() -> dict:
    """Retorna um dicionário com todas as sessões ativas e seus respectivos donos."""
    active_sessions = redis_client.keys(f"session:*")
    sessions_info = {session_key.decode("utf-8"): redis_client.get(session_key).decode("utf-8") for session_key in active_sessions}
    return sessions_info
