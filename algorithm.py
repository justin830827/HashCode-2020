def sort_lib(lib):
    return sorted(lib, key=lambda x: x[1])


def calculate_score(cur_sign, lib, total_day, books, checklist):
    res = 0
    limit = (total_day-cur_sign-lib[1]+1)*lib[2]
    count = 0
    for i in range(len(lib[4])):
        if count > limit:
            break
        if lib[4][i] not in checklist:
            res += books[lib[4][i]]
            count += 1
    return res
