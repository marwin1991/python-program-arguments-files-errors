class MyError(Exception):
    pass

def my_postivie_add(a, b):
    if a < 0:
        raise MyError

    if b < 0:
        raise MyError

    return a + b
        

try:
    result = my_postivie_add(-1, 6)
    print(result)
except MyError:
    print("Złe argumenty")