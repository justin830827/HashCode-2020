def sort_lib(lib):
    return sorted(lib,key=lambda x: x[1])

def calculate_score(cur_sign,lib,total_day):
    return sum(lib[:(total_day-cur_sign)*lib[2]])
