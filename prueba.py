
def run():
    # print("Diga un entero positivo y te digo sí es perfecto: ")
    # numero = int(input())
    # divisores = [ i for i in range(1, numero) if numero % i == 0]
    # suma = sum(divisores)
    # if suma == numero:
    #     print(f'el numero : {numero} es perfecto y sus divisores son {divisores}')
    # else:
    #      print(f'el numero : {numero} NO es perfecto y sus divisores son {divisores}')
    for i in range(1,101):
        if i%15==0:
            print("fizzBuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

if __name__ == "__main__":
    run()