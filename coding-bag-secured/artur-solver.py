#!/bin/python3
from pwn import *
import time

##  Sofi's algorithm <3
def parse_input(string):
    data = []
    lines = string.split('\n')
    for i in range(1, len(lines) - 1):
        # print(f"\n{line}\n", end='', sep='')
        row = lines[i].strip().split(' ')
        # print(f"\t{row}")
        row = [int(val) for val in row]
        data.append(row)
    # print(data)
    return data

def get_max_value(maximum_capacity, products):
    value = 0
    c_capacity = maximum_capacity
    # print(products)
    for product in products:
        if(c_capacity - product[0] >= 0):
            # p_capacity = c_capacity
            # p_value = value
            c_capacity = c_capacity - product[0]
            # print(f"C -> {p_capacity} - {product[0]} = {c_capacity}")

            value = value + product[1]
            # print(f"V -> {p_value} + {product[1]} = {value}")
    return value


# connecter function
def connecter(ip_Rec, port_Rec):
    p = remote(ip_Rec, port_Rec)
    while True:
        rec_msg = p.recvlineS().strip()
        print(rec_msg)
        if 'Chief' in rec_msg:
            rec_msg = p.recvlineS().strip()
            p.sendline("\n".encode())
            print("!!!!")
        if 'HTB' in rec_msg:
            print(rec_msg)
        if rec_msg.startswith("Test"):
            rec_msg = "\n"
            rec_msg += p.recvS()
            print(rec_msg)

            # From sol.py
            table = parse_input(rec_msg)
            N = table[0][0]
            C = table[0][1]
            table = table[1:]

            # print(N)
            # print(C)
            # print(table)

            table = sorted(table, key=lambda x: x[1],
                                reverse=True)

            # print(table)
            max_val = get_max_value(C, table)
            
            # Sender stufs
            Smax = str(max_val)
            print(Smax)
            time.sleep(1)
            p.sendline(Smax.encode())


#     ip            port
# nc 94.237.59.230 39332
connecter('94.237.54.176', 30870)
