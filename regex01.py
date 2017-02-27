import re
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."

##re.sub('string to be replaced', 'Replace with', string to be manipulated)

new = re.sub('[A-Z]', '', string)
print ("=========")
print (string)
print (new)

new = re.sub('[a-z]', '', string)
print ("=========")
print (string)
print (new)

new = re.sub('[.,\']', '', string)
print ("=========")
print (string)
print (new)

new = re.sub('[.,\'a-z]', '',  string)
print ("=========")
print (string)
print (new)

new = re.sub('[.,\'a-zA-Z]', '', string)
print ("=========")
print (string)
print (new)

new = re.sub('[.,\'A-Z]', '', string)
print ("=========")
print (string)
print (new)

new = re.sub('[.,\'A-Z+" "]', '', string)
print ("=========")
print (string)
print (new)

string = "'I AM NOT YELLING', she said. Though we knew it to not be true.6 454 - 343"
new = re.sub('[^0-9]', '', string)
print ("=========")
print (string)
print (new)
