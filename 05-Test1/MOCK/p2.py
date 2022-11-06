def f(binary_number):
    binary = [*binary_number]
    print(binary)
    for i in binary:
        if i not in ["0", "1"]:
            return False
    return True
