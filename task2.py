def typeBasedTransformer(**kwargs):
    dictionary = kwargs
    output_list = []
    for elem in dictionary.values():
        if isinstance(elem, (int, float)):
            output_list.append(elem ** 2)
        elif isinstance(elem, str):
            output_list.append(elem[::-1])
        elif isinstance(elem, bool):
            output_list.append(not elem)
        elif isinstance(elem, (list, tuple)):
            output_list.append(elem[::-1])
        elif isinstance(elem, dict):
            output_list.append([[v, k] for k, v in elem.items()])
    return output_list

print(typeBasedTransformer(g=6, y="qwerty", b=True, c= (4, 5, 6, 7), d=[9, 8, -1, 4], e={'bir': 1, 'two': 2}))

