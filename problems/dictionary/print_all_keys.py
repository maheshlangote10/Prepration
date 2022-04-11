D1={1: {2: {3: 4, 5: 6, "details": { "name":"Mahesh", "age":30, "gender":"male"}}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}


def iterate_all_key(d):
    for key, value in d.items():
        if isinstance(value, dict):
            iterate_all_key(value)
        else:
            print(key)


iterate_all_key(D1)
