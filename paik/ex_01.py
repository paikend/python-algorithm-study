def answer(N, fears):
    groups_list = []
    temp_list = []
    for fear in sorted(fears):
        temp_list.append(fear)
        if temp_list[-1] < fear:
            continue
        if temp_list[-1] == len(temp_list):
            groups_list.append(temp_list)
            temp_list = []
    return len(groups_list), groups_list


N = 5
fears = [1,2,3,3,5]
# N = int(input())
# humans_info = list(map(int, input().split()))

print(answer(N, fears))