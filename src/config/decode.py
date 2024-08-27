def decode_redis_data(data):
    """
    Converta todas as strings de bytes no dicionário de dados fornecido em strings regulares.
    """
    if isinstance(data, dict):
        return {k.decode('utf-8') if isinstance(k, bytes) else k: 
                v.decode('utf-8') if isinstance(v, bytes) else v for k, v in data.items()}
    elif isinstance(data, list):
        return [decode_redis_data(item) for item in data]
    return data
