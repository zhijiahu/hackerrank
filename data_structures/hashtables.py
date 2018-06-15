class HashTable:
    def __init__(self):
        self._map = [[] for i in range(256)]

    def __setitem__(self, key, value):
        index = self._get_index(key)
        bucket = self._map[index]

        keyIndex = -1
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                keyIndex = i
                break

        if keyIndex >= 0:
            bucket[keyIndex] = (key, value)
        else:
            bucket.append((key, value))

    def __getitem__(self, key):
        index = self._get_index(key)
        bucket = self._map[index]

        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                return v

        return None

    def _get_index(self, key):
        return hash(key) % len(self._map)


d = HashTable()
d['test'] = 2
print(d['test'])
d['test'] = 3
print(d['test'])
d['test'] = '13'
print(d['test'])

