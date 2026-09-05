def show_tuple_immutability():
    my_tuple = (1, 2, 3)
    print("Tuple:", my_tuple)
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print("Hata:", e)

show_tuple_immutability()