"""
6. Print the Highest sum of two numbers and the two numbers of an array (Program should work for any array given as input)
[5, 18, 25, -15, 20, 10, -5]
"""
num = int(input("Enter number of elements:"))
val = []
print("Enter element:")
for i in range(1, num + 1):
    a = int(input())
    val.append(a)
print("Array is : {}".format(val))
val.sort()
print("Highest Sum Of Two Number:{}+{}={}".format(val[num - 2], val[num - 1], val[num - 2] + val[num - 1]))

"""
Enter number of elements:7
Enter element:
5
18
25
-15
20
10
-5
Array is : [5, 18, 25, -15, 20, 10, -5]
Highest Sum Of Two Number:20+25=45
"""
