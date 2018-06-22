
class HashTable_Chaining:
    def __init__(self):
        print('HashMap with chaining')
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
                print('Key {} is at index[{}] and at {}th element'.format(key, index, i))
                return v

        return None

    def _get_index(self, key):
        #return hash(key) % len(self._map)
        return 1


class HashTable_LinearProbe:
    def __init__(self):
        empty_slots = [3, 5, 7]
        print('HashMap with linear probing with empty slots {}'.format(empty_slots))
        self._array = [('occupied', None)] * 256

        # except the following 3 slots
        for slot in empty_slots:
            self._array[slot] = (None, None)

    def __setitem__(self, key, value):
        index = self._get_index(key)
        bucket = self._array[index]

        if bucket[0] is None or bucket[0] == key:
            self._array[index] = (key, value)
        else:
            i = index + 1
            while i != index:
                bucket = self._array[i]
                if bucket[0] is None:
                    self._array[i] = (key, value)
                    break
                else:
                    i = (i + 1) % len(self._array)

    def __getitem__(self, key):
        index = self._get_index(key)
        bucket = self._array[index]

        if bucket[0] == key:
            print('Key {} is at index[{}]'.format(key, index))
            return bucket[1]
        else:
            i = index + 1
            while i != index:
                bucket = self._array[i]
                if bucket[0] == key:
                    print('Key {} is at index[{}]'.format(key, i))
                    return bucket[1]
                else:
                    i = (i + 1) % len(self._array)

        return None

    def _get_index(self, key):
        #return hash(key) % len(self._array)
        return 1


class HashTable_QuadraticProbe:
    def __init__(self):
        print('HashMap with quadratic probing')
        self._array = [(None, None)] * 256

    def __setitem__(self, key, value):
        index = self._get_index(key)
        bucket = self._array[index]

        if bucket[0] is None or bucket[0] == key:
            self._array[index] = (key, value)
        else:
            j = 1
            while j != len(self._array):
                i = self.quadratic_function(index, j)
                bucket = self._array[i]
                if bucket[0] is None:
                    self._array[i] = (key, value)
                    break
                else:
                    j += 1

    def __getitem__(self, key):
        index = self._get_index(key)
        bucket = self._array[index]

        if bucket[0] == key:
            print('Key {} is at index[{}]'.format(key, index))
            return bucket[1]
        else:
            j = 1
            while j != len(self._array):
                i = self.quadratic_function(index, j)
                bucket = self._array[i]
                if bucket[0] == key:
                    print('Key {} is at index[{}]'.format(key, i))
                    return bucket[1]
                else:
                    j += 1

        return None

    def _get_index(self, key):
        #return hash(key) % len(self._array)
        return 1

    def quadratic_function(self, index, j):
        new_index = (index + j * j) % len(self._array)
        return new_index


kv = [('key1', 1), ('key2', 2), ('key3', 3)]

d = HashTable_Chaining()
for k, v in kv:
    d[k] = v
    print(d[k])

print

d = HashTable_LinearProbe()
for k, v in kv:
    d[k] = v
    print(d[k])

print

d = HashTable_QuadraticProbe()
for k, v in kv:
    d[k] = v
    print(d[k])

