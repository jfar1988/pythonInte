def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firtname": "Juan", "lastname": "Aguilar"}

    super_list=[
        {"firtname": "Juan", "lastname": "Aguilar"},
        {"firtname": "Miguel", "lastname": "Torres"},
        {"firtname": "Pepe", "lastname": "Rodelo"},
        {"firtname": "Susana", "lastname": "Martinez"},
        {"firtname": "José", "lastname": "Garcia"}
    ]
    super_dict={
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')
    
    
if __name__ == "__main__":
    run()