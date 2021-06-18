def insert_dash(num):
    num = str(num)
    nmap = map(int, num)
    nlist = list(nmap)
    size = len(nlist)
    offset = 0

    for i in nlist:
        if int(num[i]) % 2 != 0 and int(num[i + 1]) % 2 != 0:
            nlist.insert(i + offset, '-')
            offset += 1
    res = str(nlist)

    return res


if __name__ == '__main__':

    print(insert_dash(27566317))
