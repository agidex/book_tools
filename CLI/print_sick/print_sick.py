def print_sick(pages):
    
    if (pages % 4) != 0:
        return None

    sheets = int(pages/4)

    side_a = []
    side_b = []
    
    for i in range(sheets):
        a1 = pages/2 + 1 + i*2
        a2 = pages/2 - i*2
        
        side_a.append(str(int(a2)))
        side_a.append(str(int(a1)))

        b1 = 1 + i*2
        b2 = pages - i*2

        side_b.append(str(int(b2)))
        side_b.append(str(int(b1)))

##    print(side_a)
##    print(side_b)

    return [side_a, side_b]
        
if __name__ == '__main__':    
    p = input('ENTER PAGES: ')
    print()

    [side_a, side_b] = print_sick(int(p))

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
    
