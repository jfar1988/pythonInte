

def run():
    # squares=[i**2 for i in range(1,101) if i%3 !=0]
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # print(squares)
    # reto=[i for i in range(1,99999) if i%36==0]

    # print(reto)

    for i in range(1,101):
        if i%15==0:
            print("fizzBuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

    # fizzBuzz = [print("fizzBuzz") for i in range(1, 101) if i % 15 == 0]
    # fizz = [print("fizz") for i in range(1, 101) if i % 3 == 0]
    # buzz = [print("buzz") for i in range(1, 101) if i % 5 == 0]

    # print(fizzBuzz)
    # print(fizz)
    # print(buzz)


if __name__ == "__main__":
    run()
