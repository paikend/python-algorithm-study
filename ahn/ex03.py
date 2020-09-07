s = input()
s = list(s)
zero_num, one_num = 0, 0
zero, one = [], []

for idx, z in enumerate(s):
    if z == '1':
        if len(zero) == 0:
            zero.append(1)
            zero_num += 1
    if z == '0':
        if len(zero) == 1:
            zero.pop()

for idx, o in enumerate(s):
    if o == '0':
        if len(one) == 0:
            one.append(1)
            one_num += 1
    if o == '1':
        if len(one) == 1:
            one.pop()

print(min(zero_num, one_num))