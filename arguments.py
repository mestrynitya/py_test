import sys

print ("NUmber of arguments: ", len(sys.argv),  "arguments.")
print ("Arguments ", sys.argv)

## remove arguments
sys.argv.remove(sys.argv[0])
print ("Arguemnts ", sys.argv)