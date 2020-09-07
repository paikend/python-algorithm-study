S = ["K", "K", "A", "C", "B"]
def answer(S):
    str_list= []
    digit = 0
    for index, value in enumerate(S):
        if value.isalpha():
            str_list.append(value)
        else:
            digit += int(value)
    if not digit:
        digit = ""
    return ''.join(sorted(str_list))+ str(digit)

print(answer(S))