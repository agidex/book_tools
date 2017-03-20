# book tools
book printing tools

Some userfull tools helps print books from PDF: splitting by gathering (so-called "packs"), calculating page numbers for print on two side of paper and other.
"pack" means gathering http://en.wikipedia.org/wiki/Gathering_%28bookbinding%29

## book_print
The combination of all tools. Type number of pages and "Calculate" - program shows you all possible variants of pages/pack_size. Select one and "Generate" - it will generate the print sequences of pages. Just copy/paste them into print dialog.

## CLI tools
Command line interface programs.
### ```pack.py```
Print the start and finish pages of every pack for given number of pages/pack size.

Example:
```
ENTER PAGES: 200
ENTER PACK SIZE: 20
PAIRS:
#1     1-20
#2    21-40
#3    41-60
#4    61-80
#5    81-100
#6   101-120
#7   121-140
#8   141-160
#9   161-180
#10  181-200
```
### ```pages.py```
Tries to calculate the right number of pages of your book (number of pages shoud divide by 4 without rest) and size and number of packs. The asterisk-marked line are good choice.

Example:
```
ENTER PAGES: 200
200 pages in book
PAGES IN PACKS:
A4  PAGES/PACK    PACKS
 1      4          50.0 packs *
 2      8          25.0 packs *
 3     12       16.6667 packs
 4     16          12.5 packs
 5     20          10.0 packs *
 6     24        8.3333 packs
 7     28        7.1429 packs
 8     32          6.25 packs
 9     36        5.5556 packs
10     40           5.0 packs *
11     44        4.5455 packs
12     48        4.1667 packs
13     52        3.8462 packs
14     56        3.5714 packs
```
### ```print_sick2.py```
And finally the generator of print sequences. Take number of pages and pack size and print 2 lines: SideA and SideB. Print SideA on one side of paper and SideB on the other side.

Example:
```
ENTER PAGES: 200
ENTER PACK SIZE: 20

SIDE A: 20,1,18,3,16,5,14,7,12,9,40,21,38,23,36,25,34,27,32,29,60,41,58,43,56,45
,54,47,52,49,80,61,78,63,76,65,74,67,72,69,100,81,98,83,96,85,94,87,92,89,120,10
1,118,103,116,105,114,107,112,109,140,121,138,123,136,125,134,127,132,129,160,14
1,158,143,156,145,154,147,152,149,180,161,178,163,176,165,174,167,172,169,200,18
1,198,183,196,185,194,187,192,189

SIDE B: 190,191,188,193,186,195,184,197,182,199,170,171,168,173,166,175,164,177,
162,179,150,151,148,153,146,155,144,157,142,159,130,131,128,133,126,135,124,137,
122,139,110,111,108,113,106,115,104,117,102,119,90,91,88,93,86,95,84,97,82,99,70
,71,68,73,66,75,64,77,62,79,50,51,48,53,46,55,44,57,42,59,30,31,28,33,26,35,24,3
7,22,39,10,11,8,13,6,15,4,17,2,19

LINES WRITTEN in "sequence.txt"
```
There are two lines in file sequence.txt. Copy/paste them into print dialog.

## REQUIREMENTS
Python 3.
