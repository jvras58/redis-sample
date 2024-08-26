"""Módulo para obter a conexão com o Redis"""

import redis


def get_redis_connection():
    '''Função para obter a conexão com o Redis'''
    return redis.StrictRedis(host='redis', port=6379, db=0)
