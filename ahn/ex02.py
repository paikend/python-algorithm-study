s = input()
number_list = map(int, list(s))
last = 0

for i, number in enumerate(number_list):
    if i == 0:
        last += number
    elif last == 0 or last == 1:
        last += number
    elif number == 0 or number == 1:
        last += number
    else:
        last *= number

print(last)
