def kwargsAcceptFun(**kwargs):
    dictionary = (kwargs)
    list_of_values = [v for k, v in dictionary.items()]
    average = sum(list_of_values) / len(list_of_values)
    return average


print(kwargsAcceptFun(a=3, b=5, c=7, d=9))