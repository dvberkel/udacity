# Regexp Details and Challenges

# Assign to the variable regexp a Python regular expression that matches
# lowercase words (a-z) or singly-hyphenated lowercase words

# Hint: it may not be possible to get correctly - do your best!
regexp = r"[a-z]+(?:-[a-z]+)?"

if __name__ == '__main__':
    # regex matches
    print re.findall(regexp, "well-liked")
    print re.findall(regexp, "html")
    
    # regex does not matches
    print re.findall(regexp, "a-b-c")
    print re.findall(regexp, "a--b")

