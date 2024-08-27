from config.redis_conect import get_redis_connection


# Conectando ao Redis
redis_connect = get_redis_connection()

def test_set_value():
    try:
        redis_connect.set('test_key', 'test_value')
        assert redis_connect.get('test_key').decode('utf-8') == 'test_value'
        return "✅ Teste de SET passou!"
    except AssertionError:
        return "❌ Teste de SET falhou!"

def test_get_value():
    try:
        redis_connect.set('test_key', 'test_value')
        valor = redis_connect.get('test_key')
        assert valor.decode('utf-8') == 'test_value'
        return "✅ Teste de GET passou!"
    except AssertionError:
        return "❌ Teste de GET falhou!"

def test_incr_value():
    try:
        redis_connect.set('counter', 1)
        redis_connect.incr('counter')
        assert redis_connect.get('counter').decode('utf-8') == '2'
        return "✅ Teste de INCR passou!"
    except AssertionError:
        return "❌ Teste de INCR falhou!"

def test_lpush_value():
    try:

        redis_connect.delete('mylist')
        
        redis_connect.lpush('mylist', 'valor1')
        redis_connect.lpush('mylist', 'valor2')
        lista = redis_connect.lrange('mylist', 0, -1)

        assert lista == [b'valor2', b'valor1'], f"Esperado [b'valor2', b'valor1'], mas obteve {lista}"

        return "✅ Teste de LPUSH passou!"
    except AssertionError as e:
        return f"❌ Teste de LPUSH falhou! {e}"

def test_lrange_values():
    try:

        redis_connect.delete('mylist')
        
        redis_connect.lpush('mylist', 'valor1')
        redis_connect.lpush('mylist', 'valor2')

        valores = redis_connect.lrange('mylist', 0, -1)
        assert [v.decode('utf-8') for v in valores] == ['valor2', 'valor1'], (
            f"Esperado ['valor2', 'valor1'], mas obteve {[v.decode('utf-8') for v in valores]}"
        )

        valores = redis_connect.lrange('mylist', 0, 0)
        assert [v.decode('utf-8') for v in valores] == ['valor2'], (
            f"Esperado ['valor2'], mas obteve {[v.decode('utf-8') for v in valores]}"
        )

        return "✅ Teste de LRANGE passou!"
    except AssertionError as e:
        return f"❌ Teste de LRANGE falhou! {e}"



def test_hset_value():
    try:
        redis_connect.hset('myhash', 'campo1', 'valor1')
        assert redis_connect.hget('myhash', 'campo1').decode('utf-8') == 'valor1'
        return "✅ Teste de HSET passou!"
    except AssertionError:
        return "❌ Teste de HSET falhou!"

def test_hgetall_values():
    try:
        redis_connect.hset('myhash', 'campo1', 'valor1')
        redis_connect.hset('myhash', 'campo2', 'valor2')
        valores = redis_connect.hgetall('myhash')
        valores_decoded = {k.decode('utf-8'): v.decode('utf-8') for k, v in valores.items()}
        assert valores_decoded == {'campo1': 'valor1', 'campo2': 'valor2'}
        return "✅ Teste de HGETALL passou!"
    except AssertionError:
        return "❌ Teste de HGETALL falhou!"
