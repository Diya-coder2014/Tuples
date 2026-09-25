def calculate_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

tup1 = (4, 3, 2, 2, -1, 18)
print(calculate_product(tup1))

tup2 = (2, 4, 8, 8, 3, 2, 9)
print(calculate_product(tup2))  

