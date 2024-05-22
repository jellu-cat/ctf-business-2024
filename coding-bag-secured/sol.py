def parse_input(string):
    data = []
    lines = string.split('\n')
    for i in range(1, len(lines) - 1):
        # print(f"\n{line}\n", end='', sep='')
        row = lines[i].strip().split(' ')
        # print(f"\t{row}")
        row = [int(val) for val in row]
        data.append(row)
    return data

def get_max_value(maximum_capacity, products):
    value = 0
    c_capacity = maximum_capacity
    # print(products)
    for product in products:
        if(c_capacity - product[0] >= 0):
            p_capacity = c_capacity
            p_value = value
            c_capacity = c_capacity - product[0]
            print(f"C -> {p_capacity} - {product[0]} = {c_capacity}")

            value = value + product[1]
            print(f"V -> {p_value} + {product[1]} = {value}")
    return value

import sys

string = """
4 9
5 5
3 3
4 8
7 5
"""

# string = sys.argv[1].replace('\\n', '\n')
# print(string)
table = parse_input(string)
N = table[0][0]
C = table[0][1]
table = table[1:]

# print(N)
# print(C)
# print(table)

table = sorted(table, key=lambda x: x[1],
                    reverse=True)

print(table)
print(get_max_value(C, table))

