import memcache

class MultiCache:
    def __init__(self, tenant_id, host_list):
        assert(isinstance(tenant_id, str))
        assert(len(tenant_id) == 4)
        self.id = tenant_id
        self.mc = memcache.Client(host_list, debug=0)

    def set(self, key, value):
        #print("key:" + self.id + key)
        return self.mc.set(self.id + key, value)
    
    def get(self, key):
        #print("key:" + self.id + key)
        return self.mc.get(self.id + key)

    def delete(self, key):
        #print("key:" + self.id + key)
        return self.mc.delete(self.id + key)

    def flush_all(self):
        return self.mc.flush_all()

if __name__ == '__main__':
    tenant_id = 'A00'
    host_list = ['localhost:8080']