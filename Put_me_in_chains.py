def chain(init_val, functions):
    for item in functions:
        init_val = item(init_val)    
    return init_val