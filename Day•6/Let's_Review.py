# Enter your code here.

num_test_cases = int(input())

for i in range(num_test_cases):
    test_str = input()
    even_ind_char = ''
    odd_ind_char = ''
    for j in range(len(test_str)):
        if j % 2 == 0:
            even_ind_char += test_str[j]
        else:
            odd_ind_char += test_str[j]

    print('{} {}'.format(even_ind_char, odd_ind_char))
