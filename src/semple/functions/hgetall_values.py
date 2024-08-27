from config.redis_conect import get_redis_connection


redis_connect = get_redis_connection()



def hgetall_values(hashname):
    """
    Recupera todos os valores de um hash Redis e os retorna como um dicionário.

    Parameters:
    - hashname (str): O nome do hash Redis.

    Returns:
    - dict: Um dicionário contendo os valores do hash Redis, com chaves e valores como strings.
    
    Equivalencia ao Redis CLI: HGETALL <hashname>
    Exemplo: HGETALL myhash
    """
    valores = redis_connect.hgetall(hashname)
    return {k.decode('utf-8'): v.decode('utf-8') for k, v in valores.items()}
