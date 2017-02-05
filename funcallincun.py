def cube(number):
    return number**3
    print ("cube")
def by_three(number):
    if number % 3 == 0:
        return cube(number)
        print ("called cube")
    else:
        print ("exiting")
        return False
        
print by_three(3)
