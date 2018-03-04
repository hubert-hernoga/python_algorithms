
bits_arr = list(range(1,513))
result = []

while len(bits_arr) != 0:
    for num in bits_arr:
        result.append(bits_arr[0] * 256 + bits_arr[1])
        del bits_arr[0]
        del bits_arr[0]

print(result)
print(len(result))



# wydajniejsza ver

for i in range(0, len(hex_list)-1, 2):
    first_elem = hex_list[i]
    secon_elem = hex_list[i+1]
    result = first_elem + secon_elem * 256
    nowa_lista.append(result)