def add_binary(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

# Input
a = "1010"
b = "1101"

print("Result:", add_binary(a, b))