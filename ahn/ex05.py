import itertools


n, m = map(int, input().split(' '))
bowling = list(map(str, input().split(' ')))
num = 0

ab = list(map(''.join, itertools.combinations(bowling, 2)))
for i in ab:
    if i[0] != i[1]:
        num += 1

print(num)