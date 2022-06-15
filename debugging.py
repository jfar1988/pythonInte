from prueba import run

def divisors(num):
    divisors = [i for i in range(1, num +1) if num % i == 0]
    return divisors

def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num <= 0:
            raise ValueError("No se puede ingresar un numero negativo")
        print(divisors(num))
        print("Termino el programa")
    except ValueError as ve:
        print(ve)
        return print("Debes ingresar un numero POSITIVO")
            
    # except ValueError:
    #     print("Debes ingresar un numero")
# def palindrome(string):
#     try:
#         if len(string) == 0:
#             raise ValueError("No se puede ingresar una cadena de texto vacia")
#         return string == string[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False

# try:
#     print(palindrome(""))
# except TypeError:
#     print("Solo se puede ingresar String o Cadenas de texto")

if "__main__" == __name__:
    run()