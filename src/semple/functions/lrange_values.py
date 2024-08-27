from config.redis_conect import get_redis_connection


redis_connect = get_redis_connection()


def lrange_values(lista, inicio, fim):
    """
    Recuperar um intervalo de valores de uma lista Redis.

    Args:
        lista (str): O nome da lista Redis.
        inicio (int): O índice inicial do intervalo.
        fim (int): O índice final do intervalo.

    Returns:
        list: Uma lista de valores do intervalo especificado.
    
    Equivalencia ao Redis CLI: LRANGE <lista> <inicio> <fim>
    Exemplo: LRANGE minha_lista 0 2
    """
    valores = redis_connect.lrange(lista, inicio, fim)
    return [v.decode('utf-8') for v in valores]
