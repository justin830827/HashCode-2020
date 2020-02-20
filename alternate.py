from main import *
from algorithm import *

def sort_by_score(libs, cur_sign, total_day, books):
    l = [lib + [calculate_score(cur_sign, lib, total_day, books)] for lib in libs]
    l.sort(key = lambda x: x[-1], reverse = True)
    return [lib[:-1] for lib in l]
    
def alter():
    if len(sys.argv) < 2:
        print("No input file !!")
        exit()

    filename = sys.argv[1]

    specs, books, libs = read_file(filename)
    print("Specs: {}".format(specs))
    print("Books: {}".format(books))
    print("Libraies: {}".format(libs))

    lib_res = []
    books_res = []
    cur_sign = 0
    while cur_sign < specs[2] and libs:
        libs = sort_by_score(libs, cur_sign, specs[2], books)
        lib_res.append(libs[0][3])
        books_res.append(libs[0][4])
        cur_sign += libs[0][1]
        del libs[0]

    wirte(books_res, lib_res, filename + "_")
        

if __name__ == '__main__':
    alter()
    