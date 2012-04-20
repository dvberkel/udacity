def nfsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            for option in edges[(current, letter)]:
                if nfsmsim(string[1:], option, edges, accepting):
                    return True
        return False
