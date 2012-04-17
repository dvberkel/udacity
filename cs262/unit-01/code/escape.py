# Tricky REs with ^ and \

# Assign to the regexp a regular expression for double quoted string literals that
# allows for escaped double quotes.

# Hint: escape " and \
# Hint: (?: (?: ) )
import re

regexp = r'"(?:[^\\]|(?:\\.))*"'

if __name__ == '__main__':
    # regex matches
    print re.findall(regexp, '"I say \\"Hello\\"')
    
    # regex does not matches
    print re.findall(regexp, '"\\')
