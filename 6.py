"""
6. Print the Highest sum of two numbers and the two numbers of an array (Program should work for any array given as input)
[5, 18, 25, -15, 20, 10, -5]
"""
def sort_fun(val):
    for i in range(len(val) - 1, 0, -1):
        for j in range(i):
            if (val[i] > val[j]):
                t = val[i];
                val[i] = val[j]
                val[j] = t


num = int(input("Enter number of elements:"))
val = []
print("Enter element:")
for i in range(1, num + 1):
    a = int(input())
    val.append(a)
print("Array is : {}".format(val))

sort_fun(val)
print("Highest Sum Of Two Number:{}+{}={}".format(val[0], val[1], val[0] + val[1]))

print(val)

# """
#
#
#
# Output:
#
#
# Enter number of elements:7
# Enter element:
# 5
# 18
# 25
# -15
# 20
# 10
# -5
# Array is : [5, 18, 25, -15, 20, 10, -5]
# Highest Sum Of Two Number:20+25=45
# """
