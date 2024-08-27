"""Módulo para obter a conexão com o Redis"""

import redis


def get_redis_connection():
    '''Função para obter a conexão com o Redis'''
    return redis.StrictRedis(host='redis', port=6379, db=0)

def check_redis_connection():
    '''Função para verificar a conexão com o Redis'''
    try:
        redis_client = get_redis_connection()
        redis_client.ping()
        return True
    except redis.ConnectionError:
        return False
