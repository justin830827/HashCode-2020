def sort_lib(lib):
    return sorted(lib, key=lambda x: x[1])


def calculate_score(cur_sign, lib, total_day, books):
    res = 0
    for i in lib[4][:(total_day-(cur_sign+lib[1])+1)*lib[2]]:
        res += books[i]
    return res
