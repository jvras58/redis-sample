from config.redis_conect import get_redis_connection

redis_connect = get_redis_connection()

def get_value(chave):
    """
    Recupera o valor associado à chave fornecida do Redis.

    Parameters:
    - chave (str): A chave para a qual recuperar o valor.

    Returns:
    - str or None: O valor associado à chave ou None se a chave não existir.

    Equivalencia ao Redis CLI: GET <chave>
    Exemplo: GET meu_valor
    """
    valor = redis_connect.get(chave)
    return valor.decode('utf-8') if valor else None

