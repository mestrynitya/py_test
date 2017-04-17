import sys

print ("NUmber of arguments: ", len(sys.argv),  "arguments.")
print ("Arguments ", sys.argv)

## remove arguments
sys.argv.remove(sys.argv[0])
print ("Arguemnts ", sys.argv)

# sum up
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number

    except Exception:
        print ("bad input")

print (sum)

print ("hello")

colour = input("what is favourite colour")
print (colour)