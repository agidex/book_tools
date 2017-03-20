PACK_SIZE_MAX = 60
ORDER_LEFT_RIGHT = True

#   |------------------------------|        |------------------------------|
#   |                              |        |                              |
#   |             A(i)             |        |             B(i)             |
#   |                              |        |                              |
#   |-------------|  |-------------|        |-------------|  |-------------|
#   | p*2*(i-1)   |  |   2*(i-1)+1 |        |     2*i     |  | p-2*(i-1)-1 |
#   |==============================|        |==============================|


def calculate_packs(pages):
    packs = [i for i in range(PACK_SIZE_MAX) if i % 4 == 0 and i != 0]

    pages_f = float(pages)

    packs_lst = []

    for pack_size in packs:
        is_good = False
        a4_count = int(pack_size/4)
        pack_count = round(pages_f/pack_size, 4)
        if pages_f % pack_size == 0:
            is_good = True
        line = (a4_count, pack_size, pack_count, is_good)
        packs_lst.append(line)

    return packs_lst


def A(i, pages, offset=0):
    left = pages - 2*(i - 1)
    right = 2*(i - 1) + 1

    if ORDER_LEFT_RIGHT:
        return left + offset, right + offset

    return (left + offset, right + offset)[::-1]


def B(i, pages, offset=0):
    left = 2*i
    right = pages - 2*(i - 1) - 1

    if ORDER_LEFT_RIGHT:
        return left + offset, right + offset

    return (left + offset, right + offset)[::-1]


def print_sick2(pages, pack_size):
    packs = int(pages / pack_size)

    seq_a = []
    seq_b = []

    sheets = int(pack_size / 4)
    for pack in range(packs):
        offset = pack * pack_size
        for i in range(1, sheets + 1):
            seq_a.extend(A(i, pack_size, offset))
            seq_b.extend(B(i, pack_size, offset))

    return seq_a, seq_b[::-1]


def flatten(lst):
    '''
    make (1, 2, 3, 4, 5, 6)
    from ((1, 2), (3, 4), (5, 6))
    '''
    lst2 = []
    for pair in lst:
        lst2.extend(pair)

    return lst2

