'''Redis raw commands'''

import redis

# Connect to Redis server python3 redis_raw.py
redis_connect = redis.StrictRedis(host='redis', port=6379, db=0)
print(redis_connect)

# Set key-value pair
redis_connect.set('name', 'John Doe')
print(redis_connect.get('name'))
