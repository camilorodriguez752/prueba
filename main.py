def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print("Operaciones Básicas:")
    print("Suma: ", suma(3, 2))
    print("Resta: ", resta(5, 2))
    print("Multiplicación: ", multiplicacion(4, 2))
    print("División: ", division(10, 2))
