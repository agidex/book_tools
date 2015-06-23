PAGES_IN_PACK_MAX = 60
PACKS = [i for i in range(PAGES_IN_PACK_MAX) if i % 4 == 0 and i != 0]

def pages(n):
    print('%s pages in book'%(n))
    print('PAGES IN PACKS:')
    pages = float(n)
    
    print('{:>2}  {:>3} {:>8}'.format('A4', 'PAGES/PACK', 'PACKS'))
    for pages_in_pack in PACKS:
        
        a4_lists = int(pages_in_pack/4)
        packs_count = round(pages / pages_in_pack, 4)
        text = 'packs'
        if pages % pages_in_pack == 0:
            text += ' *'
        print('{:>2}    {:>3}      {:>8} {}'.format(a4_lists, pages_in_pack, packs_count, text))


if __name__ == '__main__':    
    p = input('ENTER PAGES: ')
    print()

    pages(int(p))

    print()
    input('PRESS ENTER TO EXIT')
