def get_real_floor(n): 
    if n >= 13:
        The_European_system = n - 2
        return The_European_system
    elif n <= 0:
        The_European_system = n + 0
        return The_European_system
    else:
        The_European_system = n - 1
        return The_European_system