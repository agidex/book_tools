Print Scheme:
16 pages 4 sheets

            +------+
            |      |
            |      V
  --------  |  --------
  |  1A  |  |  |  4B  |
  |      |  |  |      |
  |16   1|  |  |8    9|
  --------  |  --------
     |      |     |
     V      |     V
  --------  |  --------
  |  2A  |  |  |  3B  |
  |      |  |  |      |
  |14   3|  |  |6   11|
  --------  |  --------
     |      |     |
     V      |     V
  --------  |  --------
  |  3A  |  |  |  2B  |
  |      |  |  |      |
  |12   5|  |  |4   13|
  --------  |  --------
     |      |     |
     V      |     V
  --------  |  --------
  |  4A  |  |  |  1B  |
  |      |  |  |      |
  |10   7|  |  |2   15|
  --------  |  --------
     |      |
     +------+

   Sheet layout:

  |------------------------------|        |------------------------------|
  |                              |        |                              |
  |             A(i)             |        |             B(i)             |
  |                              |        |                              |
  |-------------|  |-------------|        |-------------|  |-------------|
  | p*2*(i-1)   |  |   2*(i-1)+1 |        |     2*i     |  | p-2*(i-1)-1 |
  |==============================|        |==============================|


   "Part" process:

   1 -> 2 -> 3 -> 4 --    5 -> 6 -> 7 -> 8 --
                     |                      |
   1 <- 2 <- 3 <- 4 --    5 <- 6 <- 7 <- 8 --


   "Flow" process:

   1 -> 2 -> 3 -> 4 ----> 5 -> 6 -> 7 -> 8 --
                                            |
   1 <- 2 <- 3 <- 4 <---- 5 <- 6 <- 7 <- 8 --
