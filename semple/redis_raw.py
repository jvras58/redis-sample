'''Comandos brutos do Redis'''


# Rodar poetry run python semple/redis_raw.py
from config.redis_conect import get_redis_connection

redis_connect = get_redis_connection()
print(redis_connect)

# Definir par chave-valor
redis_connect.set('name', 'John Doe')
print(redis_connect.get('name'))
