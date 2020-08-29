test_case =  [0,2,9,8,4]

def answer(test_case):
    results = 0
    for idx, _ in enumerate(test_case):
        if idx == 0:
            results += test_case[idx]
            continue
        results = (results*test_case[idx]) if results >= 2 else  (results + test_case[idx])
    return results


print(answer(test_case))