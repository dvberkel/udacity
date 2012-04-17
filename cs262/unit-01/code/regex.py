# Disjunction Construction

# Assign to the variable regexp a regular expression that matches either the
# exact string ab or one or more digits
regexp = r"ab|[0-9]+"

if __name__ == '__main__':
    # regex matches
    print re.findall(regexp, "ab")
    print re.findall(regexp, "1")
    print re.findall(regexp, "123")

