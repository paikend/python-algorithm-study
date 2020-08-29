adventurer = int(input())
adventurer_list = list(map(int, input().split(' ')))
adventurer_list.sort()
group = 0


# 체크하기 위한 재귀함
def chk_group(clone_list, chk):
    adv_list = clone_list.copy()
    # 가장 끝에 있는 녀석의 공포 지수
    fear = adv_list[-1]
    if len(adv_list) >= fear:
        for _ in range(fear):
            adv_list.pop()
        chk += 1
    elif len(adv_list) < fear:
        adv_list = []
    if len(adv_list) == 0:
        return chk
    return chk_group(adv_list, chk)


for i in range(adventurer - 1, -1, -1):
    # 리스트에서 가장 공포가 높은 얘가 리스트 길이보다 길면 체크할 필요가 없기때문에 구분
    if len(adventurer_list) >= adventurer_list[i]:
        group_num = chk_group(adventurer_list, 0)
        if group <= group_num:
            group = group_num
    adventurer_list.pop()


print(group)



