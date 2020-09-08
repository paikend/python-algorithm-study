import sys


n = sys.stdin.readline().strip()
n = list(n)

length = int(len(n)/2)

front = n[:length]
front = list(map(int, front))

back = n[length:]
back = list(map(int, back))

if sum(front) == sum(back):
    print("LUCKY")
else:
    print("READY")