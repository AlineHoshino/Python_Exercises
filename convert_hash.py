def convert_hash_to_array(hash):
    if hash == {}:
        return []
    arr = list()
    hash2 = dict(sorted(hash.items()))
    for item in hash2:
        arr.append([item, hash[item]])

    return arr


print(
    convert_hash_to_array(
        {"name": "Jeremy", "age": 24, "role": "Software Engineer"}
    )
)
