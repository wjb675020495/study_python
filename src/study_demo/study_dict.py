def histogram(s):
    d = dict()
    for line in s:
        if line not in d:
            d[line] = 1
        else:
            d[line] += 1
    return d


def refactor_histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    # d.get() 得到的时一个int类型的值,即dict的value，若key存在则返回key对应的value，否则，返回后面的默认值
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


if __name__ == '__main__':
    print(histogram("qwer"))
    print(type(histogram("qwer").get("q", 0)))
    print(refactor_histogram("qwer"))
    print_hist(histogram("qwer"))
    print(sorted(histogram("qwer")))
    for i in sorted(histogram("qwer")):
        print(i, histogram("qwer")[i])