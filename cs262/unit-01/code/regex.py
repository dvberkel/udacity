# Disjunction Construction

# Assign to the variable regexp a regular expression that matches either the
# exact string ab or one or more digits
import re

regexp = r"ab|[0-9]+"

if __name__ == '__main__':
    # regex matches
    print re.findall(regexp, "ab")
    print re.findall(regexp, "1")
    print re.findall(regexp, "123")

    # regex does not matches
    print re.findall(regexp, "a")
    print re.findall(regexp, "abc")
