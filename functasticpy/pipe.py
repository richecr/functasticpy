def pipe(value, *funcs):
    result = value
    for func in funcs:
        result = func(result)

    return result
