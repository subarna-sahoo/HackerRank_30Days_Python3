import sys

n = int(sys.stdin.readline().strip())
phone_book = {}

for i in range(n):
    key, value = map(str, sys.stdin.readline().strip().split())
    phone_book[key] = value

q = sys.stdin.readline().strip()

while q:
    if q in phone_book:
        print(q + '=' + phone_book[q])
    else:
        print('Not found')

    q = sys.stdin.readline().strip()

