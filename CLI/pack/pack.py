def print_pack(pages, ppack):
    start = 1
    finish = ppack
    i = 1

    print('PAIRS: ')
    with open('packs.txt', 'w') as pf:

        while finish < pages + 1:
            s = '#{:<2}  {:>3}-{:<3}'.format(i, start,finish)
            print(s)
            pf.write('%s\n'%(s))
            i += 1
            start += ppack
            finish += ppack
    
        
if __name__ == '__main__':    
    p = input('ENTER PAGES: ')
    print()

    pp = input('ENTER PACK SIZE: ')

    print_pack(int(p), int(pp))
    
    print()
    input('PRESS ENTER TO EXIT')
    
