from prueba import run

def divisors(num):
    divisors = [i for i in range(1, num +1) if num % i == 0]
    return divisors

def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Termino el programa")

if "__main__" == __name__:
    run()