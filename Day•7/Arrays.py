n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

reversed_array = arr[::-1]

output_string = ''
for i in range(len(reversed_array)):
    output_string += str(reversed_array[i]) + ' '

print(output_string)
