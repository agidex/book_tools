ORDER_LEFT_RIGHT = True

def A(i, pages, offset=0):
    left = pages - 2*(i - 1)
    right = 2*(i - 1) + 1

    
    if ORDER_LEFT_RIGHT:
        return (left + offset, right + offset)

    return (left + offset, right + offset)[::-1]
    

def B(i, pages, offset=0):
    left = 2*i
    right = pages - 2*(i - 1) - 1

    if ORDER_LEFT_RIGHT:
        return (left + offset, right + offset)

    return (left + offset, right + offset)[::-1]


def print_sick2(pages, pack_size):
    packs = int(pages / pack_size)

    seq_A = []
    seq_B = []

    sheets = int(pack_size / 4)
    for pack in range(packs):
        offset = pack * pack_size
        for i in range(1, sheets + 1):
            seq_A.append(A(i, pack_size, offset))
            seq_B.append(B(i, pack_size, offset))

    return (seq_A, seq_B[::-1])

def flatten(lst):
    '''
    make (1, 2, 3, 4, 5, 6)
    from ((1, 2), (3, 4), (5, 6))
    '''
    lst2 = []
    for pair in lst:
        lst2.extend(pair)

    return lst2
    
def test2():
    pages = 60
    pack_size = 20

    a, b = print_sick2(pages, pack_size)
    
    print(flatten(a))
    print(flatten(b))

def test3():
    pages = 32
    pack_size = 32

    a, b = print_sick2(pages, pack_size)
    print(a)
    print(b)

    a, b = print_sick(pages)
    print(a)
    print(b)    


def test1():
    pages = 16
    offset = 0
    sheets = [i for i in range(1, int(pages/4) + 1)]

    print('SIDE A')
    for i in sheets:
        print(i, A(i, pages, offset))
    print('SIDE B')
    for i in sheets[::-1]:
        print(i, B(i, pages, offset))


#test2()

if __name__ == '__main__':    
    pages = int(input('ENTER PAGES: '))
    pack_size = int(input('ENTER PACK SIZE: '))
    
    print()

    [side_a, side_b] = print_sick2(pages, pack_size)
    [side_a, side_b] = [flatten(side_a), flatten(side_b)]

    side_a = list(map(lambda item: str(item), side_a))
    side_b = list(map(lambda item: str(item), side_b))
    
    line_a = ','.join(side_a)
    line_b = ','.join(side_b)

    with open('sequence.txt', 'w') as sf:
        sf.write('%s\n'%(line_a))
        sf.write('%s\n'%(line_b))

    print('SIDE A:', line_a)
    print()
    print('SIDE B:', line_b)
    print()
    print('LINES WRITTEN in "sequence.txt"')

    print()
    input('PRESS ENTER TO EXIT')













    
