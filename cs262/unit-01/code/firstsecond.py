# Selecting Substrings : Writing a Python Procedure

# Let p and q each be string containing two words separated by a space.

# Examples:
#   "bell hooks"
#   "grace hopper"
#   "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q.

def myfirst_yoursecond(p,q):
    first = p[0:p.find(" ")]
    second = q[q.find(" ") + 1:]
    return first == second

if __name__ == '__main__':
    print myfirst_yoursecond("bell hooks", "curer bell")
