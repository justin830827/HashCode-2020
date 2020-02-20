def sort_lib(lib):
    return sorted(lib, key=lambda x: x[1])


def calculate_score(cur_sign, lib, total_day, books, checklist):
    res = 0
<<<<<<< HEAD
    for i in lib[4][:(total_day-(cur_sign+lib[1])+1)*lib[2]]:
        res += books[i]
=======
    limit = (total_day-cur_sign)*lib[2]
    count = 0
    for i in len(lib[3]):
        if count > limit:
            break
        if lib[3][i] not in checklist:
            res += books[lib[3][i]]
            count += 1
>>>>>>> 75d19e4787227c3ae602179a30b96896e5aba4e2
    return res
