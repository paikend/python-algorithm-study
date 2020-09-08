import sys


n = sys.stdin.readline().strip()
n = list(map(ord, n))
n.sort()
result = ""
num = 0
for i in n:
    if i >= 65:
        result += chr(i)
    else:
        num += int(chr(i))

print(result + str(num))