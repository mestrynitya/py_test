shopping_list = ["banana", "orange", "apple", "pear"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
#    print food
    for item in food:
#        print item
 #       print prices[item]
#        print stock[item]
        if stock[item] > 0:
            total +=  prices[item]
            stock[item] -= 1
    return total
