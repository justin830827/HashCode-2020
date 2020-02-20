import sys
from algorithm import *


def sort_books(books, lib_books):
    """
    Input: 
        books: book score list
        lib_books: list of books in the library
    Output:
        the sorted list of books
    """
    l = [(books[i], i) for i in lib_books]
    l.sort(key=lambda x: x[0], reverse=True)
    return [i[1] for i in l]


def read_file(filename):
    """
    Args:
        filename: the filename without extension in ./Data

    Return:
        specs: a tuple with tuple[0] = number of books, tuple[1] = number of library,
               tuple[2] = the deadline of scanning books.
        books: a list with scroe of books. Index of list indicates the book id,
               the value of list indicates the score value.
        libs:  a list of libraries.
               library[i][0] = number of books in lib.
               library[i][1] = signup process days.
               library[i][2] = maximum ship per day.
               library[i][3] = a set contains all the books with id in the lib.

    """
    path = './Data/' + filename + '.txt'
    with open(path, 'r') as f:
        specs = f.readline().split()
        # Save basic specs on first line of input files.
        n_book, n_lib, deadline = int(specs[0]), int(specs[1]), int(specs[2])

        # Save books with its score.
        books = list(map(int, f.readline().split()))
        row = 0

        # Save libraies information with [signup, max_ship, books(set)]
        libs = []
        idx = 0
        while n_lib > row/2:
            if row % 2 == 0:
                cur_lib = list(map(int, f.readline().split())) + [idx]
                idx += 1
                libs.append(cur_lib)
            else:
                # append libray's books into its library_id
                libs[-1].append(sort_books(books,
                                           list(map(int, f.readline().split()))))
            row += 1

    return (n_book, n_lib, deadline), books, libs


def wirte(sent_books, libs, filename):
    path = './Output/' + filename + '.txt'
    with open(path, 'w') as f:
        f.write('{}\n'.format(len(libs)))
        for i in range(len(libs)):
            f.write(str(libs[i]) + ' ' + str(len(sent_books[i])) + '\n')
            for book in sent_books[i]:
                f.write(str(book) + ' ')
            f.write('\n')


def main():
    if len(sys.argv) < 2:
        print("No input file !!")
        exit()

    filename = sys.argv[1]

    specs, books, libs = read_file(filename)
    print("Specs: {}".format(specs))
    print("Books: {}".format(books))
    print("Libraies: {}".format(libs))

    libs = sort_lib(libs)
    #print("Libraies: {}".format(libs))

    lib_res = []
    books_res = []

    checklist = set()

    for lib in libs:
       
        cur_scan = []
        for book in lib[4]:
            if book not in checklist:
                cur_scan.append(book)
                checklist.add(book)
        if  cur_scan:
            lib_res.append(lib[3])
            books_res.append(cur_scan)

    wirte(books_res, lib_res, filename)


if __name__ == '__main__':
    main()
