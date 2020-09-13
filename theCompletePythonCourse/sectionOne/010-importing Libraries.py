import re


string = " 'I AM NOT YELLING!' she said, though we knew it not to be true. 1"

print(string)

new = re.sub('[A-Z]', ' ', string)          #this calls the substitute function from the reg-ex library, and substitutes spaces for all capitol letters

print(new)

new = re.sub('[a-z]', ' ', string)          #this calls the substitute function from the reg-ex library, and substitutes spaces for all lower case letters

print(new)

new = re.sub('[.,\']', ' ', string)          #this calls the substitute function from the reg-ex library, and substitutes spaces for all punctuation

print(new)
