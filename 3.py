"""
3.Printing Star sequence (take n=4). The Program should be able to print for any number (n - 5,6,7, etc..)

     *
    * *
   * * *
  * * * *
   * * *
    * *
     *
"""
i = int(input("Enter The i Value:"));
n = 1+1
m = i
for j in range(1, i + 1, 1):
    for l in range(m, 1, -1):
        print(" ", end="")
    for k in range(j):
        print("* ", end="")
    print()
    m -= 1

for j in range(i-1, 0, -1):
    for l in range(1, n, 1):
        print(" ", end="")
    for k in range(j):
        print("* ", end="")
    print()
    n += 1

"""
Output:


Enter The i Value:8
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
  * * * * * * 
 * * * * * * * 
* * * * * * * * 
 * * * * * * * 
  * * * * * * 
   * * * * * 
    * * * * 
     * * * 
      * * 
       * 

"""