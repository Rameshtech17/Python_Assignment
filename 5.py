"""
5.Printing Star sequence (take n=4). The Program should be able to print for any number (n - 5,6,7, etc..)

    * * * *
      * * *
        * *
          *

"""
i = int(input("Enter The i Value:"))
n = 1
for j in range(i, 0, -1):
    for l in range(n, 1, -1):
        print(" ", end="")
    for k in range(j):
        print(" *", end="")
    print()
    n += 2


""""   
Output:


Enter The i Value:8
 * * * * * * * *
   * * * * * * *
     * * * * * *
       * * * * *
         * * * *
           * * *
             * *
               *
"""