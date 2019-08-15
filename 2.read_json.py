new_l = []


def num_jud(json_data):
    for k, v in json_data.items():
        new_d = {}
        if isinstance(v, (int, float)):
            new_d[k] = v
            new_l.append(new_d)
        elif isinstance(v, dict):
            num_jud(v)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    num_jud(i)
    return new_l


def sort_kv(new_l):
    d_order = []
    for i in range(len(new_l)):
        d_order += new_l[i].items()
        new_l1 = sorted(d_order, key=lambda x: x[1], reverse=False)
    return new_l1


json_data = {
    "r": 1,
    "4": 150,
    "l": [1, 2, {"a": 1001}, 3, "str"],
    "o": {
        "r": 5,
        "b": 7,
        "c": "bc",
        "s": "中文"
    }
}


with open('p2.txt', 'w') as f:
    f.write(str(sort_kv(num_jud(json_data))))
    print('排序存储完成')
