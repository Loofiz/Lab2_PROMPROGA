import logging
logging.basicConfig(level=logging.DEBUG)

def add(a,b):
   return a+b+100

def minus(a,b):
    return a-b

def mult(a,b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)))        raise TypeError("Оба аргумента должны быть числами")
    logging.info(f"Умножение {a} * {b}")
    return a*b

if __name__ == "__main__":
    print(add(5, 3))
    print(mult(5, 3))
