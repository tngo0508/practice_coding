# hash table with chaining
hash_table = [[] for _ in range(10)]
print(hash_table)

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, _ = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for _ , kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v
    return -1


def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, _ = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
    


insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)