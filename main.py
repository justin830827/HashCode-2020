import sys


def read_file(filename):
    path = './Data/' + filename + '.in'
    with open(path, 'r') as f:
        spec = f.readline().split()
        target, number = int(spec[0]), int(spec[1])
        candidates = list(map(int, f.readline().split()))

    return target, number, candidates


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

    read_file(filename)


if __name__ == '__main__':
    main()
