import multicache

if __name__ == '__main__':
    tenant_id = 'A13B'
    host_list = ['localhost:5000']
    client = multicache.MultiCache(tenant_id, host_list)
    print(client.set('hello', 'world'))
    print(client.get('hello'))
    print(client.delete('hello'))
    print(client.get('hello'))
    print(client.flush_all())