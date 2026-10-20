def counter():
    elements = ["Peter", 356, 7.07, False, True, "great"]
#это у нас счетчик всех элементов строкового типа данных
    count = 0
    for item in elements:
        if type(item) == str:
            count += 1
    print("Result: ", count)

counter()