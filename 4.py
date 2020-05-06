"""
4.Printing Star sequence (take n=4). The Program should be able to print for any number (n - 5,6,7, etc..)
*
* *
* * *
* * * *

"""
i = int(input("Enter The i Value:"));
for j in range(1, i+1):
    for k in range(j):
        print("* ", end="")
    print()

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
"""