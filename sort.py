def sort_books(books, lib_books):
    l = [(books[i], i) for i in lib_books]
    l.sort(key = lambda x: x[1], reverse = True)
    return [i[1] for i in l]

if __name__ == '__main__':
    print(sort_books([1,2,3], [0,2,1]))
    