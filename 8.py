"""
    i. Print all the names of the products in a list
    ii. Print the product of "green" color
    iii. Get the list of products that has same "options"
    iv. Get products list that has price in between 5000 to 15000
    v. Write a function that takes product name as input and prints product details with it's price
"""

products = [
    {
        "id": 1,
        "name": "samsung",
        "options": {
            "color": "red",
            "ram": 4,
            "screen": 6.1
        }
    },
    {
        "id": 2,
        "name": "apple",
        "options": {
            "color": "blue",
            "ram": 4,
            "screen": 5.5
        }
    },
    {
        "id": 3,
        "name": "nokia",
        "options": {
            "color": "red",
            "ram": 4,
            "screen": 6.1
            # "color": "green",
            # "ram": 4,
            # "screen": 6.0
        }
    },
    {
        "id": 4,
        "name": "redmi",
        "options": {
            "color": "green",
            "ram": 4,
            "screen": 6.0
        }
    }
]

prices = [
    {
        "id": 1,
        "product_id": 2,
        "price": 15000
    },
    {
        "id": 2,
        "product_id": 3,
        "price": 25000
    },
    {
        "id": 3,
        "product_id": 4,
        "price": 10000
    },
    {
        "id": 4,
        "product_id": 1,
        "price": 18000
    }
]

# i. Print all the names of the products in a list
print("###  i. Print all the names of the products in a list  ####")
for i in range(0, products.__len__()):
    print("   Product Name: ", products[i]["name"])

# ii. Print the product of "green" color
print("###  ii. Print the product of \"green\" color  ####")

for i in range(0, products.__len__()):
    if products[i]["options"]["color"] == "green":
        print("   Product Name: ", products[i]["name"])

# iii. Get the list of products that has same "options"
print("####  iii. Get the list of products that has same \"options\"  ###")

for i in range(0, products.__len__(), 1):
    for j in range(i + 1, products.__len__(), 1):
        if products[i]["options"] == products[j]["options"]:
            print("   These product has Same option: {}, {}".format(products[i]["name"], products[j]["name"]))

# iv. Get products list that has price in between 5000 to 15000
print("###   iv. Get products list that has price in between 5000 to 15000   ###")

print("   Product cost between  5000 to 15000")
for i in range(0, prices.__len__(), 1):
    if (prices[i]["price"] >= 5000) and (prices[i]["price"] <= 15000):
        print("   Product name :", products[i]["name"])
        print("   Color :", products[i]["options"]["color"])
        print("   RAM :", products[i]["options"]["ram"])
        print("   Screen :", products[i]["options"]["screen"])

# v. Write a function that takes product name as input and prints product details with it's price
print("###  v. Write a function that takes product name as input and prints product details with it's price  ###")


def fun(name):
    for i in range(0, products.__len__()):
        if products[i]["name"] == name:
            print("   Product name :", products[i]["name"])
            print("   Color :", products[i]["options"]["color"])
            print("   RAM :", products[i]["options"]["ram"])
            print("   Screen :", products[i]["options"]["screen"])
            for j in range(0, prices.__len__()):
                if products[i]["id"] == prices[j]["product_id"]:
                    print("   Price :", prices[j]["price"])


na = input("   Enter product name:")

fun(na)

"""
###  i. Print all the names of the products in a list  ####
   Product Name:  samsung
   Product Name:  apple
   Product Name:  nokia
   Product Name:  redmi
###  ii. Print the product of "green" color  ####
   Product Name:  redmi
####  iii. Get the list of products that has same "options"  ###
   These product has Same option: samsung, nokia
###   iv. Get products list that has price in between 5000 to 15000   ###
   Product cost between  5000 to 15000
   Product name : samsung
   Color : red
   RAM : 4
   Screen : 6.1
   Product name : nokia
   Color : red
   RAM : 4
   Screen : 6.1
###  v. Write a function that takes product name as input and prints product details with it's price  ###
   Enter product name:redmi
   Product name : redmi
   Color : green
   RAM : 4
   Screen : 6.0
   Price : 10000

Process finished with exit code 0

"""
