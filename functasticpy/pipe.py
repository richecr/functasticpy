def pipe(value, *funcs):  # <- sem tipos aqui de propósito
    result = value
    for func in funcs:
        result = func(result)
    return result
