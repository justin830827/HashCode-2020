import sys


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
        while n_lib > row/2:
            if row % 2 == 0:
                cur_lib = list(map(int, f.readline().split()))
                libs.append(cur_lib)
            else:
                # append libray's books into its library_id
                libs[-1].append(set(map(int, f.readline().split())))
            row += 1

    return (n_book, n_lib, deadline), books, libs


def wirte(results, filename):
    path = './Output/' + filename + '.txt'
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(results)))
        for res in results:
            f.write(str(res) + ' ')


def main():
    if len(sys.argv) < 2:
        print("No input file !!")
        exit()

    filename = sys.argv[1]

    specs, books, libs = read_file(filename)
    print("Specs: {}".format(specs))
    print("Books: {}".format(books))
    print("Libraies: {}".format(libs))


if __name__ == '__main__':
    main()
