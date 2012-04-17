# RE Challenges

# Assign to the variable regexp a Python regular expression that matches single
# argument mathematical functions.

# the function name is a lowercase word (a-z), the function argument must be a 
# number (0-9), and there may optionally by spaces before and/or after the argument.

# Hint: it may not to escape the ( and ).
import re

regexp = r"[a-z]+\([ ]*-?[1-9][0-9]*[ ]*\)"

if __name__ == '__main__':
    # regex matches
    print re.findall(regexp, "cos(0)")
    print re.findall(regexp, "sqrt(  2  )")
    s
    # regex does not matches
    print re.findall(regexp, "cos   (0)")
    print re.findall(regexp, "sqrt(x)")

