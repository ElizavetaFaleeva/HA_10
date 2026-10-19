# Description of a function

def counter():
    """Count the number of string elements in a mixed list."""
    elements = ["Peter", 356, 7.07, False, True, "great", 
                "choco", [2, 5], "star"]

    count = 0
    for item in elements:
        if type(item) is str:
            count += 1
    print("Number of strings: ", count)

# Launch of the function
counter()
