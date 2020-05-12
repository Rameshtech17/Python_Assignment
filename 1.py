"""

1.Printing Star sequence (take n=4). The Program should be able to print for any number (n - 5,6,7, etc..)
* * * *
 * * *
  * *
   *

"""

# i = int(input("Enter The i Value:"));
# n = 1
# for j in range(i, 0, -1):
#     for l in range(1, n, 1):
#         print(" ", end="")
#     for k in range(j):
#         print(" *", end="")
#     print()
#     n += 1


"""
Output:


Enter The i Value:6
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
"""
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("* "*i)
    print("\n".join(myList))

# Driver Code
n = 5
pypart(n)