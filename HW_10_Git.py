def counter():
    elements = ["Peter", 356, 7.07, False, True, "great", 
                "choco", [2, 5], "star", "Красти крабс тащит", "Я люблю баню"]

    count = 0
    for item in elements:
        if type(item) == str:
            count += 1
    print("Number of string types is: ", count)

counter()