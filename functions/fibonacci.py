def fibonaccci(l):
    sequence = []
    a, b = 0, 1
    while a < l:
        sequence.append(a)
        a, b = b, a+b
    return sequence