def rand_int(x,y):
    import random
    min = x
    max = y
    integer = random.random() * (max-min) + min
    if integer >= max:
    	print(int(integer))
    else:
    	print(round(integer))

