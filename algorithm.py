def sort_lib(lib):
    return sorted(lib, key=lambda x: x[1])


def calculate_score(cur_sign, lib, total_day, books,checklist):
    res = 0
    limit=(total_day-cur_sign)*lib[2]
    count=0
    for i in len(lib[3]):
        if count>limit:
            break
        if lib[3][i] not in checklist:
            res += books[lib[3][i]]
            count+=1
    return res
