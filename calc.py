import logging
logging.basicConfig(level=logging.INFO)

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def mult(a,b):
    logging.info(f"Умножение {a} * {b}")
    return a*b

if __name__ == "__main__":
    print("Простой калькулятор")